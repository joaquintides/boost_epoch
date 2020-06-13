# Boost epoch proposal: legacy checker
#
# Copyright 2020 Joaquin M Lopez Munoz.
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)
#
# See https://github.com/joaquintides/boost_epoch/ for project home page.

import argparse
import math
import os
import re
import sys

def dir_size(path): #https://stackoverflow.com/a/1392549/213114
  total_size = 0
  for dirpath, dirnames, filenames in os.walk(path):
    for f in filenames:
      fp = os.path.join(dirpath, f)
      if not os.path.islink(fp):
        total_size += os.path.getsize(fp)
  return total_size

parser=argparse.ArgumentParser(description="Boost epoch legacy checker")
parser.add_argument(
  "--boost-root",dest="path_to_boost",default=os.environ.get("BOOST_ROOT"),
  help="path to Boost (default uses BOOST_ROOT environment variable)")
args=parser.parse_args()       

boost_root=args.path_to_boost
if not boost_root:
  sys.stdout.write("Path to Boost not available\n")
  exit()
boost_root_libs=os.path.join(boost_root,"libs")
legacy_modules=["array","bind","function","lambda","mpl","smart_ptr","thread","tuple"]

def module_size(module):
  module_path=os.path.join(boost_root_libs,module)
  return dir_size(os.path.join(module_path,"include"))+\
         dir_size(os.path.join(module_path,"src"))

libs_path=re.compile(r"^\s*path\s*=*\slibs/(\S*)\s*$")
with open(os.path.join(boost_root,".gitmodules"),"r") as gitmodules:
  modules=sorted({
    m.group(1) for m in map(libs_path.match,gitmodules.readlines()) if m})
modules.remove("headers") # fake module
module_sizes={module:module_size(module) for module in modules}

first_column_width=max(map(len,modules))
legacy_label="legacy"
last_column_width=max(len(legacy_label),4)

sys.stdout.write("|"+"".center(first_column_width))
for legacy_module in legacy_modules:
  sys.stdout.write("|"+legacy_module.center(3))
sys.stdout.write("|"+legacy_label+"|\n")
sys.stdout.write("|"+"-"*first_column_width)
for legacy_module in legacy_modules:
  sys.stdout.write("|:"+"-"*max(len(legacy_module)-2,1)+":")
sys.stdout.write("|"+"-"*(last_column_width-1)+":|\n")
  
for module in modules:
  sys.stdout.write("|"+module.ljust(first_column_width))

  report_filename="temp.txt"
  if os.system(
    "boostdep --boost-root \""+boost_root+
    "\" --track-sources --subset "+module.replace("/","~")+
    " >"+report_filename):
    break
  report_file=open(report_filename,"r")
  report=report_file.read()
  report_file.close()
  os.remove(report_filename)
  
  legacy_size=0
  total_size=0
  legacy_dep={module:False for module in legacy_modules}
  for dep_module in modules:
    if dep_module+":" in report:
      dep_size=module_sizes[dep_module]
      total_size+=dep_size
      if dep_module in legacy_modules:
        legacy_size+=dep_size
        legacy_dep[dep_module]=True

  for legacy_module in legacy_modules:
    if legacy_dep[legacy_module]:
      output=str(int(math.ceil(100.0*module_sizes[legacy_module]/total_size)))+"%"
    else: output=""
    sys.stdout.write("|"+output.center(len(legacy_module)))
  legacy=int(math.ceil(100.0*legacy_size/total_size)) if total_size!=0 else 0
  sys.stdout.write("|"+(str(legacy)+"%").rjust(last_column_width)+"|\n")
