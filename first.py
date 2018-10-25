a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}


def print_depth(data, depth=1):
    for key, value in data.items():
        print(key, depth)
        if type(value) is dict:
            depth += 1
            print_depth(value, depth)


print_depth(a)
