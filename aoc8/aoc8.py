def main():
    with open('input.txt', "r") as f:
        lines = [list(line.strip()) for line in f]
    boundaries = (len(lines), len(lines[0]))
    part1 = set()
    part2 = set()  
    for i in range(len(lines)):
        for char1_index, char1 in enumerate(lines[i]):
            if char1 != '.':  # Skip empty spaces
                for j in range(i + 1, len(lines)):  # Only check rows below the current row
                    for char2_index, char2 in enumerate(lines[j]):
                        if char2 == char1:  # Matching characters
                            # Calculate antinodes
                            part1.update(two_antinodes(
                                (i, char1_index), 
                                (j, char2_index),
                                boundaries
                            ))
                            part2.update(more_antinodes(
                                (i, char1_index), 
                                (j, char2_index),
                                boundaries
                            ))
    print(f"Part 1: {len(part1)}\nPart 2: {len(part2)}")

def two_antinodes(coord1, coord2, fboundaries):
    antinodes = set()
    antinode1 = (2 * coord1[0] - coord2[0], 2 * coord1[1] - coord2[1])
    antinode2 = (2 * coord2[0] - coord1[0], 2 * coord2[1] - coord1[1])
    if 0 <= antinode1[0] < fboundaries[0] and 0 <= antinode1[1] < fboundaries[1]:
        antinodes.add(antinode1)
    if 0 <= antinode2[0] < fboundaries[0] and 0 <= antinode2[1] < fboundaries[1]:
        antinodes.add(antinode2)
    return antinodes

def more_antinodes(coord1, coord2, fboundaries):
    antinodes = set()
    x1, y1 = coord1
    x2, y2 = coord2

    distance_x = x2-x1
    distance_y = y2-y1

    for k in range(1, max(fboundaries)):
        antinode1 = (x1 + k * distance_x, y1 + k * distance_y)
        antinode2 = (x2 - k * distance_x, y2 - k * distance_y)
        if 0 <= antinode1[0] < fboundaries[0] and 0 <= antinode1[1] < fboundaries[1]:
            antinodes.add(antinode1)
        if 0 <= antinode2[0] < fboundaries[0] and 0 <= antinode2[1] < fboundaries[1]:
            antinodes.add(antinode2)
    return antinodes

if __name__ == '__main__':
    main()
