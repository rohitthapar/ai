import sys
import copy

q = []
visited = []


def compare(a, b):
    if a == b:
        return 1
    else:
        return 0


def find_pos(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == -1:
                return ([i, j])


def up(s1, pos):
    row = pos[0]
    col = pos[1]
    s = copy.deepcopy(s1)
    if row == 0:
        return (s)
    else:
        s[row][col], s[row - 1][col] = s[row - 1][col], s[row][col]
        return (s)


def down(s1, pos):
    row = pos[0]
    col = pos[1]
    s = copy.deepcopy(s1)
    if row == len(s) - 1:
        return (s)
    else:
        s[row][col], s[row + 1][col] = s[row + 1][col], s[row][col]
        return (s)


def left(s1, pos):
    row = pos[0]
    col = pos[1]
    s = copy.deepcopy(s1)
    if col == 0:
        return (s)
    else:
        s[row][col], s[row][col - 1] = s[row][col - 1], s[row][col]
        return (s)


def right(s1, pos):
    row = pos[0]
    col = pos[1]
    s = copy.deepcopy(s1)
    if col == len(s[0]) - 1:
        return (s)
    else:
        s[row][col], s[row][col + 1] = s[row][col + 1], s[row][col]
        return (s)


def enqueue(new_state):
    if new_state not in visited and new_state not in q:
        q.append(new_state)


def dequeue():
    global q
    if len(q) == 0:
        print("Goal state can't be reached")
        sys.exit()
    x = q.pop(0)
    return x


def main():
    global visited
    global q
    S0 = [[1, 2, 3], [8, -1, 4], [7, 6, 5]]
    G = [[2, 8, 1], [-1, 4, 3], [7, 6, 5]]
    if (compare(S0, G) == 1):
        print("Inital and final state are same ")
        sys.exit();
    while (1):
        visited.append(S0)
        position = find_pos(S0)

        new_state = up(S0, position)
        if (compare(new_state, G)):
            print("Find")
            print(len(visited))
            sys.exit()
        enqueue(new_state)

        new_state = down(S0, position)
        if (compare(new_state, G)):
            print("Find")
            print(len(visited))
            sys.exit()
        enqueue(new_state)

        new_state = left(S0, position)
        if (compare(new_state, G)):
            print("Find")
            print(len(visited))
            sys.exit()
        enqueue(new_state)

        new_state = right(S0, position)
        if (compare(new_state, G)):
            print("Find")
            print(len(visited))
            sys.exit()
        enqueue(new_state)

        S0 = dequeue();


if _name_ == "_main_":
    main()