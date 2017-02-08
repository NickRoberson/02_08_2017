def main():
    input1 = "(()())))((()))" # Doesnt Work
    input2 = "(())))((()))" # Doesnt Work
    input3 = "(()()))(()))" # Doesnt Work
    input4 = "()((())()()()())" # Works :)
    check_parens(input1)
    check_parens(input2)
    check_parens(input3)
    check_parens(input4)

def check_parens(str):
    lst = list()
    for c in str:
        if c == "(":
            lst.append("(")
        else:
            if(len(lst) == 0):
                print "Invalid parenthesis, exiting"
                return False
            else:
                lst.pop()
    if len(lst) == 0:
        print "Valid parenthesis, good on you!"
        return True
    else:
        return False

main()
