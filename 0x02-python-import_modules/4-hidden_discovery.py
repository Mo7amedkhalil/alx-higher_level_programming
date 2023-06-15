#!/usr/bin/python3
if "__main__" == __name__:
    import hidden_4
    for item in dir(hidden_4):
        if not ('__' in item and (item.index('__') == 0)):
            print(item)
