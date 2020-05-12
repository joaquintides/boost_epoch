# Proposal for an epoch-based organization of Boost libraries
## Introduction
## Definitions
* Boost _epochs_ are named according to the release year of C++ standard revisions: **Boost03**, **Boost11**, ... , **Boost20**, etc.
* A Boost library _belongs_ to one or more epochs according to rules defined below.
* Local installations of Boost are constrained by the minimum (oldest) epoch allowed, as decided by the user. This is signaled by a global-level preprocessor symbol `BOOST_MIN_EPOCH`. Boost libraries that do not belong to some epoch **BoostN** with **N** ≥ `BOOST_MIN_EPOCH` are not allowed into the installation.
* A Boost library **X** _depends on_ another Boost library **Y** _for epoch_ **BoostN** if **X** depends on **Y** when `BOOST_MIN_EPOCH` is set to **N**. The set of dependencies of **X** for epoch **BoostN** is denoted by depN(**X**).
* A Boost library **X** _belongs_ to epoch **BoostN**, denoted **X** ∈ **BoostN**,  if:
  * **X** is compatible with C++**N**,
  * **(rejection rule 1)** the functionality provided by **X** is not already covered by C++**N**,
  * **(rejection rule 2)** the functionality provided by **X** is not superseded by some other, more modern, library **Y** in the epoch,
  * depN(**X**) ⊆ **BoostN**.
* Under reasonable assumptions, the epochs a given library belongs in form a contiguous interval from some **BoostN** to some **BoostM** with **M** ≥ **N** . We denote the minimum and maximum epochs comprising **X** by begin(**X**) and end(**X**), respectively. We define span(**X**) as (begin(**X**), end(**X**)). 

### Examples
* span(**Boost.Array**) = span(**Boost.Function**) = span(**Boost.Tuple**) = (**Boost03**, **Boost03**), as all of these librares have been superseded by equivalent components in C++11 (rejection rule 1)
* span(**Boost.Optional**) = (**Boost03**, **Boost14**)
* span(**Boost.Mp11**) = (**Boost11**, **Boost20**)
* span(**Boost.MPL**) = (**Boost03**, **Boost03**) (superseded by **Boost.Mp11** in C++11, rejection rule 2)
* span (**Boost.Parameter**) = (**Boost03**, **Boost14**), as it depends on **Boost.Optional**, no longer part of **Boost17**.
