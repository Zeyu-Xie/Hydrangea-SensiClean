import os
import sys
import json

# Const
chr_range_list = list(range(1, 55296))+list(range(57344, 1114112))
data_path = os.path.join(os.path.dirname(__file__), "data.json")

# Initialize chr_list
chr_list = {}
with open(data_path, "r") as file:
    try:
        chr_list = json.loads(file.read())
    except Exception as e:
        print("ERROR", type(e), e)
        chr_list = {}
    file.close()
for i in chr_range_list:
    if chr(i) not in chr_list:
        print(f"Ading \"{chr(i)}\" (unicode {i}) into chr_list")
        chr_list[chr(i)] = set()
    elif type(chr_list[chr(i)]) == {}:
        chr_list[chr(i)] = set()
    else:
        chr_list[chr(i)] = set(chr_list[chr(i)])
chr_list_backward = chr_list

# Function 1: Append
def _append(key, value):
    global chr_list
    chr_list[key].add(value)
    chr_list[value].add(key)
    for i in chr_list[value]:
        if i != key:
            chr_list[i].add(key)
            chr_list[key].add(i)
    for i in chr_list[key]:
        if i != value:
            chr_list[i].add(value)
            chr_list[value].add(i)
    for i in chr_list[key]:
        for j in chr_list[value]:
            if i != j:
                chr_list[i].add(j)
                chr_list[j].add(i)

# Function 2: Write into the JSON File
def write_file():
    global chr_list_backward
    global chr_list
    chr_list_backward = chr_list
    tmp_list = {}
    for i in chr_range_list:
        tmp_list[chr(i)] = list(chr_list[chr(i)])
    str = json.dumps(tmp_list, ensure_ascii=False, indent=4)
    with open(data_path, "w") as file:
        file.write(str)
        file.close()

# Function 3: Print List
def print_list(_key):
    global chr_list
    print(f"{_key}: ", end = "")
    for i in chr_list[_key]:
        print(i, end = " ")
    print("")

# Function 4: Go Backward
def backward():
    global chr_list_backward
    global chr_list
    chr_list = chr_list_backward

# Main Part
if __name__ == "__main__":
    
    while 1:
        print("0. Exit")
        print("1. Append")
        print("2. Discard")
        print("3. Backward (Not Available)")
        print("4. Query")
        tmp_1 = input("- Choose what you want to do: ")
        try:
            tmp_1 = int(tmp_1)
        except Exception as e:
            print("ERROR:", type(e), e)
            sys.exit(1)

        # Exit
        if tmp_1 == 0:
            write_file()
            sys.exit(0)
        # Append Connection
        elif tmp_1 == 1:
            while 1:
                print("- Please input your relative character set")
                _key = input("")
                if _key == "exit":
                    break
                else:
                    _key = list(_key)
                    for i in _key:
                        if i != _key[0]:
                            _append(i, _key[0])
                    for i in _key:
                        print_list(i)
                    write_file()
        # Discard
        elif tmp_1 == 2:
            while 1:
                _key = input("- Which character do you want to discard? ")
                if _key == "exit":
                    break
                elif _key not in chr_list:
                    print("ERROR: Character Not Found")
                    continue
                else:
                    for i in chr_list[_key]:
                        chr_list[i].discard(_key)
                        print_list(i)
                    chr_list[_key] = set()
                    print_list(_key)
                    write_file()
        # Backward
        elif tmp_1 == 3:
            backward()
            write_file()
            print("Backward")
        # Query
        elif tmp_1 == 4:
            while 1:
                _key = input("- Input the key: ")
                if _key == "exit":
                    break
                elif _key not in chr_list:
                    print("ERROR: Wrong Key")
                    continue
                else:
                    print_list(_key)