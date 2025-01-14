문제 1. 음료수 얼려먹기 문제
   N x M 크기의 얼음 틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 
   구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어잇는 경우 서로 연결되어 있는 것으로 간주한다. 
   이때 얼음틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 

n, m = map(int, input().split())
result = 0 # 아이스크림 개수
graph = []
for i in range(n):
  graph.append(list(map(int, input()))) # 2차원 리스트의 맵 정보입력받기 

def dfs(x,y):
  if x <= -1 or x>=n or y<=-1 or y >= m:
    return False #주어진 범위가 아닌경우
  if graph[x][y]==0: # 현재 노드를 방문하지 않음. 
    graph[x][y]=1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1) #상하좌우 호출, 연결된 모든 노드 방문처리
    return True
  return False

#아이스크림 개수 구하기 
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result += 1 
print(result)


문제 2. 미로탈출
   N x M 크기의 직사각형 형태의 미로에 갇혔다. 미로에는 여러마리의 괴물이 있어 이를 피해 탈출 해야한다. 
   동빈이의 위치는 (1,1)이며 미로 출구는 (N,M)의 위치에 존재하며 한번에 한칸씩 이동할 수 있다. 
   이때 괴물이 있는 부분은 0으로 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다.
   동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하여라. 칸을 셀때는 시작칸과 마지막 칸을 모두 포함해서 계산한다. 
   
from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))



