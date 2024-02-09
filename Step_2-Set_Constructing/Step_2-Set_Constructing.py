import json
import os
import sys

# Const
chr_range_list = list(range(1, 55296))+list(range(57344, 65536))

# Function 1: Write into the JSON File
def write_file():
    tmp_list = {}
    for i in chr_range_list:
        tmp_list[chr(i)] = list(chr_list[chr(i)])
    str = json.dumps(tmp_list, ensure_ascii=False, indent=4)
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "Step_2-Set_Constructing.json"), "w") as file:
        file.write(str)
        file.close()

# Initialize chr_list
chr_list = {}
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "Step_2-Set_Constructing.json"), "r") as file:
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

# Start Position
tot = 1
try:
    ipt = input("Please input your editing start position: ")
    tot = int(ipt)
except Exception as e:
    print("ERROR", type(e), e)
    print("Tot will be set as 1 by default.")
    tot = 1

# Editing Set Data
while tot in chr_range_list:

    chr_tot = chr(tot)
    chr_tot_list = chr_list[chr_tot]

    # Print Status
    print(f"{chr_tot} (Unicode {tot}): ", end = "")
    for i in chr_tot_list:
        print(i, end = " ")
    print("")
    
    chr_input = ""

    while True:

        chr_input = input(f"Input the new linked character with {chr_tot}: ")
        
        # Press Enter: Switch to Another Character
        if chr_input == "":
            break
        # Input "exit": Pause
        elif chr_input == "exit":
            write_file()
            sys.exit(0)
        # Self?
        elif chr_input == chr_tot:
            print("Self, Repeated")
        # Unavailable Character?
        elif chr_input not in chr_list:
            print("Unavailable Character")
        # Existed Character?
        elif chr_input in chr_tot_list:
            print("Existed Character")
        # Legal Character
        else:
            # Merge Sets
            chr_list[chr_tot].add(chr_input)
            chr_list[chr_input].add(chr_tot)
            for j in chr_list[chr_input]:
                if j == chr_tot:
                    continue
                else:
                    chr_list[j].add(chr_tot)
                    chr_list[chr_tot].add(j)
            for j in chr_list[chr_tot]:
                if j == chr_input:
                    continue
                else:
                    chr_list[j].add(chr_input)
                    chr_list[chr_input].add(j)
            for j in chr_list[chr_input]:
                for k in chr_list[chr_tot]:
                    if j == k:
                        continue
                    else:
                        chr_list[j].add(k)
                        chr_list[k].add(j)

            # Print Status           
            print(f"{chr_tot} (Unicode {tot}): ", end = "")
            for i in chr_tot_list:
                print(i, end = " ")
            print("")

    # Move Forward
    tot += 1