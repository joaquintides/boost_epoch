# Boost 1.73 legacy report

We have run a simulation to determine which Boost libraries would potentially
be promoted to epoch **Boost11**. The simulation uses a [dependency check utility](legacy_check.py)
based on [Boostdep](https://www.boost.org/tools/boostdep/doc/html/index.html) that detects
those libraries dependent on any of the following "legacy" modules:
`array`, `bind`, `function`, `lambda`, `mpl`, `smart_ptr`, `thread`, `tuple`. Libraries without
dependencies to these are deemed eligible for promotion to **Boost11**. Disclaimer: this is merely
a simulation and it is debatable which exact foundational libraries are really to be rejected for
**Boost11**.

In the table below each cell shows the amount of code (measured as the sum of file sizes in `include`
and `src` directories) each component adds to the total dependencies of the analyzed library.
The last column is the sum of all previous contributions: so, "0%" means that the library does not
have legacy dependencies and it therefore belongs to **Boost11**. Percentages are rounded up to unit.

Out of 138 Boost libraries analyzed, 43 (31%) go to **Boost11**. The biggest offender in terms of
library blocking and added source code overhead is **Boost.MPL**.

|                  |array|bind|function|lambda|mpl|smart_ptr|thread|tuple|legacy|
|------------------|:---:|:--:|:------:|:----:|:-:|:-------:|:----:|:---:|-----:|
|accumulators      |  1% | 1% |   1%   |      |14%|    2%   |      |  1% |   16%|
|algorithm         |  1% | 2% |   1%   |      |26%|    3%   |      |  1% |   30%|
|align             |     |    |        |      |   |         |      |     |    0%|
|any               |     |    |        |      |   |         |      |     |    0%|
|array             |  3% |    |        |      |   |         |      |     |    3%|
|asio              |  1% | 2% |   1%   |      |24%|    2%   |      |     |   27%|
|assert            |     |    |        |      |   |         |      |     |    0%|
|assign            |  1% |    |        |      |33%|    3%   |      |  1% |   36%|
|atomic            |     |    |        |      |   |         |      |     |    0%|
|beast             |  1% | 2% |   1%   |      |20%|    2%   |      |     |   23%|
|bimap             |     | 2% |   1%   |  4%  |32%|    3%   |      |  1% |   40%|
|bind              |     |30% |        |      |   |         |      |     |   30%|
|callable_traits   |     |    |        |      |   |         |      |     |    0%|
|chrono            |     |    |        |      |29%|         |      |     |   29%|
|circular_buffer   |     |    |        |      |   |         |      |     |    0%|
|compatibility     |     |    |        |      |   |         |      |     |    0%|
|compute           |  1% | 1% |   1%   |      | 9%|    1%   |  3%  |  1% |   13%|
|concept_check     |     |    |        |      |   |         |      |     |    0%|
|config            |     |    |        |      |   |         |      |     |    0%|
|container         |     |    |        |      |   |         |      |     |    0%|
|container_hash    |     |    |        |      |   |         |      |     |    0%|
|context           |     |    |        |      |   |   11%   |      |     |   11%|
|contract          |     | 2% |   1%   |      |23%|    2%   |  7%  |     |   33%|
|conversion        |     |    |        |      |   |    4%   |      |     |    4%|
|convert           |  1% | 1% |   1%   |      | 7%|    1%   |      |     |    8%|
|core              |     |    |        |      |   |         |      |     |    0%|
|coroutine         |     |    |        |      |36%|    3%   |      |     |   39%|
|coroutine2        |     |    |        |      |   |   11%   |      |     |   11%|
|crc               |  1% |    |        |      |   |         |      |     |    1%|
|date_time         |  1% | 1% |   1%   |      |19%|    2%   |      |     |   22%|
|detail            |     |    |        |      |   |         |      |     |    0%|
|dll               |     | 1% |   1%   |      |11%|    1%   |      |     |   13%|
|dynamic_bitset    |     |    |        |      |   |         |      |     |    0%|
|endian            |     |    |        |      |   |         |      |     |    0%|
|exception         |     |    |        |      |   |   18%   |      |  3% |   20%|
|fiber             |     |    |        |      |   |    7%   |      |     |    7%|
|filesystem        |     |    |        |      |43%|    4%   |      |     |   46%|
|flyweight         |     | 1% |   1%   |      |13%|    2%   |      |  1% |   15%|
|foreach           |     |    |        |      |46%|         |      |     |   46%|
|format            |     |    |        |      |   |    7%   |      |     |    7%|
|function          |     | 3% |   2%   |      |   |         |      |     |    4%|
|function_types    |     |    |        |      |47%|         |      |     |   47%|
|functional        |     | 2% |   1%   |      |30%|         |      |     |   32%|
|fusion            |     |    |        |      |16%|         |      |  1% |   16%|
|geometry          |  1% | 1% |   1%   |      | 8%|    1%   |  3%  |  1% |   11%|
|gil               |     |    |        |      |34%|         |      |     |   34%|
|graph             |  1% | 1% |   1%   |      | 7%|    1%   |  3%  |  1% |   11%|
|graph_parallel    |  1% | 1% |   1%   |      | 7%|    1%   |  3%  |  1% |   11%|
|hana              |     |    |        |      |18%|         |      |  1% |   18%|
|heap              |  1% | 1% |   1%   |      |16%|         |      |     |   18%|
|histogram         |     |    |        |      |40%|    4%   |      |     |   43%|
|hof               |     |    |        |      |   |         |      |     |    0%|
|icl               |  1% |    |        |      |18%|    2%   |      |     |   20%|
|integer           |     |    |        |      |   |         |      |     |    0%|
|interprocess      |     |    |        |      |25%|    3%   |      |  1% |   28%|
|intrusive         |     |    |        |      |   |         |      |     |    0%|
|io                |     |    |        |      |   |         |      |     |    0%|
|iostreams         |     | 2% |   1%   |      |32%|    3%   |      |     |   37%|
|iterator          |     |    |        |      |18%|    2%   |      |  1% |   19%|
|lambda            |     | 3% |        |  5%  |45%|         |      |  1% |   52%|
|lexical_cast      |  1% |    |        |      |22%|         |      |     |   22%|
|local_function    |     | 2% |   1%   |      |31%|         |      |     |   33%|
|locale            |     | 3% |   1%   |      |42%|    4%   |      |     |   48%|
|lockfree          |  1% | 1% |   1%   |      |17%|         |      |  1% |   19%|
|log               |  1% | 1% |   1%   |      | 6%|    1%   |  2%  |  1% |    9%|
|logic             |     |    |        |      |   |         |      |     |    0%|
|math              |  1% | 1% |        |  2%  |11%|    1%   |      |  1% |   14%|
|metaparse         |     |    |        |      |48%|         |      |     |   48%|
|move              |     |    |        |      |   |         |      |     |    0%|
|mp11              |     |    |        |      |   |         |      |     |    0%|
|mpi               |  1% | 1% |   1%   |      |17%|    2%   |      |  1% |   20%|
|mpl               |     |    |        |      |49%|         |      |     |   49%|
|msm               |     | 1% |   1%   |      | 9%|         |      |  1% |   10%|
|multi_array       |  1% |    |        |      |47%|         |      |     |   47%|
|multi_index       |     | 2% |        |      |37%|    3%   |      |  1% |   43%|
|multiprecision    |  1% |    |        |      |10%|    1%   |      |  1% |   11%|
|nowide            |     |    |        |      |42%|    4%   |      |     |   45%|
|numeric/conversion|     |    |        |      |51%|         |      |     |   51%|
|numeric/interval  |     |    |        |      |   |         |      |     |    0%|
|numeric/odeint    |  1% | 1% |   1%   |      | 9%|    1%   |  3%  |  1% |   12%|
|numeric/ublas     |  1% | 1% |   1%   |      | 9%|    1%   |  3%  |  1% |   13%|
|optional          |     |    |        |      |   |         |      |     |    0%|
|outcome           |     |    |        |      |   |   11%   |      |     |   11%|
|parameter         |     | 1% |   1%   |      |18%|         |      |     |   19%|
|parameter_python  |     | 2% |   1%   |      |35%|    3%   |      |  1% |   41%|
|phoenix           |     | 1% |   1%   |      | 9%|    1%   |      |     |   11%|
|poly_collection   |     |    |        |      |29%|    3%   |      |     |   31%|
|polygon           |     |    |        |      |   |         |      |     |    0%|
|pool              |     |    |        |      |   |         |      |     |    0%|
|predef            |     |    |        |      |   |         |      |     |    0%|
|preprocessor      |     |    |        |      |   |         |      |     |    0%|
|process           |     | 1% |   1%   |      |14%|    2%   |      |     |   16%|
|program_options   |  1% | 2% |   1%   |      |21%|    2%   |      |     |   24%|
|property_map      |  1% | 1% |   1%   |      |19%|    2%   |      |  1% |   22%|
|property_tree     |     | 2% |        |      |33%|    3%   |      |  1% |   38%|
|proto             |     |    |        |      |15%|         |      |     |   15%|
|ptr_container     |  1% |    |        |      |27%|    3%   |      |  1% |   29%|
|python            |  1% | 2% |   1%   |      |20%|    2%   |      |  1% |   24%|
|qvm               |     |    |        |      |   |         |      |     |    0%|
|random            |  1% |    |        |      |19%|         |      |     |   19%|
|range             |  1% |    |        |      |17%|    2%   |      |  1% |   18%|
|ratio             |     |    |        |      |48%|         |      |     |   48%|
|rational          |     |    |        |      |   |         |      |     |    0%|
|regex             |     |    |        |      |41%|    4%   |      |     |   44%|
|safe_numerics     |     |    |        |      |   |         |      |     |    0%|
|scope_exit        |     | 3% |   2%   |      |   |         |      |     |    4%|
|serialization     |  1% |    |        |      |21%|    2%   |      |  1% |   23%|
|signals2          |     | 1% |   1%   |      |17%|    2%   |      |  1% |   20%|
|smart_ptr         |     |    |        |      |   |   15%   |      |     |   15%|
|sort              |     |    |        |      |41%|         |      |     |   41%|
|spirit            |  1% | 1% |   1%   |      | 6%|    1%   |  2%  |  1% |    9%|
|stacktrace        |  1% |    |        |      |   |         |      |     |    1%|
|statechart        |     | 2% |   1%   |      |32%|    3%   | 10%  |     |   46%|
|static_assert     |     |    |        |      |   |         |      |     |    0%|
|static_string     |     |    |        |      |   |         |      |     |    0%|
|system            |     |    |        |      |   |         |      |     |    0%|
|test              |     | 2% |   1%   |      |34%|    3%   |      |     |   39%|
|thread            |     | 2% |   1%   |      |24%|    2%   |  8%  |  1% |   35%|
|throw_exception   |     |    |        |      |   |         |      |     |    0%|
|timer             |     |    |        |      |   |         |      |     |    0%|
|tokenizer         |     |    |        |      |49%|         |      |     |   49%|
|tti               |     |    |        |      |46%|         |      |     |   46%|
|tuple             |     |    |        |      |   |         |      |  4% |    4%|
|type_erasure      |     |    |        |      |15%|    2%   |      |     |   16%|
|type_index        |     |    |        |      |   |    8%   |      |     |    8%|
|type_traits       |     |    |        |      |   |         |      |     |    0%|
|typeof            |     |    |        |      |   |         |      |     |    0%|
|units             |     | 1% |        |  2%  |19%|         |      |  1% |   22%|
|unordered         |     |    |        |      |   |    4%   |      |  1% |    5%|
|utility           |     |    |        |      |   |         |      |     |    0%|
|uuid              |     |    |        |      |34%|         |      |     |   34%|
|variant           |     | 3% |        |      |44%|         |      |     |   46%|
|variant2          |     |    |        |      |   |         |      |     |    0%|
|vmd               |     |    |        |      |   |         |      |     |    0%|
|wave              |  1% | 1% |        |      |13%|    2%   |  4%  |  1% |   19%|
|winapi            |     |    |        |      |   |         |      |     |    0%|
|xpressive         |  1% |    |        |      |11%|    1%   |      |     |   11%|
|yap               |     |    |        |      |   |         |      |     |    0%|
