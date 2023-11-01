from collections import deque


def is_valid(x, y, N):
    return 0 <= x < N and 0 <= y < N


def find_shortest_path(N, src, dest):
    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]

    visited = [[False for _ in range(N)] for _ in range(N)]

    x, y = src
    visited[x][y] = True

    queue = deque([(x, y, 0)])

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == dest:
            return dist

        for k in range(8):
            new_x, new_y = x + row[k], y + col[k]
            if is_valid(new_x, new_y, N) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, dist + 1))

    return -1
