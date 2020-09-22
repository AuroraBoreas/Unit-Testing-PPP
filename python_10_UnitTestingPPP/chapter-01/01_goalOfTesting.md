# overview

chapter 01, The goal of unit testing

learning unit testing doesn't stop at mastering the technical bits of it, such as your favorite framework, mocking library, and so on.

there's much more to unit testing than the act of writing tests.

you always have to strive to achieve the best return on the time you invest in unit testing, minimizing the effort you put into tests and maximizing the benefits they provide. achieving both things isn't an easy task.

## goal

the learning doesn't end with the basics.

there's a next level: 
not just writing tests, but doing unit testing in a way 
that  provides you with the best return on your efforts

when you reach this point, most books pretty much leave you
to your own devices to figure out how to get that next level.

Sustainability and scalability are the keys.
they allow you to maintain development speed in the long run.

NOT all tests are created equal.

the cost component is determined by the amount of time spent on various activities.

- refactoring the test when you refactor the underlying code
- running the test on each code change
- dealing with false alarms raised by the test
- spending time reading the test when u trying to understand how the underlying code behaves

it's easy to create tests whose net value is close to zero or even is negative due to high maintenance costs.

to enable sustainable project growth, you have to exclusively focus on high-quality tests -- those are the only type of tests that are worth keeping in the test suite.


## good or bad tests?

using "coverage metric" to measure.

a coverage metric shows how much source code a test suite executes, from none to 100%

```
code coverage(or test coverage) = lines of code executed / total number of lines

branch coverage = branches traversed / total number of branches
```
### problems

- YOU CAN'T GUARANTEE THAT THE TEST VERIFIES ALL THE POSSIBLE OUTCOMES.

- NO COVERAGE METRIC CAN TAKE INTO ACCOUNT CODE PATHS IN EXTERNAL LIBRARIES

the best way to view a coverage metric is as an indicator, not a goal in and of itself.

```
coverage metrics are a good negative indicator, 
but a bad positive one.
```

### TIP

It’s good to have a high level of coverage in core parts of your system.

It’s bad to make this high level a requirement. The difference is subtle but critical.

## what makes a successful test suite?

@ What about a proper way?

@ How should you measure your test suite’s quality?

```
the only reliable way is to evaluate each test in the suite individually, one by one.
```

### It's integrated into the development cycle

The only point in having automated tests is if you constantly use them. All tests should
be integrated into the development cycle. Ideally, you should execute them on every
code change, even the smallest one.

## target

it targets only the most important parts of your code base.

```
just as all tests are NOT created equal, 
NOT all parts of your code base are worth the same attention in terms of unit testing.
```

it's important to direct your unit testing efforts to the most critical parts of the system
and verify the others only briefly or indirectly. 

in most application, the most important part is the part that <font color="blue">contains business logic -- the domain model.</font>

testing business logic gives you the best return on your time investment.

all other parts can be divided into three categories.

- infrastructure code
- external services and dependencies, such as the database and third-party systems
- code that glues everything together

## a test double, originated from "a stunt double" (特技替身演员)

a test double is an object that looks and ehaves like its release-intended counterpart
but is actually a simplified version that reduces the complexity and facilittates testing.

this term was introduced by Gerard Meszaros in his book, xUnit Test Patterns: Refactoring Test Code.

the name itself comes from the notion of a stunt double in movies.

### MUT

a method under test (MUT) is a method in the SUT called by the test.
the terms MUT and SUT are often used as synonyms, but normally, MUT refers to a method
while SUT refers to the whole class.

### MOCK

A mock is a special kind of test double that allows you to examine
interactions between the system under test and its collaborators

### isolation problem

Instead, unit tests themselves should be run in isolation from each other. 
That way, you can run the tests in parallel, sequentially, and in any order,
whatever fits you best, and they still won’t affect each other’s outcome.

isolation tests from each other means it's fine to exercise several classes at once
as long as they all reside in the memmory and don't reach out to a shared state,
thru which the tests can communicate and affect each other's execution context.


## shared, private and out-of-process dependencies

dependency principles, "cohesion". read more for OOD, @uncle Bob

### shared dependency

a shared dependency is a dependency that is shared btwn tests 
and provides means for those tests to affect each other's outcome.

a typical example of shared dependency is a static mutable field.
a change to such a field is visible across all unit tests running with the same process.
a database is another typical example of a shared dependency.

### private dependency

a private dependency is a dependency that is NOT shared

### out-of-process dependency

an out-of-process dependency is a dependency that runs outside the application's execution process;
it's a proxy to data that is NOT yet in the memory.

an out-of-process dependency corresponds to a shared dependency in the vast majority of cases, but not always.

for example, a database is both out-of-process and shared.
but if u launch that database in a Docker container before each test run,
that would make this dependency out-of-process but not shared,
since tests no longer work with the same instance of it.

similarly, a read-only database is also out-of-process but not shared, even if it's reused by tests.

tests can't mutate data in such a database and thus can't affect each other's outcome.

#### concept: in-process vs out-of-process?

link: docs.embarcadero.com

it's all about where dependency resides..

Table: in-process vs out-of-process vs remote

| concept           | explanation                                                                         |
|-------------------|-------------------------------------------------------------------------------------|
| in-process        | a library(DLL) running in the same process space as the client                      |
| out-of-process    | another app(EXE) running in a different space but on the same machine as the client |
| remote            | a DLL or app running on a different machine from that of the client.                |