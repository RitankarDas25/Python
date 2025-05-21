# recursion is calling itself
def show(n):
    if(n<0): #base case condition which stops the recursion
        return
    print(n)
    show(n-1) # recursive call
    print(n) # backtrack to last function call prints in reverse
show(5)

# factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)
print(fact(3))

# waf to print all elements of list

def print_list(list,i=0): # i=0 gives default value of i as 0
    if(i==len(list)):
        return
    print(list[i])
    print_list(list,i+1)
arr =["a","b","c","d"]
print_list(arr)