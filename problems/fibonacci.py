#Define the fibonacci sequence function 
def fib(n, k):
    # first 2 cases
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1, k) + fib(n-2, k)

# ask user for the period of rabbit reproduction
n = int(input("How many months of rabbits are you tracking? "))
# ask user for litter size
k =  int(input("What is the litter size? "))
# print results
print(fib(n,k))
