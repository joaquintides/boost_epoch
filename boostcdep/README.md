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
