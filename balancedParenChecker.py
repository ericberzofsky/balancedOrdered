##################################################################
# Interview question: Create a method to verify that a string of
# open and closed parens and square brackets is both balanced,
# and ordered
#
# Returns Boolean
# Sample testcases:
# () - pass
# ([)] - fail, this is balanced, but not ordered. I got busted on this one
# ([]) - pass
# ([) - fail
##################################################################
valid_chars = ('(',')','[',']')
def check_even_length(string_to_check):
    
    ##################################################################
    # A string of odd length is an immediate failure,
    # as it can't be balanced
    ##################################################################
    if len(string_to_check) % 2 > 0:
        print("String length is odd. FAIL")
        return False
    else:
        print("String length is even")
        return True

def check_for_balanced_and_ordered(string_to_check):
    print("Got here with {0}".format(string_to_check))
    
    ##################################################################
    # A balanced string is one that has as many close paren and
    # close square braces as open parens/square braces.
    #
    # For the string to also be ordered, we must close the last brace
    # we opened
    ##################################################################

    
    ##################################################################
    # As we traverse the string, keep an ordered list of the open
    # braces we see. When we see a close brace, ensure that it matches
    # the close of the last open we saw. If so, pop off the last open.
    # If not, fail as unodered
    ##################################################################
    opens = list()

    for next_char in string_to_check:
        print("Looking at {0}".format(next_char))
        ##################################################################
        # Ensure only valid chars seen
        ##################################################################
        if next_char not in valid_chars:
            print("Invalid char seen: {0}. FAIL".format(next_char))
            return False
        if next_char in ('(','['):
            opens.append(next_char)
            print("Open {0} seen. Current list of opens: {1}".format(next_char, opens))
        else:
            ##################################################################
            # If we see a close without any more opens left to close, fail
            ##################################################################
            if len(opens) == 0:
                print("We saw a close {0} without any remaining opens. FAIL".format(next_char))
                return False
            if (next_char == ')' and opens[-1] == '(') \
               or (next_char == ']' and opens[-1] == '['):
                opens.pop()
                print("Saw a corresponding close for the last open. Remaining opens: {0}".format(opens))
            else:
                print("Wrong close brace seen. FAIL")
                return False

    ##################################################################
    # At this point, we should not have any more opens, and can return
    # a pass, but let's do one more check
    ##################################################################
    if len(opens) == 0:
        print("Closed them all")
        return True
    else:
        print("We still expect some closes. Remaining opens: {0}. FAIL".format(opens))
        return False
            
def is_string_balanced_and_ordered (string_to_check):
    if not check_even_length(string_to_check): return False
    return check_for_balanced_and_ordered(string_to_check)
##################################################################
# Main code starts here
##################################################################
print("Testcase 1: (). Expecting pass")
assert(is_string_balanced_and_ordered("()"))
print("------------------------------------------")
print("Testcase 2: ([)]. Expecting fail")
assert(not is_string_balanced_and_ordered("([)]"))
print("------------------------------------------")
print("Testcase 3: ([]). Expecting pass")
assert(is_string_balanced_and_ordered("([])"))
print("------------------------------------------")
print("Testcase 4: ([). Expecting fail")
assert(not is_string_balanced_and_ordered("([)"))
print("------------------------------------------")
print("Testcase 5: {}. Expecting fail")
assert(not is_string_balanced_and_ordered("{}"))
print("------------------------------------------")
print("Testcase 6: ]. Expecting fail")
assert(not is_string_balanced_and_ordered("]"))

print("All tests passed. Have a nice day!")
 
