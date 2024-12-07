def main():
    with open("input.txt", "r") as file:
        line_arr = [list(line.split()) for line in file]
    for line in line_arr:
        for i in range(len(line)):
            line[i] = int(line[i])

    part2 = 0
    arr = [(line_arr[i][0],line_arr[i][1:]) for i in range(len(line_arr))]
    for line in arr:
        if check_operators(line[0], line[1]):
            part2+= line[0]
    print("Part2: ",part2)

def check_operators(result, inputs):
    def helper(current_result, index):
        if index == len(inputs):
            return current_result == result

        # Try adding the next number
        if helper(current_result + inputs[index], index + 1):
            return True

        # Try multiplying the next number
        if helper(current_result * inputs[index], index + 1):
            return True

        # Try concatenating the next number
        ## removing this would give the answer to part 1 (without the concatenation operation)
        concatenated_number = int(str(current_result) + str(inputs[index]))
        if helper(concatenated_number, index + 1):
            return True

        return False

    # Start the recursion with the first number in the inputs
    return helper(inputs[0], 1)

if __name__ == "__main__":
    main()