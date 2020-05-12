# Proposal for an epoch-based organization of Boost libraries
## Introduction
## Definitions
* Boost _epochs_ are named according to the release year of C++ standard revisions: **Boost03**, **Boost11**, ... , **Boost20**, etc.
* A Boost library _belongs_ to one or more epochs according to rules defined below.
* Local installations of Boost are constrained by the minimum (oldest) epoch allowed, as decided by the user. This is signaled by a global-level preprocessor symbol `BOOST_MIN_EPOCH`. Boost libraries that do not belong to some epoch **BoostN** with **N** ≥ `BOOST_MIN_EPOCH` are not allowed into the installation.
* A Boost library **X** _depends on_ another Boost library **Y** _for epoch_ **BoostN** if **X** depends on **Y** when `BOOST_MIN_EPOCH` is set to **N**. The set of dependencies of **X** for epoch **BoostN** is denoted by depN(**X**).
* A Boost library **X** _belongs_ to epoch **BoostN**, denoted **X** ∈ **BoostN**,  if:
  * **X** is compatible with C++**N**,
  * the functionality provided by **X** is not already covered by C++**N** natively,
  * depN(**X**) ⊆ **BoostN**.
* Under reasonable assumptions, the epochs a given library belongs in form a contiguous interval from some **BoostN** to some **BoostM** with **M** ≥ **N** . We denote the minimum and maximum epochs comprising **X** by begin(**X**) and end(**X**), respectively. 
