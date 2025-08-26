# Demonstrating the working local and global variables.

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
