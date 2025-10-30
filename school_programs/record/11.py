#  Demonstrating the working of .tell() and .seek() methods on a text file.

with open("authors.txt", 'a+') as f:
    f.write("Homer Shaw\n") # Write string to file
    print(f.tell())
    f.seek(0) # Re-position file pointer to BOF
    print(f.tell()) # Print file pointer position
    f.write("Shakespeare\n") # Writes to EOF
    f.seek(0)
    print(f.read()) # Print file contents
    print(f.tell())
    f.close() 
