import time

def main():
    start_time = time.time()
    
    with open("input.txt", "r") as file:
        line_arr = [list(line.strip()) for line in file]

    boundaries = (len(line_arr), len(line_arr[0]))
    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    for i in range(boundaries[0]):
        for j in range(boundaries[1]):
            if line_arr[i][j] == "^":
                start = (i,j)
                break

    part1_positions = get_visited_positions(start, line_arr, boundaries, directions)
    part1 = len(part1_positions)
    print(f"Part 1: {part1}")
    
    part2 = 0
    
    for pos in part1_positions:
        line_arr[pos[0]][pos[1]] = "#"  # add new obstruction
        if get_visited_positions(start, line_arr, boundaries, directions) == {start}:
            part2 += 1
        line_arr[pos[0]][pos[1]] = "."

    print(f"Part 2: {part2}")
    
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Runtime: {runtime:.3f} seconds")


def get_visited_positions(fstart, fline_arr, fboundaries, fdirections):
    current_pos = fstart
    current_direction = fdirections[0]
    next = (current_pos[0] + current_direction[0], current_pos[1] + current_direction[1])
    fvisited_positions = set()  # using a set ensures duplicates are not added, as a position can be visited multiple times
    fvisited_positions.add(current_pos)
    visited_states = set()
    dir_id = 0

    while 0 <= next[0] < fboundaries[0] and 0 <= next[1] < fboundaries[1]:
        state = (current_pos, dir_id)
        if state in visited_states:
            return {fstart}
        visited_states.add(state)
        
        if fline_arr[next[0]][next[1]] == "#":
            dir_id = (dir_id + 1) % 4
            current_direction = fdirections[dir_id]
        else:
            current_pos = next
            fvisited_positions.add(current_pos)
        next = (current_pos[0] + current_direction[0], current_pos[1] + current_direction[1])

    return fvisited_positions

if __name__ == "__main__":
    main()