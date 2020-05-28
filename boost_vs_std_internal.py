# Boost epoch proposal: Boost vs std components within non-C++03 Boost libs
#
# Copyright 2020 Joaquin M Lopez Munoz.
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)
#
# See https://github.com/joaquintides/boost_epoch/ for project home page.

import argparse
import os
import sys

parser=argparse.ArgumentParser(
  description="Reporter for Boost vs std components within non-C++03 Boost libs")
parser.add_argument(
  "-b","--boost-root",metavar="<path-to-boost>",
  dest="path_to_boost",default=os.environ.get("BOOST_ROOT"),
  help="path to Boost (default uses BOOST_ROOT environment variable)")
args=parser.parse_args()

boost_root=args.path_to_boost
if not boost_root:
  sys.stderr.write("Path to Boost not available\n")
  exit(1)
if not os.path.exists(boost_root):
  sys.stderr.write("Can't find "+boost_root+"\n")
  exit(1)

legacy_modules=["array","bind","function","lambda","mpl","smart_ptr","thread","tuple"]
cp11_components=[
  ("std::array",[r"\s*#\s*include\s*<array>"]),
  ("std::bind",["std::bind"]),
  ("std::function",["std::function","std::mem_fn"]),
  ("boost::mp11",[r"\s*#\s*include\s*<boost/mp11"]),
  ("std::shared_ptr",["std::shared_ptr","std::make_shared"]),
  ("std::thread",[r"\s*#\s*include\s*<thread>"]),
  ("std::tuple",[r"\s*#\s*include\s*<tuple>"])]
non_cpp03_modules=["beast","context","contract","coroutine2","fiber","gil","hana","histogram",
                   "hof","mp11","outcome","poly_collection","process","safe_numerics",
                   "static_string","variant2","vmd","yap"] # add "stl_interfaces" in Boost 1.74

report_filename="temp.txt"

def grep_for(term,module):
  if os.system(
    "boostgrep.py --boost-root \""+boost_root+"\" \""+\
    term+"\" "+module+" >"+report_filename):
    exit(1)
  with open(report_filename,"r") as report_file: report=report_file.read()
  os.remove(report_filename)
  return "module count: 1" in report

first_column_width=max(map(len,non_cpp03_modules))
headers=list(map(lambda x: "boost::"+x,legacy_modules))+\
        list(map(lambda x: x[0],cp11_components))

sys.stdout.write("|"+"".center(first_column_width))
for header in headers:
  sys.stdout.write("|"+header.center(3))
sys.stdout.write("|\n")
sys.stdout.write("|"+"-"*first_column_width)
for header in headers:
  sys.stdout.write("|:"+"-"*max(len(header)-2,1)+":")
sys.stdout.write("|\n")

for module in non_cpp03_modules:
  sys.stdout.write("|"+module.ljust(first_column_width))
  column=0
  
  if os.system(
    "boostdep --boost-root \""+boost_root+"\" --primary "+module+" >"+report_filename):
    exit(1)
  with open(report_filename,"r") as report_file: report=report_file.read()
  os.remove(report_filename)
  for legacy_module in legacy_modules:
    output="X" if legacy_module+":" in report else " "
    sys.stdout.write("|"+output.center(len(headers[column])))
    column+=1
 
  for component,terms in cp11_components:
    output="X" if any(grep_for(term,module) for term in terms) else ""
    sys.stdout.write("|"+output.center(len(headers[column])))
    column+=1

  sys.stdout.write("|\n")
