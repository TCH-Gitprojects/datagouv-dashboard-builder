# Git Workflow Guide

Complete guide for setting up GitHub repository and pushing your code safely.

---

## 🚀 Quick Setup (Recommended)

### Step 1: Initialize Local Repository

```bash
# Navigate to your project folder
cd /path/to/datagouv-streamlit

# Initialize Git repository
git init

# Set default branch to main
git branch -m main
```

### Step 2: Configure Git (First Time Only)

```bash
# Set your name and email
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Verify configuration
git config --list
```

### Step 3: Create GitHub Repository

#### Option A: Using GitHub CLI (gh)

```bash
# Install gh if not already installed
# macOS: brew install gh
# Windows: winget install GitHub.cli
# Linux: see https://github.com/cli/cli/blob/trunk/docs/install_linux.md

# Authenticate with GitHub
gh auth login

# Create repository and push
git add .
git commit -m "Initial commit: DataGouv Dashboard Builder v1.0"

# Create public repo and push
gh repo create datagouv-dashboard-builder --public --source=. --push

# Or create private repo
# gh repo create datagouv-dashboard-builder --private --source=. --push
```

#### Option B: Manual Setup (Web Interface)

1. Go to [github.com/new](https://github.com/new)
2. Fill in repository details:
   - **Repository name**: `datagouv-dashboard-builder`
   - **Description**: "Transform French Open Data into Beautiful Dashboards"
   - **Visibility**: Public or Private
   - **☐** Initialize with README (UNCHECK this - we already have one)
   - **☐** Add .gitignore (UNCHECK this - we already have one)
   - **☐** Choose a license (UNCHECK this - we already have one)
3. Click **Create repository**

4. Push your code:
```bash
git add .
git commit -m "Initial commit: DataGouv Dashboard Builder v1.0"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/datagouv-dashboard-builder.git

# Push to main branch
git push -u origin main
```

---

## 🔧 Fixing "Non-Fast-Forward" Errors

If you encounter this error:
```
! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/...'
```

### Solution 1: Force Push (⚠️ Destructive - Use with Caution)

```bash
# Only use if you're sure no one else has pushed to the repo
git push -f origin main
```

### Solution 2: Pull and Merge (Recommended)

```bash
# Fetch remote changes
git fetch origin

# Merge remote changes with yours
git pull origin main --rebase

# If conflicts occur, resolve them, then:
git add .
git rebase --continue

# Push again
git push origin main
```

### Solution 3: Reset and Clean Push

```bash
# Save your current work on a backup branch
git branch backup-main

# Fetch remote
git fetch origin

# Reset local main to match remote
git reset --hard origin/main

# Cherry-pick your commits (if any)
# Or manually copy your files back

# Add and commit your changes
git add .
git commit -m "Initial commit: DataGouv Dashboard Builder v1.0"

# Push
git push origin main
```

---

## 📝 Common Git Commands

### Daily Workflow

```bash
# Check status
git status

# Stage all changes
git add .

# Stage specific file
git add src/database.py

# Commit with message
git commit -m "feat: add SQL query builder"

# Push to remote
git push origin main

# Pull latest changes
git pull origin main
```

### Branching

```bash
# Create new branch
git checkout -b feature/new-widget

# Switch branches
git checkout main

# List branches
git branch -a

# Merge branch into main
git checkout main
git merge feature/new-widget

# Delete branch after merge
git branch -d feature/new-widget
```

### Viewing History

```bash
# View commit history
git log --oneline -10

# View changes in working directory
git diff

# View changes in staging area
git diff --staged
```

### Undoing Changes

```bash
# Unstage a file
git reset HEAD src/database.py

# Discard changes in working directory
git checkout -- src/database.py

# Amend last commit
git commit --amend -m "New commit message"

# Revert a commit (creates new commit)
git revert HEAD
```

---

## 🔄 Complete Reset (Nuclear Option)

If everything is messed up and you want to start fresh:

```bash
# 1. Save your code somewhere safe (copy the entire folder)
cp -r datagouv-streamlit datagouv-streamlit-backup

# 2. Remove git history
rm -rf .git

# 3. Reinitialize
git init
git branch -m main

# 4. Add and commit
git add .
git commit -m "Initial commit: DataGouv Dashboard Builder v1.0"

# 5. Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/datagouv-dashboard-builder.git
git push -f origin main
```

---

## ✅ Pre-Push Checklist

Before pushing to GitHub, verify:

- [ ] `requirements.txt` is up to date
- [ ] `.gitignore` includes sensitive files (`.env`, data files)
- [ ] No large data files (>100MB) are being committed
- [ ] Code runs without errors: `streamlit run app.py`
- [ ] README has correct repository URL
- [ ] No API keys or secrets in code

---

## 🐛 Troubleshooting

### Issue: "fatal: not a git repository"

```bash
# You're not in a git repository
cd /path/to/your/project
git init
```

### Issue: "fatal: Authentication failed"

```bash
# Update credentials
git config --global --unset user.password
# Or use SSH instead of HTTPS
```

### Issue: "Changes not staged for commit"

```bash
# Check what files changed
git status

# Stage them
git add .
```

### Issue: "Your branch is ahead of 'origin/main' by X commits"

```bash
# This is normal - just push
git push origin main
```

---

## 🎯 Best Practices

1. **Commit Often**: Make small, focused commits
2. **Write Good Messages**: Use conventional commits format
   - `feat: add new chart type`
   - `fix: resolve SQL query bug`
   - `docs: update README`
   - `refactor: simplify data analyzer`

3. **Pull Before Push**: Always pull latest changes first
4. **Use Branches**: Don't commit directly to main for big features
5. **Review Changes**: Check `git diff` before committing

---

## 📚 Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Fixing common mistakes
