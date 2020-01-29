if __name__ == '__main__':
    n = int(input())
    list = []
    to_execute = []
    for _ in range(n):
        command, *args = input().split(' ')
        to_execute.append([command, [int(arg) for arg in args]])

    for executing in to_execute:
        command = executing[0]
        args = executing[1]
        if command == "insert":
            list.insert(args[0], args[1])
        elif command == "remove":
            list.remove(args[0])
        elif command == "append":
            list.append(args[0])
        elif command == "sort":
            list = sorted(list)
        elif command == "pop":
            list.pop()
        elif command == "reverse":
            list.reverse()
        elif command == "print":
            print(list)
