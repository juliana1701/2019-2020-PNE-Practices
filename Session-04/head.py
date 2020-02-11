from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print("First line of the RNU6_269P.txt file:")
print(file_contents.split("\n")[0])
