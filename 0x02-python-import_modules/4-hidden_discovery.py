#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lib = dir(hidden_4)
    for i in lib:
        if i[0] == "_":
            continue
        else:
            print(i)
