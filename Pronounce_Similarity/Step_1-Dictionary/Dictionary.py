import os
import sys
import json

tmp_1 = ""
tmp_2 = {}
with open(os.path.join(os.path.dirname(__file__), "Dictionary.txt"), "r") as file:
    tmp_1 = file.read()
    file.close()
tmp_1 = tmp_1.split("\n")
for item in tmp_1:
    item = item.split(" ")
    tmp_2[item[0]] = item[1:]

with open(os.path.join(os.path.dirname(__file__), "Dictionary.json"), "w") as file:
    json.dump(tmp_2, file, indent = 4, ensure_ascii = False)
    file.close()

if __name__ == "__main__":
    while 1:
        _str = input("Your Query: ")
        if _str == "exit":
            sys.exit(0)
        elif _str[-1].isdigit():
            for i in tmp_2:
                if _str in tmp_2[i]:
                    print(i, end = " ")
            print("")
        else:
            for i in tmp_2:
                for j in range(1,5):
                    _str_1 = _str + str(j)
                    if _str_1 in tmp_2[i]:
                        print(i, end = " ")
            print("")