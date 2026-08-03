
# Git Workflow for This Project

## 1. Start each session
Update your local branch before making changes:

```bash
git pull --ff-only origin main
```

## 2. Make your changes
Work on the project as usual.

## 3. Check what changed
```bash
git status
```

## 4. Add your changes
```bash
git add .
```

## 5. Commit your changes
```bash
git commit -m "Describe your change"
```

## 6. Push your changes
```bash
git push origin main
```

## Simple habit to remember
- pull first
- edit
- add
- commit
- push

## Why use `--ff-only`?
- it updates your branch only when Git can do so without creating a merge commit
- it keeps your history clean and simple