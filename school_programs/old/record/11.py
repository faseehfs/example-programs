#  Demonstrating the working of .tell() and .seek() methods on a text file.

with open("README.md", 'a+') as f:
    f.write("Homer Shaw ")
    print(f.tell())
    f.seek(0)
    print(f.tell())
    f.write("Shakespeare ")
    f.seek(0)
    print(f.read())
    print(f.tell())
    f.close()
