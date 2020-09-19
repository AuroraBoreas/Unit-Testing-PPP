"""
? But did I improve the test suite with this refactoring? 
* Of course not.

The test still verifies the same number of possible outcomes.

This simple example shows how easy it is to game the coverage numbers. 
The more compact your code is, the better the test coverage metric becomes, 
because it only accounts for the raw line numbers. 

* At the same time, squashing more code into less space 
* doesn’t (and shouldn’t) change the value of the test suite or the maintainability of the underlying code base.

"""

def isStringLong(s: str) -> bool:
    # if len(s) > 5:
    #     return True
    # else:
    #     return False

    # return True if len(s) > 5 else False
    
    return len(s) > 5