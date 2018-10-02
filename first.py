a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}


def print_depth(data):
    for key, value in data.items():
        if type(value) is dict:
            print_depth(value)
        else:
            print(key, value)


print_depth(a)
