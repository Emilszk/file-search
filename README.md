# File Search Tool (Python)

A simple command-line Python tool for searching files recursively in directories.  
It supports partial name matching, persistent session path, and interactive repeated searches.

---

## Features

- Recursive file search using `os.walk()`
- Partial filename matching (case-insensitive)
- Persistent folder path across search sessions
- Option to use current directory automatically
- Interactive loop for multiple searches
- Clean CLI output with session separation

---

## How it works

The program:
1. Asks for a folder path (or uses current directory if empty)
2. Asks for a file name or part of it
3. Searches recursively through all subfolders
4. Displays all matching files with full paths
5. Shows total number of matches
6. Allows repeated searches in the same or new directory

---

## Usage

Run the script:

```bash
python main.py
