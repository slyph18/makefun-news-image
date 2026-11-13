#!/usr/bin/env python3
"""make.fun entry: writes the bundled image to /output/entry.png. Deterministic, no network."""
import shutil, os
os.makedirs("/output", exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(__file__), "entry.png"), "/output/entry.png")
print("entry.png written")
