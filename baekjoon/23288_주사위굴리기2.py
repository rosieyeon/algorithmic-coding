from collections import deque

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dice = {'top': 1, 'bottom': 6, 'front': 5, 'back': 2, 'right': 3, 'left': 4}
answer = 0
# visited = [[0]*m for _ in range(n)]
# visited[0][0] = 1


# 90도 회전 고려해서 동-남-서-북 순서로 지정
def rotate_dice(d):
    if d == 0:  # 동쪽으로
        dice['top'], dice['right'], dice['left'], dice['bottom'] = dice['left'], dice['top'], dice['bottom'], dice['right']
    elif d == 1:  # 남쪽으로
        dice['top'], dice['front'], dice['bottom'], dice['back'] = dice['back'], dice['top'], dice['front'], dice['bottom']
    elif d == 2:  # 서쪽으로
        dice['top'], dice['right'], dice['left'], dice['bottom'] = dice['right'], dice['bottom'], dice['top'], dice['left']
    elif d == 3:  # 북쪽으로
        dice['top'], dice['front'], dice['bottom'], dice['back'] = dice['front'], dice['bottom'], dice['back'], dice['top']


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y, b):
    q = deque()
    q.append([x, y])
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == b and not visited[nx][ny]:
                visited[nx][ny] = 1
                cnt += 1
                q.append([nx, ny])
    return cnt * b


def move_dice(k):
    global answer
    q = [[0, 0, 0]]
    for _ in range(k):
        x, y, d = q.pop()
        nx = x + dx[d]
        ny = y + dy[d]

        # 지도에서 벗어난 경우에는 반대방향으로 회전함
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            d = (d+2) % 4
            nx = x + dx[d]
            ny = y + dy[d]

        rotate_dice(d)
        answer += bfs(nx, ny, arr[nx][ny])

        if dice['bottom'] > arr[nx][ny]:
            d = (d+1) % 4
        if dice['bottom'] < arr[nx][ny]:
            d = (d-1) % 4
        if dice['bottom'] == arr[nx][ny]:
            d = d
        q.append([nx, ny, d])


move_dice(k)
print(answer)
