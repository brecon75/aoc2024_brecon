def main():
    with open('input.txt', "r") as f:
        data = [int(x) for x in list(f.readline())]
    disk = [int(i/2) if i%2 == 0 else '.' for i in range(len(data)) for _ in range(data[i])]
    start_swaps(disk)
    checksum = sum(i * disk[i] for i in range(len(disk)) if disk[i] != "." )
    print("Checksum:", checksum)

def start_swaps(fdisk):
    back = len(fdisk) - 1
    while True:
        id = None
        from_indicies = []
        to_indicies = []
        while back >= 0:
            item = fdisk[back]
            if item != '.' and (id is None or id == item):
                id = item
                from_indicies.append(back)
                back -= 1
            elif item == '.' and len(from_indicies) == 0:
                back -= 1
            else:
                break

        front = 0

        while front <= back:
            item = fdisk[front]
            if item == '.':
                to_indicies.append(front)
                if len(to_indicies) == len(from_indicies):
                    for a, b in zip(from_indicies, to_indicies):
                        fdisk[a], fdisk[b] = fdisk[b], fdisk[a]
                    break
            else:
                to_indicies = []
            front += 1

        if back < 0:
            break


if __name__ == '__main__':
    main()