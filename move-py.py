import os
import shutil

source_dir = os.getcwd()
destination_dir = 'python'

os.makenewdir(destination_dir, exist_ok=True)
for filename in os.listdir(source_dir):
  if filename.endwith(".py"):
    shutil.move(os.path.join(source_dir, filename), destination_dir)
    print(f"Moved: {filename}")

print("All .py files have been moved to the destination directory.")
    