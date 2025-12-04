# scripts/update_readme.py
import os
import glob

def count_problems():
    easy = len(glob.glob("problems/easy/*.md"))
    medium = len(glob.glob("problems/medium/*.md"))
    hard = len(glob.glob("problems/hard/*.md"))
    
    print(f"Easy: {easy}")
    print(f"Medium: {medium}")
    print(f"Hard: {hard}")
    print(f"Total: {easy + medium + hard}")

count_problems()
