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

P38