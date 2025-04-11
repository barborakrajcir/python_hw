import json

with open('alice.txt', mode="r", encoding="utf-8") as file:   
    total_char = {}
    for line in file:
        line = line.strip()
        line = line.lower()
        line = line.replace(" ", "")  
        line = line.strip('\n')
        for char in line:
            if char not in total_char:
                total_char[char] = 0
            total_char[char] += 1
    


sorted_dict = dict(sorted(total_char.items()))

with open("hw01_output.json.", "w", encoding="utf-8") as output_file:
    json.dump(sorted_dict, output_file, ensure_ascii=False, indent=4)