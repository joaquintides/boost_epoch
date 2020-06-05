# boostgrep
#
# Copyright 2020 Joaquin M Lopez Munoz.
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)
#
# See https://github.com/joaquintides/boost_epoch/ for project home page.

import argparse
import os
import re
import sys

parser=argparse.ArgumentParser(description="Boost grep")
parser.add_argument(
  "-b","--boost-root",metavar="<path-to-boost>",
  dest="path_to_boost",default=os.environ.get("BOOST_ROOT"),
  help="path to Boost (default uses BOOST_ROOT environment variable)")
parser.add_argument(
  "-v","--verbose",action="store_true",help="verbose mode")
parser.add_argument(
  "-f","--first_only",action="store_true",
  help="show just the first match per module (in verbose mode)")
parser.add_argument(
  "term",metavar="<term>",
  help="grepped term (regexp), strings outside pp directives and "\
       "comments are not considered")
parser.add_argument(
  "module",metavar="<module>",nargs="?",
  help="restrict search to <module>")
args=parser.parse_args()

boost_root=args.path_to_boost
if not boost_root:
  sys.stderr.write("Path to Boost not available\n")
  exit(1)
if not os.path.exists(boost_root):
  sys.stderr.write("Can't find "+boost_root+"\n")
  exit(1)
boost_root_libs=os.path.join(boost_root,"libs")
libs_path=re.compile(r"^\s*path\s*=*\slibs/(\S*)\s*$")
with open(os.path.join(boost_root,".gitmodules"),"r") as gitmodules:
  modules=sorted({
    m.group(1) for m in map(libs_path.match,gitmodules.readlines()) if m})
include_path={module:os.path.join(boost_root_libs,module,"include")
              for module in modules}
src_path={module:os.path.join(boost_root_libs,module,"src")
              for module in modules}

verbose_mode=args.verbose
first_only_mode=args.first_only
term=re.compile(args.term)
target_module=args.module
if target_module and not target_module in modules:
  sys.stderr.write("Can't find "+target_module+"\n")
  exit(1)
  
# remove comments and strings (except strings in pp directives)
def clean_lines(lines):
  def coda(line):
    if len(line)>1 and line[-2:]=="\\\n": return "\\\n"
    if len(line)>0 and line[-1:]=="\n": return "\n"
    return ""
    
  prefix=re.compile(r"#|/\*|\"|//")
  prefix_in_pp_directive=re.compile(r"/\*|//")
  all_blank=re.compile(r"^\s*$")
  c_comment_suffix=re.compile(r"\*/")
  str_suffix=re.compile(r"^\"|[^\\]\"")
  in_c_comment=False
  in_string=False
  in_pp_directive=False
  for line in lines:
    original_line=line
    index=0
    while index<len(line):
      if in_c_comment:
        match=c_comment_suffix.search(line[index:])
        if match:
          rest=index+match.end()
          line=line[:index]+line[rest:]
          in_c_comment=False
        else:
          line=line[:index]+coda(line)
          break
      elif in_string:
          match=str_suffix.search(line[index:])
          if match:
            rest=index+match.end()
            line=line[:index]+line[rest:]
            in_string=False
          else:
            line=line[:index]+coda(line)
            break
      else:
        if in_pp_directive: match=prefix_in_pp_directive.search(line[index:])
        else: match=prefix.search(line[index:])
        if not match: break
        else:
          matched=match.group()
          start=index+match.start()
          rest=index+match.end()
          if matched=="#":
            in_pp_directive=(all_blank.match(line[:start])!=None)
            index=rest
          elif matched=="/*":
            line=line[:start]+line[rest:]
            index=start
            in_c_comment=True
          elif matched=="\"":
            line=line[:start]+line[rest:]
            index=start
            in_string=True
          else: # "//"
            line=line[:start]+coda(line)
            break
    yield (line,original_line)
    if len(line)<2 or line[-2:]!="\\\n":
      in_string=False
      in_pp_directive=False

    
def grep_file(filename,first_only=True):
  line_count=0
  unfinished_comment=False
  res=[]
  with open(filename,"r") as file:
    for line,original_line in clean_lines(file.readlines()):
      if term.search(line):
        res.append((filename,line_count,original_line))
        if first_only: return res;
      line_count+=1
  return res

def grep_dir(path,first_only=True):
  admitted_extensions={".h",".c",".hpp",".cpp",".hh",".cc",".h+",".c+",".h++",".c++"}
  res=[]
  for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
      if not os.path.splitext(filename)[1].lower() in admitted_extensions: continue
      res+=grep_file(os.path.join(dirpath,filename),first_only)
      if first_only and res: return res
  return res

def grep_module(module,first_only=True):
  res=grep_dir(os.path.join(include_path[module]),first_only)
  if first_only and res: return res
  res+=grep_dir(os.path.join(src_path[module]))
  return res

module_count=0
for module in modules if not target_module else [target_module]:
  res=grep_module(module,first_only=not verbose_mode or first_only_mode)
  if res:
    sys.stdout.write(module+"\n")
    module_count+=1
    if verbose_mode:
      for item in res:
        sys.stdout.write("  "+os.path.relpath(item[0],boost_root_libs)+":"+str(item[1])+"\n")
        sys.stdout.write("  "+item[2])
sys.stdout.write("module count: "+str(module_count)+"\n")
