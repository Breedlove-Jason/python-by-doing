"""
Project: Add Date to Filenames
Course: Learn Python by Doing with 100 Projects
"""

from datetime import datetime
import os


def main() -> None:
    """Run the project."""
    print("Project starter: Add Date to Filenames")

    directory = "files"

    filenames = os.listdir(directory)
    print(filenames)

    day = datetime.now().strftime("%A")

    for filename in filenames:
        filepath = os.path.join(directory, filename)

        with open(filepath, "r") as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            new_filename = f"{filename[:-4]}-{word_count}-{day}.txt"

            new_filepath = os.path.join(directory, new_filename)
            os.rename(filepath, new_filepath)

            print(f"Renamed {filename} to {new_filename}")


if __name__ == "__main__":
    main()
