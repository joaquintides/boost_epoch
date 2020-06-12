# Illustrative Boost 1.73 epoch report, lax mode

This is an example of a Boost epoch assignment report using the lax-mode epoch membership rules.
Compared with its [strict counterpart](epoch_report), this allows more libraries into
higher epochs: to give just one example, [**Boost.QVM**](#qvm) belongs here in all epochs from
[**Boost03**](#boost03) to [**Boost20**](#boost20), whereas in strict mode it only belongs
in [**Boost03**](#boost03) due to its dependency from [**Boost.Exception**](#exception).

## Boost epochs

### Boost03

[`accumulators`](#accumulators), [`algorithm`](#algorithm), [`align`](#align), [`any`](#any), [`array`](#array), [`asio`](#asio), [`assert`](#assert), [`assign`](#assign), [`atomic`](#atomic), [`bimap`](#bimap), [`bind`](#bind), [`callable_traits`](#callable_traits), [`chrono`](#chrono), [`circular_buffer`](#circular_buffer), [`compatibility`](#compatibility), [`compute`](#compute), [`concept_check`](#concept_check), [`config`](#config), [`container`](#container), [`container_hash`](#container_hash), [`conversion`](#conversion), [`convert`](#convert), [`core`](#core), [`coroutine`](#coroutine), [`crc`](#crc), [`date_time`](#date_time), [`detail`](#detail), [`dll`](#dll), [`dynamic_bitset`](#dynamic_bitset), [`endian`](#endian), [`exception`](#exception), [`filesystem`](#filesystem), [`flyweight`](#flyweight), [`foreach`](#foreach), [`format`](#format), [`function`](#function), [`function_types`](#function_types), [`functional`](#functional), [`fusion`](#fusion), [`geometry`](#geometry), [`graph`](#graph), [`graph_parallel`](#graph_parallel), [`heap`](#heap), [`icl`](#icl), [`integer`](#integer), [`interprocess`](#interprocess), [`intrusive`](#intrusive), [`io`](#io), [`iostreams`](#iostreams), [`iterator`](#iterator), [`lambda`](#lambda), [`lexical_cast`](#lexical_cast), [`local_function`](#local_function), [`locale`](#locale), [`lockfree`](#lockfree), [`log`](#log), [`logic`](#logic), [`math`](#math), [`metaparse`](#metaparse), [`move`](#move), [`mpi`](#mpi), [`mpl`](#mpl), [`msm`](#msm), [`multi_array`](#multi_array), [`multi_index`](#multi_index), [`multiprecision`](#multiprecision), [`nowide`](#nowide), [`numeric/conversion`](#numericconversion), [`numeric/interval`](#numericinterval), [`numeric/odeint`](#numericodeint), [`numeric/ublas`](#numericublas), [`optional`](#optional), [`parameter`](#parameter), [`parameter_python`](#parameter_python), [`phoenix`](#phoenix), [`polygon`](#polygon), [`pool`](#pool), [`predef`](#predef), [`preprocessor`](#preprocessor), [`program_options`](#program_options), [`property_map`](#property_map), [`property_tree`](#property_tree), [`proto`](#proto), [`ptr_container`](#ptr_container), [`python`](#python), [`qvm`](#qvm), [`random`](#random), [`range`](#range), [`ratio`](#ratio), [`rational`](#rational), [`regex`](#regex), [`scope_exit`](#scope_exit), [`serialization`](#serialization), [`signals2`](#signals2), [`smart_ptr`](#smart_ptr), [`sort`](#sort), [`spirit`](#spirit), [`stacktrace`](#stacktrace), [`statechart`](#statechart), [`static_assert`](#static_assert), [`system`](#system), [`test`](#test), [`thread`](#thread), [`throw_exception`](#throw_exception), [`timer`](#timer), [`tokenizer`](#tokenizer), [`tti`](#tti), [`tuple`](#tuple), [`type_erasure`](#type_erasure), [`type_index`](#type_index), [`type_traits`](#type_traits), [`typeof`](#typeof), [`units`](#units), [`unordered`](#unordered), [`utility`](#utility), [`uuid`](#uuid), [`variant`](#variant), [`wave`](#wave), [`winapi`](#winapi), [`xpressive`](#xpressive)

### Boost11

[`align`](#align), [`any`](#any), [`assert`](#assert), [`atomic`](#atomic), [`callable_traits`](#callable_traits), [`circular_buffer`](#circular_buffer), [`compatibility`](#compatibility), [`concept_check`](#concept_check), [`config`](#config), [`container`](#container), [`container_hash`](#container_hash), [`core`](#core), [`detail`](#detail), [`dynamic_bitset`](#dynamic_bitset), [`endian`](#endian), [`hof`](#hof), [`integer`](#integer), [`intrusive`](#intrusive), [`io`](#io), [`logic`](#logic), [`move`](#move), [`mp11`](#mp11), [`numeric/interval`](#numericinterval), [`optional`](#optional), [`polygon`](#polygon), [`pool`](#pool), [`predef`](#predef), [`preprocessor`](#preprocessor), [`qvm`](#qvm), [`rational`](#rational), [`static_assert`](#static_assert), [`static_string`](#static_string), [`system`](#system), [`throw_exception`](#throw_exception), [`type_traits`](#type_traits), [`typeof`](#typeof), [`utility`](#utility), [`variant2`](#variant2), [`vmd`](#vmd), [`winapi`](#winapi)

### Boost14

[`align`](#align), [`any`](#any), [`assert`](#assert), [`atomic`](#atomic), [`callable_traits`](#callable_traits), [`circular_buffer`](#circular_buffer), [`compatibility`](#compatibility), [`concept_check`](#concept_check), [`config`](#config), [`container`](#container), [`container_hash`](#container_hash), [`core`](#core), [`detail`](#detail), [`dynamic_bitset`](#dynamic_bitset), [`endian`](#endian), [`hof`](#hof), [`integer`](#integer), [`intrusive`](#intrusive), [`io`](#io), [`logic`](#logic), [`move`](#move), [`mp11`](#mp11), [`numeric/interval`](#numericinterval), [`optional`](#optional), [`polygon`](#polygon), [`pool`](#pool), [`predef`](#predef), [`preprocessor`](#preprocessor), [`qvm`](#qvm), [`rational`](#rational), [`safe_numerics`](#safe_numerics), [`static_assert`](#static_assert), [`static_string`](#static_string), [`system`](#system), [`throw_exception`](#throw_exception), [`type_traits`](#type_traits), [`typeof`](#typeof), [`utility`](#utility), [`variant2`](#variant2), [`vmd`](#vmd), [`winapi`](#winapi), [`yap`](#yap)

### Boost17

[`align`](#align), [`assert`](#assert), [`atomic`](#atomic), [`callable_traits`](#callable_traits), [`circular_buffer`](#circular_buffer), [`compatibility`](#compatibility), [`concept_check`](#concept_check), [`config`](#config), [`container`](#container), [`container_hash`](#container_hash), [`core`](#core), [`detail`](#detail), [`dynamic_bitset`](#dynamic_bitset), [`endian`](#endian), [`hof`](#hof), [`integer`](#integer), [`intrusive`](#intrusive), [`io`](#io), [`logic`](#logic), [`move`](#move), [`mp11`](#mp11), [`numeric/interval`](#numericinterval), [`polygon`](#polygon), [`pool`](#pool), [`predef`](#predef), [`preprocessor`](#preprocessor), [`qvm`](#qvm), [`rational`](#rational), [`safe_numerics`](#safe_numerics), [`static_assert`](#static_assert), [`static_string`](#static_string), [`system`](#system), [`throw_exception`](#throw_exception), [`type_traits`](#type_traits), [`typeof`](#typeof), [`utility`](#utility), [`variant2`](#variant2), [`vmd`](#vmd), [`winapi`](#winapi), [`yap`](#yap)

### Boost20

[`align`](#align), [`assert`](#assert), [`atomic`](#atomic), [`callable_traits`](#callable_traits), [`circular_buffer`](#circular_buffer), [`compatibility`](#compatibility), [`concept_check`](#concept_check), [`config`](#config), [`container`](#container), [`container_hash`](#container_hash), [`core`](#core), [`detail`](#detail), [`dynamic_bitset`](#dynamic_bitset), [`endian`](#endian), [`hof`](#hof), [`integer`](#integer), [`intrusive`](#intrusive), [`io`](#io), [`logic`](#logic), [`move`](#move), [`mp11`](#mp11), [`numeric/interval`](#numericinterval), [`polygon`](#polygon), [`pool`](#pool), [`predef`](#predef), [`preprocessor`](#preprocessor), [`qvm`](#qvm), [`rational`](#rational), [`safe_numerics`](#safe_numerics), [`static_assert`](#static_assert), [`static_string`](#static_string), [`system`](#system), [`throw_exception`](#throw_exception), [`type_traits`](#type_traits), [`typeof`](#typeof), [`utility`](#utility), [`variant2`](#variant2), [`vmd`](#vmd), [`winapi`](#winapi), [`yap`](#yap)

## Boost modules

### `accumulators`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `algorithm`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `align`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `any`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14)  
**Why not in Boost17:**  
Subsumed by `std::any`  

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
Depends on [`bind`](#bind), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

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
Depends on [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

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
Depends on [`bind`](#bind), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

### `bimap`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`lambda`](#lambda), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

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
Depends on [`mpl`](#mpl)  

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
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

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
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`thread`](#thread)  

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
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

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
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`tuple`](#tuple)  

### `coroutine2`

**Requires:**  
C++11 or later  
**Epochs:**  
None  
**Why not in Boost11:**  
Depends on [`smart_ptr`](#smart_ptr)  

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
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

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
Depends on [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

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
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

### `filesystem`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

### `flyweight`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `foreach`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl)  

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
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl)  

### `fusion`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl), [`tuple`](#tuple)  

### `geometry`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`tuple`](#tuple)  

### `gil`

**Requires:**  
C++11 or later  
**Epochs:**  
None  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl)  

### `graph`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `graph_parallel`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `hana`

**Requires:**  
C++14 or later  
**Epochs:**  
None  
**Why not in Boost14:**  
Depends on [`mpl`](#mpl), [`tuple`](#tuple)  

### `heap`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`mpl`](#mpl)  

### `histogram`

**Requires:**  
C++14 or later  
**Epochs:**  
None  
**Why not in Boost14:**  
Depends on [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

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
Depends on [`array`](#array), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

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
Depends on [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

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
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

### `iterator`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `lambda`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Subsumed by C+11 lambda expressions  

### `lexical_cast`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`mpl`](#mpl)  

### `local_function`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl)  

### `locale`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`tuple`](#tuple)  

### `lockfree`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`mpl`](#mpl), [`tuple`](#tuple)  

### `log`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`tuple`](#tuple)  

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
Depends on [`array`](#array), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

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
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

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
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`tuple`](#tuple)  

### `multi_array`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`mpl`](#mpl)  

### `multi_index`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`mpl`](#mpl), [`tuple`](#tuple)  

### `multiprecision`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

### `nowide`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl)  

### `numeric/conversion`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl)  

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
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `numeric/ublas`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

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
Depends on [`smart_ptr`](#smart_ptr)  

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
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `phoenix`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

### `poly_collection`

**Requires:**  
C++11 or later  
**Epochs:**  
None  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

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
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

### `program_options`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

### `property_map`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `property_tree`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `proto`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl)  

### `ptr_container`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `python`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `qvm`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03), [`Boost11`](#boost11), [`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

### `random`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`mpl`](#mpl)  

### `range`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

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
Depends on [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

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
Depends on [`bind`](#bind), [`function`](#function)  

### `serialization`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`tuple`](#tuple)  

### `signals2`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

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
Depends on [`mpl`](#mpl)  

### `spirit`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`tuple`](#tuple)  

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
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`thread`](#thread)  

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
Depends on [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

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
Depends on [`mpl`](#mpl)  

### `tokenizer`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl)  

### `tti`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl)  

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
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`tuple`](#tuple)  

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
Depends on [`bind`](#bind), [`lambda`](#lambda), [`mpl`](#mpl), [`tuple`](#tuple)  

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
Depends on [`mpl`](#mpl)  

### `variant`

**Requires:**  
C++03 or later  
**Epochs:**  
[`Boost03`](#boost03)  
**Why not in Boost11:**  
Depends on [`mpl`](#mpl)  

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
Depends on [`array`](#array), [`bind`](#bind), [`function`](#function), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr), [`thread`](#thread), [`tuple`](#tuple)  

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
Depends on [`array`](#array), [`mpl`](#mpl), [`smart_ptr`](#smart_ptr)  

### `yap`

**Requires:**  
C++14 or later  
**Epochs:**  
[`Boost14`](#boost14), [`Boost17`](#boost17), [`Boost20`](#boost20)  

