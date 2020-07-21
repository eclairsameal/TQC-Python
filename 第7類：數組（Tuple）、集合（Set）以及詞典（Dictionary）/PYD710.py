def input_dir():
    input_dir = {}
    while True:
        key = input("Key: ")
        if key=="end":
            break
        input_dir[key] = input("Value: ")
    return input_dir

dir_str = input_dir()
search_key = input("Search key: ")
print( str(search_key in dir_str.keys()))