import os
import sys
import json

tmp_1 = ""
tmp_2 = {}

# Read into Tmp_2
with open(os.path.join(os.path.dirname(__file__), "source.txt"), "r") as file:
    tmp_1 = file.read()
    file.close()
tmp_1 = tmp_1.split("\n")
for item in tmp_1:
    item = item.split(" ")
    tmp_2[item[0]] = item[1:]

chr_list = []

# Sort
for i in tmp_2:
    tmp_2[i].sort()
    chr_list.append(i)
def sort_f(chr):
    return tmp_2[chr][0]
chr_list.sort(key = sort_f)

# Output

def cut_tone(_str):
    if _str[-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return _str[:-1]
    return _str

with open(os.path.join(os.path.dirname(__file__), "dictionary.json"), "w") as file:
    json.dump(tmp_2, file, indent = 4, ensure_ascii = False)
    file.close()
with open(os.path.join(os.path.dirname(__file__), "dictionary_character_only.txt"), "w") as file:
    l = len(chr_list)
    for i in range(0, l):
        if (l == 0) or (cut_tone(tmp_2[chr_list[i-1]][0]) != cut_tone(tmp_2[chr_list[i]][0])):
            file.write("\n")
            file.write("== "+cut_tone(tmp_2[chr_list[i]][0])+" ==")
            file.write("\n")
        file.write(chr_list[i]+"\n")
    file.close()