# boostcdep

`boostcdep` calculates the internal dependencies of Boost modules in a given environment.
For instance, the default dependencies of **Boost.StaticString** in Clang 10 with `-std=c++17`
are (output reformatted for conciseness):
```
> boostcdep.py cclang-linux-10~c++17.txt static_string
assert config container_hash core detail integer io
static_assert throw_exception type_traits utility
```
Whereas if `BOOST_STATIC_STRING_STANDALONE` is defined there are no internal dependencies:
```
> boostcdep.py cclang-linux-10~c++17.txt -DBOOST_STATIC_STRING_STANDALONE static_string
>
```
As another example, these are the dependencies of **Boost.DLL** in GCC 4.6 with `-std=c++98`:
```
> boostcdep.py -cgcc-4.6~c++98.txt dll
assert bind config container_hash core detail filesystem function
integer io iterator move mpl predef preprocessor smart_ptr
static_assert system throw_exception type_index type_traits
```
And these when using Clang 10 with `-std=c++17`:
```
> boostcdep.py -cclang-linux-10~c++17.txt dll
assert config container_hash core detail filesystem
integer io iterator move mpl predef preprocessor smart_ptr
static_assert system throw_exception type_index type_traits
```
Note that **Boost.Bind** and **Boost.Function** do not appear now
because their `std` counterparts are used instead in this environment.

`boostcdep` is a Python script that internally uses
[Boost.Wave driver](https://www.boost.org/libs/wave/doc/wave_driver.html) command-line tool.

## Usage
```
usage: boostcdep.py [-h] [-b <path-to-boost>] -c <config-file> [-D <pp-symbol>] [-v] <module>
positional arguments:
  <module>              Boost module name
optional arguments:
  -h, --help            show this help message and exit
  -b <path-to-boost>,
  --boost-root <path-to-boost>
                        path to Boost (default uses BOOST_ROOT environment variable)
  -c <config-file>,
  --config-info <config-file>
                        path to config info file
  -D <pp-symbol>        predefined preprocessor symbol (can be used multiple times)
  -v, --verbose         verbose mode
```
**&lt;module&gt;**

Name of the Boost module to be inspected.

**-b \[--boost-root \] &lt;path-to-boost&gt;**

Path to an installation of modular Boost. If this option is not provided, the program
uses the environment variable `BOOST_ROOT`. It is not necessary that the installation
has its headers collected under a common `boost` subdir via `b2 headers`. 

**-c \[--config-info \] &lt;config-file&gt;**

Path to a file containing the output of Boost.Config [`config_info`](https://github.com/boostorg/config/blob/develop/test/config_info.cpp)
test program for the selected environment. For instance, if one wishes to calculate dependencies
for MSVC 14.1, it merely takes to go to the associated
[regression test page](https://www.boost.org/development/tests/develop/developer/output/teeks99-09-p-64onAMD64-boost-bin-v2-libs-config-test-config_info-test-msvc-14-1-dbg-adrs-mdl-64-lnk-sttc-rntm-lnk-sttc.html) and copy
that entirely to a local text file.

**-D &lt;pp-symbol&gt;**

Predefined preprocessor symbol, either as  `-DSYMBOL` or `-DSYMBOL=VALUE`.
This command option can be repeated to define multiple symbols.
