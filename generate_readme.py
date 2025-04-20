import os

ignored_folders = ["z-old", ".git", "__pycache__", "node_modules", ".vscode"]


def generate_readme():
    readme_content = "# Example Programs\n\n"

    for folder in os.listdir("."):
        if folder in ignored_folders or not os.path.isdir(folder):
            continue

        folder_name = folder.replace("-", " ").lower()
        readme_content += f"- [{folder_name}](/{folder}/)\n"

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)
        print("README.md generated successfully!")


generate_readme()
