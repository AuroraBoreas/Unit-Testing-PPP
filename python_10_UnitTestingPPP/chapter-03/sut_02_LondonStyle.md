# London style of unittesting

the london school's approach provides the following benefits:

- better granularity
- it's easier to unit test a larger graph of interconnnected classes
- if a test fails, u know for sure which functionality has failed

## TIP

test shouldn't verify units of code.
rather, they should verify units of behavior: something that is meaningful for the problem domain and, ideally, something that a business person can recognize as useful.

the number of classes it takes to implement such a unit of behavior is irrelevant.

the unit could span across multiple classes or only one class,
or even take up just a tiny method.

```
as long as the test checks a signle unit of behavior, 
it's a good test.
```

## "cohesive story"

```
a test should tell a story about the problem your code helps to solve, and this story should be cohesive and meaningful to a non-programmer.
```

for instance, this is an example of a cohesive story

```
when i call my dog, my dog comes right to me
```

vs

now compare it to the following:

```
when i call my dog, he moves his front left leg first,
then the front right leg, his head turns, the tail start wagging...
```

a <font color="blue">good</font> unit test is a test that

- verify a single unit of behavior
- does it quickly
- does it in isolation from other tests

## unit test vs interaction test vs integration test

Table: unittest vs interactive test vs integratino test

| test               | explanaton                |
|--------------------|---------------------------|
| unit test          | test unit of behavior     |
| interaction test   | test interaction behavior |
| integration test   | test integration behavior |