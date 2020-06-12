# Boost epoch proposal: epoch report generator
#
# Copyright 2020 Joaquin M Lopez Munoz.
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)
#
# See https://github.com/joaquintides/boost_epoch/ for project home page.

import argparse
import json
import os
import sys

parser=argparse.ArgumentParser(
  description="Boost epoch report generator")
parser.add_argument(
  "cdmap_file",metavar="<cdmap-file>",
  help="path to JSON file with Boost conditional dependency map")
parser.add_argument(
  "ban_file",metavar="<ban-file>",
  help="path to JSON file with info on Boost libs explicitly banned for epoch progression")
args=parser.parse_args()

cdmap_file=args.cdmap_file
if not os.path.exists(cdmap_file):
  sys.stderr.write("Can't find "+cdmap_file+"\n")
  exit(1)
with open(cdmap_file,"r") as file: cdmap=json.load(file)

ban_file=args.ban_file
if not os.path.exists(ban_file):
  sys.stderr.write("Can't find "+ban_file+"\n")
  exit(1)
with open(ban_file,"r") as file: ban=json.load(file)

modules=sorted(cdmap.keys())
epochs={module:None for module in modules}
block=dict()
assessment_done={module:False for module in modules}

def markup(module): return "[`{}`](#{})".format(module,module.replace(" ","-"))

def assess_dependencies(module,epoch,cyclic_deps):
  for dep in sorted(set(cdmap[module][epoch])-cyclic_deps):
    assess(dep,cyclic_deps|{dep})
    if dep in block and block[dep]["epoch"]<=epoch:
      if not module in block:
        block[module]={"epoch":epoch,"reason":"Depends on {}".format(markup(dep))}
      else:
        block[module]["reason"]+=", {}".format(markup(dep))
  
def assess(module,cyclic_deps=set()):
  if not assessment_done[module]:
    epochs[module]=[]
    block.pop(module,None)
    for epoch in sorted(cdmap[module].keys()):
      if module in ban and ban[module]["epoch"]==epoch:
        block[module]=ban[module]
        break
      else:
        assess_dependencies(module,epoch,cyclic_deps|{module})
        if module in block: break
        epochs[module].append(epoch)
  if not cyclic_deps.intersection(
    set().union(*(set(deps) for deps in cdmap[module].values()))):
    assessment_done[module]=True

for module in modules: assess(module)

sys.stdout.write("## Boost modules\n\n")
for module in modules:
  sys.stdout.write("### `{}`\n\n".format(module))
  sys.stdout.write("**Requires:**  \nC++{} or later  \n".format(
    min(cdmap[module].keys())))
  sys.stdout.write("**Epochs:**  \n{}  \n".format(
    ", ".join("Boost{}".format(epoch) for epoch in epochs[module]) if epochs[module] else "None"))
  if module in block:
    sys.stdout.write("**Why not in Boost{}:**  \n{}  \n".format(
      block[module]["epoch"],block[module]["reason"]))
  sys.stdout.write("\n")
