# Internal relevance in post-C++03 Boost of Boost03 components vs. standard equivalents

Out of the 136 modules in Boost 1.73, 18 are for libraries that require C++11, or
in some cases higher, to work. We want to study how these libraries favor standard
components vs. their **Boost03** counterparts.

The table shows for each of these C++11-or-later Boost libraries their
*direct* dependencies on:

* **Boost03** components: `array`, `bind`, `function`, `lambda`, `mpl`,
`smart_ptr`, `thread`, `tuple`
* C++11/**Boost11** counterparts: `std::array`, `std::bind`, `std::function`,
`boost::mp11`, `std::shared_ptr`, `std::thread`, `std::tuple`.

Results have been obtained with a [script](boost_vs_std_internal.py)
that uses [Boostdep](https://www.boost.org/tools/boostdep/doc/html/index.html)
and [`boostgrep`](boostgrep).

It can be seen that (direct) usage of **Boost03** components is residual (and
in some cases due to backwards compatibility rather than for their functionality).
We can draw then the conclusion that newer Boost libraries are already dismissing
legacy dependencies when the standard environment offers alternatives.

|               |boost::array|boost::bind|boost::function|boost::lambda|boost::mpl|boost::smart_ptr|boost::thread|boost::tuple|std::array|std::bind|std::function|boost::mp11|std::shared_ptr|std::thread|std::tuple|
|---------------|:----------:|:---------:|:-------------:|:-----------:|:--------:|:--------------:|:-----------:|:----------:|:--------:|:-------:|:-----------:|:---------:|:-------------:|:---------:|:--------:|
|beast          |            |     X     |               |             |          |       X        |             |            |    X     |         |      X      |      X      |     X     |       X       |       X       |           |    X     |
|context        |            |           |               |             |          |       X        |             |            |          |    X    |      X      |      X      |           |               |               |           |    X     |
|contract       |            |           |       X       |             |    X     |       X        |      X      |            |          |         |             |             |           |               |               |           |    X     |
|coroutine2     |            |           |               |             |          |                |             |            |          |         |             |             |           |               |               |           |          |
|fiber          |            |           |               |             |          |       X        |             |            |          |    X    |             |             |           |               |               |     X     |    X     |
|gil            |            |           |               |             |          |                |             |            |    X     |    X    |      X      |      X      |     X     |       X       |       X       |           |          |
|hana           |            |           |               |             |    X     |                |             |     X      |    X     |         |             |             |           |               |               |           |    X     |
|histogram      |            |           |               |             |          |                |             |            |    X     |         |             |             |     X     |               |               |           |    X     |
|hof            |            |           |               |             |          |                |             |            |    X     |         |             |             |           |               |               |           |    X     |
|mp11           |            |           |               |             |          |                |             |            |          |         |             |             |     X     |               |               |           |    X     |
|outcome        |            |           |               |             |          |                |             |            |          |         |             |             |           |               |               |           |          |
|poly_collection|            |           |               |             |    X     |                |             |            |          |         |      X      |             |     X     |               |               |           |    X     |
|process        |            |           |               |             |          |                |             |            |    X     |         |      X      |             |           |       X       |       X       |           |    X     |
|safe_numerics  |            |           |               |             |          |                |             |            |          |         |             |             |     X     |               |               |           |          |
|static_string  |            |           |               |             |          |                |             |            |          |         |             |             |           |               |               |           |          |
|variant2       |            |           |               |             |          |                |             |            |          |         |             |             |     X     |               |               |           |          |
|vmd            |            |           |               |             |          |                |             |            |          |         |             |             |           |               |               |           |          |
|yap            |            |           |               |             |          |                |             |            |          |         |             |             |           |               |               |           |          |
