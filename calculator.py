def add(a,b):
 return a + b

def sub(a,b):
 return a - b

def multiply(a,b):
 return a - b

def division(a,b):
 return a/b

print("please select the operator:")
print("a. add")
print("b. subtract")
print("c. multyply")
print("d. division")


choice = input("please enter choice (a/b/c/d): ")

num_1 = int(input ("please enter the first number: "))
num_2 = int(input ("please enter the second number: "))

def new_func(multiply, num_1, num_2):
    print(num_1, "*", num_2, "=", multiply(num_1,num_2))

if choice=='a':
 print(num_1,"+", num_2, "=", add(num_1,num_2))

elif choice=='b':
 print(num_1, "-", num_2, "=", sub(num_1,num_2))

elif choice=='c':
 new_func(multiply, num_1, num_2)

elif choice=='d':
 print(num_1, "/", num_2, "=", division(num_1, num_2))

else:
 print("this is an invalid input")
 