# boostcdep: Boost conditional dependency calculator
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

parser=argparse.ArgumentParser(description="Boost conditional dependency calculator")
parser.add_argument(
  "-b","--boost-root",metavar="<path-to-boost>",
  dest="path_to_boost",default=os.environ.get("BOOST_ROOT"),
  help="path to Boost (default uses BOOST_ROOT environment variable)")
parser.add_argument(
  "-c","--config-info",metavar="<config-file>",
  dest="config_info",required=True,
  help="path to config info file")
parser.add_argument(
  "-D",metavar="<pp-symbol>",
  dest="symbols",action="append",
  help="predefined preprocessor symbol (can be used multiple times)")
parser.add_argument(
  "-v","--verbose",action="store_true",help="verbose mode")
parser.add_argument(
  "module",metavar="<module>",help="Boost module name")
args=parser.parse_args()

boost_root=args.path_to_boost
if not boost_root:
  sys.stderr.write("Path to Boost not available\n")
  exit(1)
if not os.path.exists(boost_root):
  sys.stderr.write("Can't find "+boost_root+"\n")
  exit(1)
boost_root_libs=os.path.join(boost_root,"libs")
modules=filter(
  lambda x: os.path.isdir(os.path.join(boost_root_libs,x)),
  os.listdir(boost_root_libs))
modules.remove("headers") # fake module
include_path={module:os.path.join(boost_root_libs,module,"include")
              for module in modules}
src_path={module:os.path.join(boost_root_libs,module,"src")
              for module in modules}

if os.system("wave -v >nul 2>nul")!=0:
  sys.stderr.write("Can't execute wave\n")
  exit(1)

wave_cfg_filename="wave_cfg.txt"
wave_out_filename="wave_out.txt"

with open(wave_cfg_filename,"w") as wave_cfg:
  wave_cfg.write("--output\n-\n")
  wave_cfg.write("--long_long\n")
  wave_cfg.write("--c++11\n")
  wave_cfg.write("--listincludes\n"+wave_out_filename+"\n")
  wave_cfg.write("-DBOOST_PP_VARIADICS=0\n") # wave chokes on Boost.PP otherwise
  wave_cfg.write("-DBOOST_COMPILER_CONFIG=\"\"\n")
  wave_cfg.write("-DBOOST_STDLIB_CONFIG=\"\"\n")
  wave_cfg.write("-DBOOST_PLATFORM_CONFIG=\"\"\n")
  if args.symbols:
    for symbol in args.symbols: wave_cfg.write("-D"+symbol+"\n")

  for module in modules:
    wave_cfg.write("-S"+include_path[module]+"\n")

  config_info=args.config_info
  if not os.path.exists(config_info):
    sys.stderr.write("Can't find "+config_info+"\n")
    exit(1)
  config_file=open(config_info,"r")
  pattern1="^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=(.*)\s*$"
  pattern2="^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\[no value\]\s*$"
  blocked_symbols={
      "__STDC__","__cplusplus","__LINE__",
      "__FILE__","__BASE_FILE__","__DATE__",
      "__TIME__","__INCLUDE_LEVEL__","__WAVE__",
      "__SPIRIT_PP__","__WAVE_VERSION__","__SPIRIT_PP_VERSION__",
      "__WAVE_VERSION_STR__","__SPIRIT_PP_VERSION_STR__","__STDC_VERSION__",
      "__STDC_HOSTED__","__WAVE_HAS_VARIADICS__","__WAVE_CONFIG__",
      "BOOST_COMPILER_CONFIG","BOOST_STDLIB_CONFIG","BOOST_PLATFORM_CONFIG"}
  for line in config_file.readlines():
    symbol_name=None
    symbol_def=None
    match=re.match(pattern1,line)
    if match:
      symbol_name=match.group(1)
      symbol_def=match.group(2)
    else:
      match=re.match(pattern2,line)
      if match: symbol_name=match.group(1)
    if symbol_name and not symbol_name in blocked_symbols:
      wave_cfg.write("-D"+symbol_name)
      if symbol_def: wave_cfg.write("="+symbol_def)
      wave_cfg.write("\n")

verbose_mode=args.verbose
dependencies=set()

def add_dependencies_file(filename):
  os.system("wave --config-file "+wave_cfg_filename+" \""+filename+"\" 2>nul")
  with open(wave_out_filename,"r") as wave_out:
    pattern="^\s*(<.*>)\s*\((.*)\)\s*$"
    for line in wave_out.readlines():
      match=re.match(pattern,line)
      if match:
        path=match.group(2)
        for module in modules:
          if os.path.commonprefix([include_path[module],path])==include_path[module]:
            dependencies.add(module)
            break

def add_dependencies_dir(path):
  admitted_extensions={".h",".c",".hpp",".cpp",".hh",".cc",".h+",".c+",".h++",".c++"}
  excluded_subdirs={"detail","impl"}
  for dirpath, dirnames, filenames in os.walk(path):
    dirnames[:]=[d for d in dirnames if d not in excluded_subdirs]
    for filename in filenames:
      if not os.path.splitext(filename)[1].lower() in admitted_extensions: continue
      if verbose_mode:
        sys.stdout.write(
          os.path.relpath(os.path.join(dirpath,filename),boost_root_libs)+"\n")
      add_dependencies_file(os.path.join(dirpath,filename))

target_module=args.module
if not target_module in modules:
  sys.stderr.write("Can't find module "+target_module+"\n")
  exit(1)  

if verbose_mode: sys.stdout.write("Scanning dependencies...\n")
add_dependencies_dir(os.path.join(include_path[target_module]))
add_dependencies_dir(os.path.join(src_path[target_module]))
dependencies.discard(target_module)
if verbose_mode: sys.stdout.write("Dependencies for module "+target_module+":\n")
for module in sorted(dependencies): sys.stdout.write(module+"\n")
os.remove(wave_out_filename)
os.remove(wave_cfg_filename)

