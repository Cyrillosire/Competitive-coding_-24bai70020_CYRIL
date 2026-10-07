from collections import deque
def valid_path(n, edges, source, destination):
    adj = [[] for _ in range(n)]
    for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
    if source == destination:
        return True
    visited = [False] * n
    queue = deque([source])
    visited[source] = True
    while queue:
        node = queue.popleft()
        for nxt in adj[node]:
            if nxt == destination:
                return True
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
        return False
print(valid_path(4, [[0, 1], [2, 0], [2, 1], [1, 0]], 0, 2))