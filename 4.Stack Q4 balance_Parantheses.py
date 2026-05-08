
def is_balanced(s: str) -> bool:        # “This function takes a string as input and returns a boolean result.
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():  # opening brackets
            stack.append(char)
        elif char in mapping:  # closing brackets       checking for key in dictionary
            if (not stack) or stack[-1] != mapping[char]:#If the stack is empty OR the top of the stack doesn’t match the closing bracket, then return False.
                return False
            stack.pop()

    return not stack        #check if stack is empty or not , if balance then stack should be empty (not stack) == True

print(is_balanced("{(a+b))(a-b)}"))
