###### FileNotFound #####
#with open("file.txt") as file:
#    file.read()
try:
    a_file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["different_key"])
    a_list = ["apple", "pear", "cherry"]
    print(a_list[3])
    text = "abd"
    print(text + 5)

except FileNotFoundError:
    open("file.txt", "w")

except KeyError as error_message:
    print(f"the key {error_message} does not exist")

except IndexError:
    print("the requested item is out of the index range")

except TypeError:
    print("type error")

else:
    contents = a_file.read()
    print(contents)

finally:
    raise KeyError("raise an error anyway")




