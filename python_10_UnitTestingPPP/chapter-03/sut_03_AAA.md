# AAA

AAA stands for <font color="blue">arrange</font>, <font color="blue">act</font>, <font color="blue">assert</font> process of a unit test.

wait a sec, why AAA pattern?

as the definition of a good unit test indicates, it tests a unit of behavior.

imaging how u evaluate people or things in real life,

if some phynomina is triggered, people react or things happen,
u assert some conclusion.

to absract it, isn't it the pattern of AAA?

or analog like the following

- Given -- corresponds to the arrage section
- when  -- corresponds to the act section
- then  -- corresponds to the assert section

## how to implement?

- arrange section, u bring the SUT and its dependencies to a desir state
- act section, u call methods on the SUT, pass the prepared dependencies, and capture the output value(if any)
- assert section, u verify outcome. the outcome may be represented by the return value, the final state of the SUT and its collaborators, or the methods the SUT called on those collaborators.
