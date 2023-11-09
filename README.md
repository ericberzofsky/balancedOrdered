# balancedOrdered
Python script to solve an interview question asking to check if the provided string of braces is both balanced and ordered

# Interview question
Create a method to verify that a string of open and closed parens and square brackets is both balanced, and ordered
Returns Boolean

# Sample testcases:
() - pass
([)] - fail, this is balanced, but not ordered. I got busted on this one
([]) - pass
([) - fail

# Execution results
    Testcase 1: (). Expecting pass
    String length is even
    Got here with ()
    Looking at (
    Open ( seen. Current list of opens: ['(']
    Looking at )
    Saw a corresponding close for the last open. Remaining opens: []
    Closed them all

    Testcase 2: ([)]. Expecting fail
    String length is even
    Got here with ([)]
    Looking at (
    Open ( seen. Current list of opens: ['(']
    Looking at [
    Open [ seen. Current list of opens: ['(', '[']
    Looking at )
    Wrong close brace seen. FAIL
    
    Testcase 3: ([]). Expecting pass
    String length is even
    Got here with ([])
    Looking at (
    Open ( seen. Current list of opens: ['(']
    Looking at [
    Open [ seen. Current list of opens: ['(', '[']
    Looking at ]
    Saw a corresponding close for the last open. Remaining opens: ['(']
    Looking at )
    Saw a corresponding close for the last open. Remaining opens: []
    Closed them all

    Testcase 4: ([). Expecting fail
    String length is odd. FAIL

    Testcase 5: {}. Expecting fail
    String length is even
    Got here with {}
    Looking at {
    Invalid char seen: {. FAIL

    Testcase 6: ]. Expecting fail
    String length is odd. FAIL
