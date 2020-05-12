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
* span (**Boost.Parameter**) = (**Boost03**, **Boost14**), as it depends on **Boost.Optional**, no longer part of **Boost17**

## How does the scheme work
### For users
* Users can modulate the amount of "legacy" stuff they are willing to tolerate by setting `BOOST_MIN_EPOCH` to a value of their choice, presumably to match their C++ baseline version.
* Settling on a minimum Boost epoch means that fundamental libraries already covered natively by C++ will not polute the workspace, but also bans "old" libraries that have not evolved/adapted to get rid of these dependencies.
* When a particular library is sought for that does not reach a mininimum epoch, users can either lower their `BOOST_MIN_EPOCH` or press the associated Boost author to modernize the library.

### For Boost authors
* Authors retain full control over their libraries. If left untouched, a library will continue to belong in epoch **Boost03** for ever.
* But now there is a social incentive to extend the epoch span of a library **X**. This can be done in basically two ways, according to how conservative the author is with respect to backwards compatibility:
  * Replacement of internal dependencies with C++ native equivalents: increases _both_ begin(**X**) and end(**X**).
  * Conditional inclusion of internal dependencies or native equivalents based on `BOOST_MIN_EPOCH`: keeps begin(**X**) and increases end(**X**).
* `BOOST_MIN_EPOCH`-conditional inclusion is likely to improve compilation times in more recent epochs, as whole legacy headers (and their dependencies) will just not be processed. This adds yet another incentive for modernization even in the case of conservative authors who do not wish to break backward compatiblity.
* In the case of abandoned libraries,the Boost Community Maintenance Team can take on `BOOST_MIN_EPOCH`-conditional modernization as this looks like a moderately straigthforward procedure.

### For Boost management
* The determination of the span of a library is automatic (and can be automated), except for the two rejection rules (superseded by C++**N**, superseded by a newer Boost library), which must be decided by a human. This can be controversial as authors may fight "deprecation" back (a typical argument would run that the native equivalent does not cover 100% of the superseded library). For this reason, it seems advisable that epoch rejection be governed by some central authority like the Boost Steering Committee.
* Epochs pose additional constraints to acceptance of new Boost libraries. For instance, a candidate library requiring C++11 and using **Boost.Tuple** cannot be accepted, as its resulting epoch span would be void. This guarantees certain level of "modernity" right from the start of a library's lifetime.
* Similary, an analysis of _existing_ Boost libraries could reveal that some of them have a void epoch span. What to do about those is an open matter.
* Epoch enforcement does not prevent authors from proposing libraries that significantly improve on the functionality of a particular C++ component or Boost library (determination of whether the improvement is actually significant is governed by epoch rejection rules). We already have two examples of this, namely **Boost.Mp11** and **Boost.Variant2**.
