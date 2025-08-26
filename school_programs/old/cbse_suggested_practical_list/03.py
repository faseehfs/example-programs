# Remove all the lines that contain the character 'a' in a file and write it to another file.

with open("README.md", "r") as f:
    lines = [line for line in f.readlines() if line.find("a") == -1]

with open("temp.txt", "w") as f:
    f.writelines(lines)