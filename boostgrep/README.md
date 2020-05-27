# boostgrep

`boostgrep` is a small utilty for regex searching within the
Boost source code tree.

## Usage
```
usage: boostgrep.py [-h] [-b <path-to-boost>] [-v] [-f] <term> [<module>]
positional arguments:
  <term>                grepped term (regexp), strings outside pp directives
                        and comments are not considered
  <module>              restrict search to <module>
optional arguments:
  -h, --help            show this help message and exit
  -b <path-to-boost>, --boost-root <path-to-boost>
                        path to Boost (default uses BOOST_ROOT environment
                        variable)
  -v, --verbose         verbose mode
  -f, --first_only      show just the first match per module (in verbose mode)
```
**&lt;term&gt;**

Regular expression used in the search. Only the `include` and `src` subdirectories
of each module are inspected, and only header and source code files. Comments
and strings (except strings within a preprocessor directive, such as
`#include "foo.hpp"`) are not considered in the search.

**&lt;module&gt;**

Optional. If provided, resticts the search to this module alone.

**-b \[--boost-root \] &lt;path-to-boost&gt;**

Path to an installation of modular Boost. If this option is not provided, the program
uses the environment variable `BOOST_ROOT`. It is not necessary that the installation
has its headers collected under a common `boost` subdir via `b2 headers`. 

**-v \[--verbose\]**

When in verbose mode, matching lines are shown for each module. Otherwise, the
program just shows the name of the modules for which the search was successful. 

**-f \[--first_only\]**

If in verbose mode, this flag instructs the program to just show the first
matching line found in each module.
