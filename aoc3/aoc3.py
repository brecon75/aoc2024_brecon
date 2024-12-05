import re  ## lmao regex seekhna padgaya

def main():
    with open("input.txt", "r") as file:
        string = file.read()
    pattern = r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))'
    mul = r'mul\((\d{1,3}),(\d{1,3})\)'
    valid_muls = []
    
    sum = 0
    initial = "mul(747,16)*why()mul(354,748)how()<?mul(29,805)where()mul(480,119)!,why()mul(685,393)(~'&[what()what()mul(376,146)"
    init_muls = re.findall(mul, initial)
    for init_mul in init_muls:
        sum += int(init_mul[0]) * int(init_mul[1])
    last_instruction = None

    for match in re.finditer(pattern, string):
        current = match.group(0) 
        
        if current == 'don\'t()':
            last_instruction = 'dont' 
        elif current == 'do()':
            last_instruction = 'do'  
        elif current.startswith('mul'):  
            if last_instruction == 'do':
                valid_muls.append(current)
    
    for valid_mul in valid_muls:
        vmul = re.search(mul, valid_mul)
        sum += int(vmul.group(1)) * int(vmul.group(2))

    print(sum)
    


if __name__ == "__main__":
    main()