def tower_of_hanoi(num, source, temp, target):
    if num == 1:
        print(f"move disk 1 from {source} to {target}")
        return

    tower_of_hanoi(num-1, source, target, temp)
    print(f"move disk {num} from {source} to {target}")
    tower_of_hanoi(num-1, temp, target, source)


num = int(input("enter number of disks: "))
tower_of_hanoi(num, 'a', 'b', 'c')
