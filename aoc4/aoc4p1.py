def main():
    with open("input.txt", "r") as file:
        line_arr = [list(line.strip()) for line in file]

    count = 190+248
    for i in range(len(line_arr)-3):
        for j in range(len(line_arr[i])):
            if(line_arr[i][j] == 'X' and line_arr[i+1][j] == 'M' and line_arr[i+2][j] == 'A' and line_arr[i+3][j] == 'S'):
                count+=1
            if(line_arr[i][j] == 'S' and line_arr[i+1][j] == 'A' and line_arr[i+2][j] == 'M' and line_arr[i+3][j] == 'X'):
                count+=1
            if(j<len(line_arr[i])-3 and line_arr[i][j] == 'X' and line_arr[i+1][j+1] == 'M' and line_arr[i+2][j+2] == 'A' and line_arr[i+3][j+3] == 'S'):
                count+=1
            if(j<len(line_arr[i])-3 and line_arr[i][j] == 'S' and line_arr[i+1][j+1] == 'A' and line_arr[i+2][j+2] == 'M' and line_arr[i+3][j+3] == 'X' ):
                count+=1
            if(j>2 and line_arr[i][j] == 'X' and line_arr[i+1][j-1] == 'M' and line_arr[i+2][j-2] == 'A' and line_arr[i+3][j-3] == 'S'):
                count+=1
            if(j>2 and line_arr[i][j] == 'S' and line_arr[i+1][j-1] == 'A' and line_arr[i+2][j-2] == 'M' and line_arr[i+3][j-3] == 'X'):
                count+=1

    print(count)
            

if __name__ == "__main__":
    main()