# Illustrative Boost 1.73 epoch report

We have used [a utility](epoch_report/epoch_report.py) that automatically generates
an epoch assignment report based on these two inputs:
* [`boostcdmap.1.73.0.json`](epoch_report/boostcdmap.1.73.0.json): a conditional
dependency map for Boost generated with [`boostcdmap`](https://github.com/joaquintides/boostcdmap).
* [`boostepochban.1.73.0.json`](epoch_report/boostepochban.1.73.0.json): a JSON file
specifying which Boost libraries are explicitly rejected for epoch progression due to
their being subsumed by the C++ standard or more modern alternatives in Boost. Please note
that the rejections contained in this example file are in no way official and can be
debated; you can run the report generation utility using your own rejection file to see how
results differ.

From the core rejections contained in [`boostepochban.1.73.0.json`](epoch_report/boostepochban.1.73.0.json),
the utility derives the rest of epoch assignments following the purely formal rules
[described in the proposal](README.md#definitions).

See also the [lax-mode version](lax_epoch_report.md) of the report.

## Boost epochs

### Boost03

[`accumulators`](#accumulators), [`algorithm`](#algorithm), [`align`](#align), [`any`](#any), [`array`](#array), [`asio`](#asio), [`assert`](#assert), [`assign`](#assign), [`atomic`](#atomic), [`bimap`](#bimap), [`bind`](#bind), [`callable_traits`](#callable_traits), [`chrono`](#chrono), [`circular_buffer`](#circular_buffer), [`compatibility`](#compatibility), [`compute`](#compute), [`concept_check`](#concept_check), [`config`](#config), [`container`](#container), [`container_hash`](#container_hash), [`conversion`](#conversion), [`convert`](#convert), [`core`](#core), [`coroutine`](#coroutine), [`crc`](#crc), [`date_time`](#date_time), [`detail`](#detail), [`dll`](#dll), [`dynamic_bitset`](#dynamic_bitset), [`endian`](#endian), [`exception`](#exception), [`filesystem`](#filesystem), [`flyweight`](#flyweight), [`foreach`](#foreach), [`format`](#format), [`function`](#function), [`function_types`](#function_types), [`functional`](#functional), [`fusion`](#fusion), [`geometry`](#geometry), [`graph`](#graph), [`graph_parallel`](#graph_parallel), [`heap`](#heap), [`icl`](#icl), [`integer`](#integer), [`interprocess`](#interprocess), [`intrusive`](#intrusive), [`io`](#io), [`iostreams`](#iostreams), [`iterator`](#iterator), [`lambda`](#lambda), [`lexical_cast`](#lexical_cast), [`local_function`](#local_function), [`locale`](#locale), [`lockfree`](#lockfree), [`log`](#log), [`logic`](#logic), [`math`](#math), [`metaparse`](#metaparse), [`move`](#move), [`mpi`](#mpi), [`mpl`](#mpl), [`msm`](#msm), [`multi_array`](#multi_array), [`multi_index`](#multi_index), [`multiprecision`](#multiprecision), [`nowide`](#nowide), [`numeric/conversion`](#numericconversion), [`numeric/interval`](#numericinterval), [`numeric/odeint`](#numericodeint), [`numeric/ublas`](#numericublas), [`optional`](#optional), [`parameter`](#parameter), [`parameter_python`](#parameter_python), [`phoenix`](#phoenix), [`polygon`](#polygon), [`pool`](#pool), [`predef`](#predef), [`preprocessor`](#preprocessor), [`program_options`](#program_options), [`property_map`](#property_map), [`property_tree`](#property_tree), [`proto`](#proto), [`ptr_container`](#ptr_container), [`python`](#python), [`qvm`](#qvm), [`random`](#random), [`range`](#range), [`ratio`](#ratio), [`rational`](#rational), [`regex`](#regex), [`scope_exit`](#scope_exit), [`serialization`](#serialization), [`signals2`](#signals2), [`smart_ptr`](#smart_ptr), [`sort`](#sort), [`spirit`](#spirit), [`stacktrace`](#stacktrace), [`statechart`](#statechart), [`static_assert`](#static_assert), [`system`](#system), [`test`](#test), [`thread`](#thread), [`throw_exception`](#throw_exception), [`timer`](#timer), [`tokenizer`](#tokenizer), [`tti`](#tti), [`tuple`](#tuple), [`type_erasure`](#type_erasure), [`type_index`](#type_index), [`type_traits`](#type_traits), [`typeof`](#typeof), [`units`](#units), [`unordered`](#unordered), [`utility`](#utility), [`uuid`](#uuid), [`variant`](#variant), [`wave`](#wave), [`winapi`](#winapi), [`xpressive`](#xpressive)

### Boost11

[`align`](#align), [`assert`](#assert), [`atomic`](#atomic), [`callable_traits`](#callable_traits), [`circular_buffer`](#circular_buffer), [`compatibility`](#compatibility), [`concept_check`](#concept_check), [`config`](#config), [`container`](#container), [`container_hash`](#container_hash), [`core`](#core), [`detail`](#detail), [`dynamic_bitset`](#dynamic_bitset), [`endian`](#endian), [`hof`](#hof), [`integer`](#integer), [`intrusive`](#intrusive), [`io`](#io), [`logic`](#logic), [`move`](#move), [`mp11`](#mp11), [`numeric/interval`](#numericinterval), [`optional`](#optional), [`polygon`](#polygon), [`pool`](#pool), [`predef`](#predef), [`preprocessor`](#preprocessor), [`rational`](#rational), [`static_assert`](#static_assert), [`static_string`](#static_string), [`system`](#system), [`throw_exception`](#throw_exception), [`type_traits`](#type_traits), [`typeof`](#typeof), [`utility`](#utility), [`variant2`](#variant2), [`vmd`](#vmd), [`winapi`](#winapi)

### Boost14

[`align`](#align), [`assert`](#assert), [`atomic`](#atomic), [`callable_traits`](#callable_traits), [`circular_buffer`](#circular_buffer), [`compatibility`](#compatibility), [`concept_check`](#concept_check), [`config`](#config), [`container`](#container), [`container_hash`](#container_hash), [`core`](#core), [`detail`](#detail), [`dynamic_bitset`](#dynamic_bitset), [`endian`](#endian), [`hof`](#hof), [`integer`](#integer), [`intrusive`](#intrusive), [`io`](#io), [`logic`](#logic), [`move`](#move), [`mp11`](#mp11), [`numeric/interval`](#numericinterval), [`optional`](#optional), [`polygon`](#polygon), [`pool`](#pool), [`predef`](#predef), [`preprocessor`](#preprocessor), [`rational`](#rational), [`safe_numerics`](#safe_numerics), [`static_assert`](#static_assert), [`static_string`](#static_string), [`system`](#system), [`throw_exception`](#throw_exception), [`type_traits`](#type_traits), [`typeof`](#typeof), [`utility`](#utility), [`variant2`](#variant2), [`vmd`](#vmd), [`winapi`](#winapi)

### Boost17

[`align`](#align), [`assert`](#assert), [`atomic`](#atomic), [`callable_traits`](#callable_traits), [`circular_buffer`](#circular_buffer), [`compatibility`](#compatibility), [`concept_check`](#concept_check), [`config`](#config), [`container`](#container), [`container_hash`](#container_hash), [`core`](#core), [`detail`](#detail), [`dynamic_bitset`](#dynamic_bitset), [`endian`](#endian), [`hof`](#hof), [`integer`](#integer), [`intrusive`](#intrusive), [`io`](#io), [`logic`](#logic), [`move`](#move), [`mp11`](#mp11), [`numeric/interval`](#numericinterval), [`polygon`](#polygon), [`pool`](#pool), [`predef`](#predef), [`preprocessor`](#preprocessor), [`rational`](#rational), [`safe_numerics`](#safe_numerics), [`static_assert`](#static_assert), [`static_string`](#static_string), [`system`](#system), [`throw_exception`](#throw_exception), [`type_traits`](#type_traits), [`typeof`](#typeof), [`utility`](#utility), [`variant2`](#variant2), [`vmd`](#vmd), [`winapi`](#winapi)

### Boost20

[`align`](#align), [`assert`](#assert), [`atomic`](#atomic), [`callable_traits`](#callable_traits), [`circular_buffer`](#circular_buffer), [`compatibility`](#compatibility), [`concept_check`](#concept_check), [`config`](#config), [`container`](#container), [`container_hash`](#container_hash), [`core`](#core), [`detail`](#detail), [`dynamic_bitset`](#dynamic_bitset), [`endian`](#endian), [`hof`](#hof), [`integer`](#integer), [`intrusive`](#intrusive), [`io`](#io), [`logic`](#logic), [`move`](#move), [`mp11`](#mp11), [`numeric/interval`](#numericinterval), [`polygon`](#polygon), [`pool`](#pool), [`predef`](#predef), [`preprocessor`](#preprocessor), [`rational`](#rational), [`safe_numerics`](#safe_numerics), [`static_assert`](#static_assert), [`static_string`](#static_string), [`system`](#system), [`throw_exception`](#throw_exception), [`type_traits`](#type_traits), [`typeof`](#typeof), [`utility`](#utility), [`variant2`](#variant2), [`vmd`](#vmd), [`winapi`](#winapi)

## Boost modules

### `accumulators`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`fusion`](#fusion), [`iterator`](#iterator), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`numeric/ublas`](#numericublas), [`parameter`](#parameter), [`range`](#range), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `algorithm`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`exception`](#exception), [`function`](#function), [`iterator`](#iterator), [`mpl`](#mpl), [`range`](#range), [`regex`](#regex), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple), [`type_index`](#type_index)  

### `align`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `any`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`type_index`](#type_index)  

### `array`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Subsumed by `std::array`  

### `asio`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`context`](#context), [`coroutine`](#coroutine), [`date_time`](#date_time), [`exception`](#exception), [`iterator`](#iterator), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`range`](#range), [`regex`](#regex), [`smart_ptr`](#smart_ptr)  

### `assert`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `assign`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`iterator`](#iterator), [`mpl`](#mpl), [`ptr_container`](#ptr_container), [`range`](#range), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `atomic`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `beast`

**Requires:**  
C++11 or later  
**Epochs:**  
None  
**Why not in Boost11:**  
Depends on [`asio`](#asio), [`bind`](#bind), [`date_time`](#date_time), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`smart_ptr`](#smart_ptr)  

### `bimap`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`foreach`](#foreach), [`iterator`](#iterator), [`lambda`](#lambda), [`mpl`](#mpl), [`multi_index`](#multi_index), [`property_map`](#property_map), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `bind`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Subsumed by `std::bind`  

### `callable_traits`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `chrono`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl), [`ratio`](#ratio)  

### `circular_buffer`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `compatibility`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `compute`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`array`](#array), [`bind`](#bind), [`chrono`](#chrono), [`function`](#function), [`function_types`](#function_types), [`fusion`](#fusion), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`proto`](#proto), [`range`](#range), [`ratio`](#ratio), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple), [`type_index`](#type_index), [`uuid`](#uuid)  

### `concept_check`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `config`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `container`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `container_hash`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `context`

**Requires:**  
C++11 or later  
**Epochs:**  
None  
**Why not in Boost11:**  
Depends on [`smart_ptr`](#smart_ptr)  

### `contract`

**Requires:**  
C++11 or later  
**Epochs:**  
None  
**Why not in Boost11:**  
Depends on [`any`](#any), [`bind`](#bind), [`chrono`](#chrono), [`date_time`](#date_time), [`exception`](#exception), [`function`](#function), [`function_types`](#function_types), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`ratio`](#ratio), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`type_index`](#type_index)  

### `conversion`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`smart_ptr`](#smart_ptr)  

### `convert`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`foreach`](#foreach), [`function`](#function), [`function_types`](#function_types), [`fusion`](#fusion), [`iostreams`](#iostreams), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`parameter`](#parameter), [`phoenix`](#phoenix), [`proto`](#proto), [`range`](#range), [`regex`](#regex), [`smart_ptr`](#smart_ptr), [`spirit`](#spirit), [`type_index`](#type_index), [`variant`](#variant)  

### `core`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `coroutine`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`array`](#array), [`bind`](#bind), [`chrono`](#chrono), [`context`](#context), [`date_time`](#date_time), [`exception`](#exception), [`function`](#function), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`range`](#range), [`ratio`](#ratio), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`tuple`](#tuple), [`type_index`](#type_index)  

### `coroutine2`

**Requires:**  
C++11 or later  
**Epochs:**  
None  
**Why not in Boost11:**  
Depends on [`context`](#context), [`smart_ptr`](#smart_ptr)  

### `crc`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array)  

### `date_time`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`array`](#array), [`bind`](#bind), [`function`](#function), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`range`](#range), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`tokenizer`](#tokenizer), [`type_index`](#type_index)  

### `detail`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `dll`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`filesystem`](#filesystem), [`iterator`](#iterator), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`type_index`](#type_index)  

### `dynamic_bitset`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `endian`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `exception`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `fiber`

**Requires:**  
C++11 or later  
**Epochs:**  
None  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`bind`](#bind), [`context`](#context), [`filesystem`](#filesystem), [`format`](#format), [`function`](#function), [`iterator`](#iterator), [`mpl`](#mpl), [`range`](#range), [`smart_ptr`](#smart_ptr), [`type_index`](#type_index)  

### `filesystem`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`iterator`](#iterator), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

### `flyweight`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`date_time`](#date_time), [`foreach`](#foreach), [`interprocess`](#interprocess), [`iterator`](#iterator), [`mpl`](#mpl), [`multi_index`](#multi_index), [`numeric/conversion`](#numericconversion), [`parameter`](#parameter), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `foreach`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`iterator`](#iterator), [`mpl`](#mpl), [`range`](#range)  

### `format`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`smart_ptr`](#smart_ptr)  

### `function`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Subsumed by `std::function`  

### `function_types`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl)  

### `functional`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`function`](#function), [`function_types`](#function_types), [`mpl`](#mpl), [`type_index`](#type_index)  

### `fusion`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`function_types`](#function_types), [`mpl`](#mpl), [`tuple`](#tuple)  

### `geometry`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`array`](#array), [`bind`](#bind), [`chrono`](#chrono), [`date_time`](#date_time), [`exception`](#exception), [`function`](#function), [`function_types`](#function_types), [`fusion`](#fusion), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`qvm`](#qvm), [`range`](#range), [`ratio`](#ratio), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`tokenizer`](#tokenizer), [`tuple`](#tuple), [`type_index`](#type_index), [`variant`](#variant)  

### `gil`

**Requires:**  
C++11 or later  
**Epochs:**  
None  
**Why not in Boost11:**  
Depends on [`iterator`](#iterator), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`type_index`](#type_index), [`variant`](#variant)  

### `graph`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`any`](#any), [`array`](#array), [`bimap`](#bimap), [`bind`](#bind), [`conversion`](#conversion), [`exception`](#exception), [`foreach`](#foreach), [`function`](#function), [`function_types`](#function_types), [`fusion`](#fusion), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`multi_index`](#multi_index), [`numeric/conversion`](#numericconversion), [`parameter`](#parameter), [`property_map`](#property_map), [`property_tree`](#property_tree), [`proto`](#proto), [`random`](#random), [`range`](#range), [`regex`](#regex), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`spirit`](#spirit), [`tti`](#tti), [`tuple`](#tuple), [`type_index`](#type_index), [`unordered`](#unordered), [`xpressive`](#xpressive)  

### `graph_parallel`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`any`](#any), [`array`](#array), [`bind`](#bind), [`conversion`](#conversion), [`exception`](#exception), [`filesystem`](#filesystem), [`foreach`](#foreach), [`function`](#function), [`function_types`](#function_types), [`fusion`](#fusion), [`graph`](#graph), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpi`](#mpi), [`mpl`](#mpl), [`multi_index`](#multi_index), [`numeric/conversion`](#numericconversion), [`parameter`](#parameter), [`property_map`](#property_map), [`property_tree`](#property_tree), [`proto`](#proto), [`python`](#python), [`random`](#random), [`range`](#range), [`regex`](#regex), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`spirit`](#spirit), [`tti`](#tti), [`tuple`](#tuple), [`type_index`](#type_index), [`unordered`](#unordered), [`variant`](#variant), [`xpressive`](#xpressive)  

### `hana`

**Requires:**  
C++14 or later  
**Epochs:**  
None  
**Why not in Boost14:**  
Depends on [`fusion`](#fusion), [`mpl`](#mpl), [`tuple`](#tuple)  

### `heap`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`iterator`](#iterator), [`mpl`](#mpl), [`parameter`](#parameter)  

### `histogram`

**Requires:**  
C++14 or later  
**Epochs:**  
None  
**Why not in Boost14:**  
Depends on [`mpl`](#mpl), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr)  

### `hof`

**Requires:**  
C++11 or later  
**Epochs:**  
[`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `icl`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`array`](#array), [`date_time`](#date_time), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`range`](#range), [`smart_ptr`](#smart_ptr), [`tokenizer`](#tokenizer)  

### `integer`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `interprocess`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`date_time`](#date_time), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple), [`unordered`](#unordered)  

### `intrusive`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `io`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `iostreams`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`function`](#function), [`iterator`](#iterator), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`random`](#random), [`range`](#range), [`regex`](#regex), [`smart_ptr`](#smart_ptr), [`type_index`](#type_index)  

### `iterator`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`conversion`](#conversion), [`function_types`](#function_types), [`fusion`](#fusion), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `lambda`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Subsumed by C++11 lambda expressions  

### `lexical_cast`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`iterator`](#iterator), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`range`](#range)  

### `local_function`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`scope_exit`](#scope_exit), [`type_index`](#type_index)  

### `locale`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`array`](#array), [`bind`](#bind), [`chrono`](#chrono), [`date_time`](#date_time), [`exception`](#exception), [`function`](#function), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`range`](#range), [`ratio`](#ratio), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`tuple`](#tuple), [`type_index`](#type_index), [`unordered`](#unordered)  

### `lockfree`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`iterator`](#iterator), [`mpl`](#mpl), [`parameter`](#parameter), [`tuple`](#tuple)  

### `log`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`any`](#any), [`array`](#array), [`asio`](#asio), [`bind`](#bind), [`chrono`](#chrono), [`conversion`](#conversion), [`date_time`](#date_time), [`exception`](#exception), [`filesystem`](#filesystem), [`foreach`](#foreach), [`function`](#function), [`function_types`](#function_types), [`fusion`](#fusion), [`interprocess`](#interprocess), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`locale`](#locale), [`math`](#math), [`mpl`](#mpl), [`multi_index`](#multi_index), [`numeric/conversion`](#numericconversion), [`parameter`](#parameter), [`phoenix`](#phoenix), [`property_tree`](#property_tree), [`proto`](#proto), [`random`](#random), [`range`](#range), [`ratio`](#ratio), [`regex`](#regex), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`spirit`](#spirit), [`thread`](#thread), [`tokenizer`](#tokenizer), [`tuple`](#tuple), [`type_index`](#type_index), [`unordered`](#unordered), [`variant`](#variant), [`xpressive`](#xpressive)  

### `logic`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `math`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`range`](#range), [`smart_ptr`](#smart_ptr)  

### `metaparse`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl)  

### `move`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `mp11`

**Requires:**  
C++11 or later  
**Epochs:**  
[`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `mpi`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`any`](#any), [`array`](#array), [`bind`](#bind), [`conversion`](#conversion), [`exception`](#exception), [`foreach`](#foreach), [`function`](#function), [`fusion`](#fusion), [`graph`](#graph), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`multi_index`](#multi_index), [`numeric/conversion`](#numericconversion), [`parameter`](#parameter), [`property_map`](#property_map), [`property_tree`](#property_tree), [`proto`](#proto), [`python`](#python), [`range`](#range), [`regex`](#regex), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`spirit`](#spirit), [`tuple`](#tuple), [`type_index`](#type_index), [`unordered`](#unordered), [`xpressive`](#xpressive)  

### `mpl`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Subsumed by [`mp11`](#mp11)  

### `msm`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`any`](#any), [`bind`](#bind), [`function`](#function), [`fusion`](#fusion), [`mpl`](#mpl), [`parameter`](#parameter), [`phoenix`](#phoenix), [`proto`](#proto), [`serialization`](#serialization), [`tuple`](#tuple), [`type_index`](#type_index)  

### `multi_array`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`functional`](#functional), [`iterator`](#iterator), [`mpl`](#mpl)  

### `multi_index`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`foreach`](#foreach), [`iterator`](#iterator), [`mpl`](#mpl), [`serialization`](#serialization), [`tuple`](#tuple)  

### `multiprecision`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`random`](#random), [`range`](#range), [`smart_ptr`](#smart_ptr)  

### `nowide`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`filesystem`](#filesystem), [`iterator`](#iterator), [`mpl`](#mpl)  

### `numeric/conversion`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`conversion`](#conversion), [`mpl`](#mpl)  

### `numeric/interval`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `numeric/odeint`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`array`](#array), [`bind`](#bind), [`chrono`](#chrono), [`compute`](#compute), [`function`](#function), [`function_types`](#function_types), [`functional`](#functional), [`fusion`](#fusion), [`graph`](#graph), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpi`](#mpi), [`mpl`](#mpl), [`multi_array`](#multi_array), [`numeric/conversion`](#numericconversion), [`numeric/ublas`](#numericublas), [`property_map`](#property_map), [`proto`](#proto), [`range`](#range), [`ratio`](#ratio), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple), [`type_index`](#type_index), [`units`](#units), [`uuid`](#uuid)  

### `numeric/ublas`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`array`](#array), [`bind`](#bind), [`chrono`](#chrono), [`compute`](#compute), [`function`](#function), [`function_types`](#function_types), [`fusion`](#fusion), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`proto`](#proto), [`range`](#range), [`ratio`](#ratio), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple), [`type_index`](#type_index), [`uuid`](#uuid)  

### `optional`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14)  
**Why not in Boost17:**  
Subsumed by `std::optional`  

### `outcome`

**Requires:**  
C++14 or later  
**Epochs:**  
None  
**Why not in Boost14:**  
Depends on [`exception`](#exception), [`smart_ptr`](#smart_ptr)  

### `parameter`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl)  

### `parameter_python`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`conversion`](#conversion), [`function`](#function), [`iterator`](#iterator), [`mpl`](#mpl), [`parameter`](#parameter), [`python`](#python), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple), [`type_index`](#type_index)  

### `phoenix`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`function`](#function), [`fusion`](#fusion), [`iterator`](#iterator), [`mpl`](#mpl), [`proto`](#proto), [`range`](#range), [`smart_ptr`](#smart_ptr), [`type_index`](#type_index)  

### `poly_collection`

**Requires:**  
C++11 or later  
**Epochs:**  
None  
**Why not in Boost11:**  
Depends on [`iterator`](#iterator), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`type_erasure`](#type_erasure)  

### `polygon`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `pool`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `predef`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `preprocessor`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `process`

**Requires:**  
C++11 or later  
**Epochs:**  
None  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`asio`](#asio), [`bind`](#bind), [`filesystem`](#filesystem), [`function`](#function), [`fusion`](#fusion), [`iterator`](#iterator), [`mpl`](#mpl), [`range`](#range), [`smart_ptr`](#smart_ptr), [`tokenizer`](#tokenizer), [`type_index`](#type_index)  

### `program_options`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`any`](#any), [`array`](#array), [`bind`](#bind), [`function`](#function), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`range`](#range), [`smart_ptr`](#smart_ptr), [`tokenizer`](#tokenizer), [`type_index`](#type_index)  

### `property_map`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`any`](#any), [`array`](#array), [`bind`](#bind), [`foreach`](#foreach), [`function`](#function), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpi`](#mpi), [`mpl`](#mpl), [`multi_index`](#multi_index), [`numeric/conversion`](#numericconversion), [`range`](#range), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple), [`type_index`](#type_index)  

### `property_tree`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`any`](#any), [`bind`](#bind), [`foreach`](#foreach), [`format`](#format), [`iterator`](#iterator), [`mpl`](#mpl), [`multi_index`](#multi_index), [`range`](#range), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple), [`type_index`](#type_index)  

### `proto`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`fusion`](#fusion), [`iterator`](#iterator), [`mpl`](#mpl), [`range`](#range)  

### `ptr_container`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`iterator`](#iterator), [`mpl`](#mpl), [`range`](#range), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple), [`unordered`](#unordered)  

### `python`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`any`](#any), [`array`](#array), [`bind`](#bind), [`conversion`](#conversion), [`exception`](#exception), [`foreach`](#foreach), [`function`](#function), [`fusion`](#fusion), [`graph`](#graph), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`multi_index`](#multi_index), [`numeric/conversion`](#numericconversion), [`parameter`](#parameter), [`property_map`](#property_map), [`property_tree`](#property_tree), [`proto`](#proto), [`range`](#range), [`regex`](#regex), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`spirit`](#spirit), [`tuple`](#tuple), [`type_index`](#type_index), [`unordered`](#unordered), [`xpressive`](#xpressive)  

### `qvm`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`exception`](#exception)  

### `random`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`multiprecision`](#multiprecision), [`numeric/conversion`](#numericconversion), [`range`](#range)  

### `range`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`conversion`](#conversion), [`fusion`](#fusion), [`iterator`](#iterator), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`regex`](#regex), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `ratio`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl)  

### `rational`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `regex`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`iterator`](#iterator), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

### `safe_numerics`

**Requires:**  
C++14 or later  
**Epochs:**  
[`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `scope_exit`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`function`](#function), [`type_index`](#type_index)  

### `serialization`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`iterator`](#iterator), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`spirit`](#spirit), [`tuple`](#tuple), [`type_index`](#type_index), [`unordered`](#unordered), [`variant`](#variant)  

### `signals2`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`function`](#function), [`iterator`](#iterator), [`mpl`](#mpl), [`parameter`](#parameter), [`smart_ptr`](#smart_ptr), [`type_index`](#type_index), [`variant`](#variant)  

### `smart_ptr`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Subsumed by C++11 smart pointer facilities  

### `sort`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`iterator`](#iterator), [`mpl`](#mpl), [`range`](#range), [`serialization`](#serialization)  

### `spirit`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`chrono`](#chrono), [`date_time`](#date_time), [`filesystem`](#filesystem), [`foreach`](#foreach), [`function`](#function), [`function_types`](#function_types), [`fusion`](#fusion), [`iostreams`](#iostreams), [`iterator`](#iterator), [`locale`](#locale), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`phoenix`](#phoenix), [`proto`](#proto), [`range`](#range), [`ratio`](#ratio), [`regex`](#regex), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`tuple`](#tuple), [`type_index`](#type_index), [`unordered`](#unordered), [`variant`](#variant)  

### `stacktrace`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array)  

### `statechart`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`chrono`](#chrono), [`conversion`](#conversion), [`date_time`](#date_time), [`function`](#function), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`ratio`](#ratio), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`type_index`](#type_index)  

### `static_assert`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `static_string`

**Requires:**  
C++11 or later  
**Epochs:**  
[`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `system`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `test`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`bind`](#bind), [`exception`](#exception), [`function`](#function), [`iterator`](#iterator), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`range`](#range), [`smart_ptr`](#smart_ptr), [`type_index`](#type_index)  

### `thread`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Subsumed by `std::thread`  

### `throw_exception`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `timer`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`chrono`](#chrono), [`mpl`](#mpl), [`ratio`](#ratio)  

### `tokenizer`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`iterator`](#iterator), [`mpl`](#mpl)  

### `tti`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`function_types`](#function_types), [`mpl`](#mpl)  

### `tuple`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Subsumed by `std::tuple`  

### `type_erasure`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`array`](#array), [`bind`](#bind), [`chrono`](#chrono), [`date_time`](#date_time), [`exception`](#exception), [`function`](#function), [`fusion`](#fusion), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`range`](#range), [`ratio`](#ratio), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`tuple`](#tuple), [`type_index`](#type_index)  

### `type_index`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`smart_ptr`](#smart_ptr)  

### `type_traits`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `typeof`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `units`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`iterator`](#iterator), [`lambda`](#lambda), [`math`](#math), [`mpl`](#mpl), [`serialization`](#serialization), [`tuple`](#tuple)  

### `unordered`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`tuple`](#tuple)  

### `utility`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `uuid`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`conversion`](#conversion), [`function_types`](#function_types), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`random`](#random), [`serialization`](#serialization), [`tti`](#tti)  

### `variant`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl), [`type_index`](#type_index)  

### `variant2`

**Requires:**  
C++11 or later  
**Epochs:**  
[`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `vmd`

**Requires:**  
C++11 or later  
**Epochs:**  
[`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `wave`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`algorithm`](#algorithm), [`array`](#array), [`bind`](#bind), [`chrono`](#chrono), [`date_time`](#date_time), [`exception`](#exception), [`filesystem`](#filesystem), [`foreach`](#foreach), [`function`](#function), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`multi_index`](#multi_index), [`numeric/conversion`](#numericconversion), [`range`](#range), [`ratio`](#ratio), [`serialization`](#serialization), [`smart_ptr`](#smart_ptr), [`spirit`](#spirit), [`thread`](#thread), [`tuple`](#tuple), [`type_index`](#type_index)  

### `winapi`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `xpressive`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`conversion`](#conversion), [`exception`](#exception), [`function_types`](#function_types), [`fusion`](#fusion), [`iterator`](#iterator), [`lexical_cast`](#lexical_cast), [`math`](#math), [`mpl`](#mpl), [`numeric/conversion`](#numericconversion), [`proto`](#proto), [`range`](#range), [`smart_ptr`](#smart_ptr)  

### `yap`

**Requires:**  
C++14 or later  
**Epochs:**  
None  
**Why not in Boost14:**  
Depends on [`hana`](#hana), [`type_index`](#type_index)  

