#implementing stack using pyhton class 

class Stack():
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

#Function to check pair
 


# Function to check a balance is in stack or not

def is_paren_balance(paren_string):
    stack=Stack()

    is_balanced=True

    for paren in range(len(paren_string)):
        if paren_string[paren] == "(":
            stack.push(paren_string[paren])
        else:
            if stack.is_empty():
                is_balanced = False
            else:
                stack.pop()
            
    if is_balanced and stack.is_empty():
        return True
    else:
        return False

    
print(is_paren_balance(")())"))