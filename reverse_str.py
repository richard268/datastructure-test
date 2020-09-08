def reverse_str(str):
    temp=[char for char in str] #create a list to store strings
    stack=[] #create a stack list
    for i in range(len(temp)):
        stack.append(temp[i]) #similar to push() on stack
    for i in range(len(temp)):
        temp[i]=stack.pop()
    return ''.join(temp[i] for i in range(len(temp)))

print(reverse_str('hello'))
print(reverse_str('MyCodeSchool'))

def reverse_str1(str):
    temp=[char for char in str]
    i=0
    j=len(temp)-1
    while i<j:
        a=temp[i]
        temp[i]=temp[j]
        temp[j]=a
        i+=1
        j-=1
    return ''.join(temp[i] for i in range(len(temp)))

print(reverse_str1('hello'))
print(reverse_str1('MyCodeSchool'))

def balanced_parentheses(str):
    def arepair(open,close):
        if open=='(' and close==')':
            return True
        elif open=='{' and close=='}':
            return True
        elif open=='[' and close==']':
            return True
        else:
            return False
    stack=[] #define a stack list
    for i in range(len(str)):
        if str[i]=='(' or str[i] == '{' or str[i]=='[':
            stack.append(str[i])
        else:
            if not stack or not arepair(stack[-1],str[i]):
                return False
            else:
                stack.pop()
    return  len(stack)==0

print(balanced_parentheses('(((())))'))
print(balanced_parentheses('{[(())]}'))
print(balanced_parentheses('[((())))'))
