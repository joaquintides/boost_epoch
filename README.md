# Proposal for an epoch-based organization of Boost libraries

## Contents

* [Introduction](#introduction)
* [Goals](#goals)
* [Definitions](#definitions)
* [How does the scheme work](#how-does-the-scheme-work)
* [Feedback](#feedback)

## Introduction

The recent ["Why you don't use Boost"](https://www.reddit.com/r/cpp/comments/gfowpq/why_you_dont_use_boost/) Reddit thread showed some level of discomfort with the current status of the Boost project. From the plethora of information (and noise), we want to distill the following issues (which do not cover the entirety of the discussion):

* Much stuff in Boost is now useless as it was adopted into the C++ standard itself.
* There is an unacceptably high level of internal dependencies among libraries ("pulling one library drags most of Boost in").
* Very high compilation times (partly attributable to internal dependencies).

We propose an epoch-based mechanism that can potentially alleviate these problems in a sensible, non-disruptive manner.

## Goals

This proposal tries to balance a number of antagonistic forces in the process:

* Provide a mechanism for users to know the degree to which each Boost library is catching up with the C++ standard and select those that meet their modernity requirements.
* Incentivize Boost authors to embrace newer versions of the C++ standard and get rid of internal dependencies while offering an optional path to backwards compatibility and respecting their absolute sovereignty over the libraries they maintain.
* Promote a general Boost trend towards leaner, less entangled and more modern libraries. When starting anew, Boost made crucial contributions to the evolution of C++03 to C++11: we want to regain this role as C++20 progresses towards C++23 and beyond.

## Definitions

* Boost _epochs_ are named according to the release year of C++ standard revisions: **Boost03**, **Boost11**, ... , **Boost20**, etc.
* A Boost library _belongs_ to one or more epochs according to rules defined below.
* Users indicate the miminum version of the C++ standard supported by their project by setting a global level preprocessor symbol `BOOST_ASSUME_CXX`, with possible values 03 (the default), 11, 14, etc.
* A Boost library **X** _depends on_ another Boost library **Y** _for epoch_ **BoostN** if **X** depends on **Y** when `BOOST_ASSUME_CXX` is set to **N**. Transitive dependencies are taken into account. The set of dependencies of **X** for epoch **BoostN** is denoted by depN(**X**).
* A Boost library **X** _belongs_ to epoch **BoostN** if:
  * **X** is compatible with C++**N**,
  * **(rejection rule 1)** the functionality provided by **X** is not already covered by C++**N**,
  * **(rejection rule 2)** the functionality provided by **X** is not superseded by some other, more modern, library **Y** in **BoostN**,
  * all the libraries in depN(**X**) belong to **BoostN**.
* Under reasonable assumptions, the epochs a given library belongs in form a contiguous interval from some **BoostN** to some **BoostM** with **N** ≤ **M** . We denote the minimum and maximum epochs comprising **X** by begin(**X**) and end(**X**), respectively. We define span(**X**) as (begin(**X**), end(**X**)).

From these definitions, it follows that each epoch **BoostN** is a self-contained set without internal dependencies to other Boost libraries outside the epoch.

### Examples

* span(**Boost.Array**) = span(**Boost.Function**) = span(**Boost.Tuple**) = (**Boost03**, **Boost03**), as all of these librares have been superseded by equivalent components in C++11 (rejection rule 1)
* span(**Boost.Optional**) = (**Boost03**, **Boost14**)
* span(**Boost.Mp11**) = (**Boost11**, **Boost20**)
* span(**Boost.MPL**) = (**Boost03**, **Boost03**) (superseded by **Boost.Mp11** in C++11, rejection rule 2)
* span (**Boost.Parameter**) = (**Boost03**, **Boost14**), as it depends on **Boost.Optional**, no longer part of **Boost17**

## How does the scheme work

### For users

* Users can modulate the amount of "legacy" stuff they don't want to depend on by setting `BOOST_ASSUME_CXX` to a value of their choice, presumably to match their C++ baseline version.
* Settling on a minimum Boost epoch means that *pre-epoch* libs (those whose maximum epoch does not reach the threshold) won't be internally used and can be safely omitted from the local installation.
* On the other hand, pre-epoch libraries can be explicitly used by users if they so decide. In case a corporate or project-specific ban exists on older Boost epochs, users are expected to press the Boost authors to modernize those libraries of their interest.

### For Boost authors

* Authors retain full control over their libraries. If left untouched, a library will continue to belong in epoch **Boost03** for ever.
* But now there is a social incentive to extend the epoch span of a library **X**. This can be done in basically two ways, according to how conservative the author is with respect to backwards compatibility:
  * Replacement of internal dependencies with C++ native equivalents: increases _both_ begin(**X**) and end(**X**).
  * Conditional inclusion of internal dependencies or native equivalents based on `BOOST_ASSUME_CXX`: keeps begin(**X**) and increases end(**X**).
* `BOOST_ASSUME_CXX`-conditional inclusion is likely to improve compilation times in more recent epochs, as whole legacy headers (and their dependencies) will just not be processed. This adds yet another incentive for modernization even in the case of conservative authors who do not wish to break backwards compatiblity.
* In the case of abandoned libraries, the Boost Community Maintenance Team can take on `BOOST_ASSUME_CXX`-conditional modernization as this looks like a moderately straigthforward procedure.

### For Boost management

* The determination of the span of a library is automatic (and can be automated), except for the two rejection rules (superseded by C++**N**, superseded by a newer Boost library), which must be decided by a human. This can be controversial as authors may fight "deprecation" back (a typical argument would run that the native equivalent does not cover 100% of the superseded library). For this reason, it seems advisable that epoch rejection be governed by some central authority like the Boost Steering Committee.
* Epochs pose additional constraints to acceptance of new Boost libraries. For instance, a candidate library requiring C++11 and using **Boost.Tuple** cannot be accepted, as its resulting epoch span would be void. This guarantees certain level of "modernity" right from the start of a library's lifetime.
* Similarly, an analysis of _existing_ Boost libraries could reveal that some of them have a void epoch span. What to do about those is an open matter.
* Epoch enforcement does not prevent authors from proposing libraries that significantly improve on the functionality of a particular C++ component or Boost library (determination of whether the improvement is actually significant is governed by epoch rejection rules). We already have two examples of this, namely **Boost.Mp11** and **Boost.Variant2**.

### Tooling

#### bcp

In order to use bcp for automatic epoch determination, this dependency extraction utility should be updated so as to detect `BOOST_ASSUME_CXX`-conditional header inclusions.

#### B2

B2 should be made `BOOST_ASSUME_CXX` aware. Note that binary redistributables depend on `BOOST_ASSUME_CXX`.

#### Package managers

Boost does not feature its own package manager, but some external tools (vg. vcpkg) do have a notion of internal dependencies between Boost libraries. It remains to be studied how epoch management can be fitted here.

## Feedback

Please do share your comments on this proposal through the Boost mailing lists, the Boost Slack channel or by directly submitting issues here. The document will be updated as the conversation around it goes on.
