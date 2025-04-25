import os

programs_folder = "programs"
ignored = [".git", "__pycache__", "node_modules", ".vscode"]


def generate_readme():
    readme_content = "# Example Programs\n\n"

    if not os.path.exists(programs_folder):
        print(f"'{programs_folder}' directory does not exist.")
        return

    for item in sorted(os.listdir(programs_folder)):
        if item in ignored:
            continue

        name, _ = os.path.splitext(item.replace("-", " ").lower())
        readme_content += f"- [{name}]({programs_folder}/{item})\n"

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)
        print("README.md generated successfully!")


generate_readme()
