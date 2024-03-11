# Default mood of this open() method is 'r'
with open("../files/doc.txt") as file:
    content = file.read()
    print(content)

# we cannot do that because the file is already closed, but the file variable still exists
# (The close() method is called implicitly even though we don't call it explicitly.
# The Python interpreter will call the method when it sees that we have written a with-context manager.)
# file.read()

print(content)