def check_parentheses(s: str) -> bool:
    s = s.replace(" ", "")
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0


print(check_parentheses(""))
print(check_parentheses("("))
print(check_parentheses(")"))
print(check_parentheses(")("))
print(check_parentheses("()"))
print(check_parentheses("( (()) ()()) )"))
print(check_parentheses("( (()) (()()) )"))  
print(check_parentheses("( (()) (()()) ) ("))
print(check_parentheses("( (()) (()()) ) ()"))
