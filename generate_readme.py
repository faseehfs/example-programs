import os

programs_folder = "programs"
ignored = [".git", "__pycache__", "node_modules", ".vscode"]

content_before = """# Example Programs

"""

content_after = """- [Git Manual](git_manual.md)"""

def generate_readme():
    readme_content = content_before

    if not os.path.exists(programs_folder):
        print(f"'{programs_folder}' directory does not exist.")
        return

    for item in sorted(os.listdir(programs_folder)):
        if item in ignored:
            continue

        name, _ = os.path.splitext(item.replace("-", " ").replace("_", " ").lower())
        readme_content += f"- [{name}]({programs_folder}/{item})\n"
    
    readme_content += content_after

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)
        print("README.md generated successfully!")

if __name__ == "__main__":
    generate_readme()
