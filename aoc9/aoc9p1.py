def main():
    with open('input.txt', "r") as f:
        data = [int(x) for x in list(f.readline())]
    disk = [int(i/2) if i%2 == 0 else "." for i in range(len(data)) for _ in range(data[i])]
    start_swaps(disk)
    checksum = sum(i * disk[i] for i in range(len(disk)) if disk[i] != "." )
    print("Checksum:", checksum)

def start_swaps(fdisk):
    for i in range(len(fdisk)):
        swapped = False
        if fdisk[i] == ".":
            for j in range(len(fdisk) - 1, -1, -1):
                if fdisk[j] != "." and j > i:
                    swapped = True
                    fdisk[i], fdisk[j] = fdisk[j], fdisk[i]
                    break
            if not swapped:
                return

if __name__ == '__main__':
    main()