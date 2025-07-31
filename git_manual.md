# Git Manual

## 🔧 Configuration
- `git config --global user.name "Your Name"`
- `git config --global user.email "you@example.com"`
- `git config --list` – View current config

---

## 📁 Repository Initialization & Cloning
- `git init` – Initialize a new repo
- `git clone <url>` – Clone an existing repo

---

## 📄 Staging & Committing
- `git status` – Check current status
- `git add <file>` – Stage a file
- `git add .` – Stage all changes
- `git commit -m "Message"` – Commit staged changes

---

## 📚 Branching
- `git branch` – List branches
- `git branch <name>` – Create new branch
- `git checkout <name>` – Switch branch
- `git checkout -b <name>` – Create & switch branch
- `git merge <branch>` – Merge branch into current
- `git branch -d <name>` – Delete branch

---

## 🔁 Remote Repositories
- `git remote -v` – View remotes
- `git remote add origin <url>` – Add remote
- `git push -u origin <branch>` – Push & set upstream
- `git push` – Push changes
- `git pull` – Pull from remote
- `git fetch` – Fetch changes (no merge)

---

## 🕘 History & Logs
- `git log` – Show commit history
- `git log --oneline` – Compact log
- `git diff` – Show unstaged changes
- `git diff --staged` – Show staged changes

---

## 🧪 Undoing
- `git checkout -- <file>` – Discard file changes
- `git reset <file>` – Unstage file
- `git reset --hard` – Reset to last commit (destructive)
- `git revert <commit>` – Undo a commit (safe)

---

## 🧹 Cleaning & Tags
- `git clean -fd` – Remove untracked files
- `git tag` – List tags
- `git tag <tag>` – Create tag

---

## 📦 Stash
- `git stash` – Stash changes
- `git stash pop` – Reapply stash
- `git stash list` – Show stashes
