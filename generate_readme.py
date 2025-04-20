import os

programs_folder = "programs"
ignored_folders = ["z-old", ".git", "__pycache__", "node_modules", ".vscode"]


def generate_readme():
    readme_content = "# Example Programs\n\n"

    if not os.path.exists(programs_folder):
        print(f"'{programs_folder}' directory does not exist.")
        return

    for folder in os.listdir(programs_folder):
        if folder in ignored_folders:
            continue

        if not os.path.isdir(os.path.join(programs_folder, folder)):
            continue

        folder_name = folder.replace("-", " ").lower()
        readme_content += f"- [{folder_name}](/{programs_folder}/{folder}/)\n"

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)
        print("README.md generated successfully!")


generate_readme()
