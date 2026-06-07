"""
Project: Add Date to Filenames
Course: Learn Python by Doing with 100 Projects
"""
from datetime import datetime
import os



def main() -> None:
    """Run the project."""
    print("Project starter: Add Date to Filenames")
    directory = 'files'
    filepaths  = os.listdir(directory)
    print(filepaths)
    # filenames = [for file in directory in range(filepaths)]
    now = datetime.now()
    day_name = now.strftime("%A")
    print(day_name)
    # loop over the files in the directory and add the date to the filename
    for file in filepaths:
        print(file)

        # file.append(day_name)
        # "file_{day_name}_{filepaths[file]}"
if __name__ == "__main__":
    main()
