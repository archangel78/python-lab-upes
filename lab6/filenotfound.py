file_name = input("Enter file name to read: ")

try:
    file = open(file_name, "r")
    print(file.read())
except FileNotFoundError:
    print("Invalid file name")
