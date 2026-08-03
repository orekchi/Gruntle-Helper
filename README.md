Gruntle-Helper is a searchable note-taking app, written in Python using Django and is a web based app. The idea came as I was 
learning stuff like Python, Linux, Django, Kivy and needed to write notes, but then it was difficult to organize them and to 
search for what I needed. I wanted to have a few different topics (Python, Linux...) and then being able to search inside of 
them. 

## Requirements

- Python 3.14
- UV

## Installation

1. Install UV if it is not already available:
   https://docs.astral.sh/uv/getting-started/installation/

2. From the project root, install the dependencies:

```bash
uv sync
```

3. Run the project:
```bash
uv run manage.py runserver
```

4. go to the browser and type:
```bash
localhost:8001
```

   



# Git Workflow 

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

