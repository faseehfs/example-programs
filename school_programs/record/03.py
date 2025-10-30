# Demonstrating the working of local and global variables.

# Define three functions: 
# - one that uses a local variable, 
# - one that reads a global variable, 
# - and one that modifies a global variable.

def f1():
    local_var = 1
    print(local_var)

def f2():
    print(global_var)

def f3():
    global global_var
    global_var = -1
    print(global_var)

global_var = 0

f1()
f2()
f3()
 