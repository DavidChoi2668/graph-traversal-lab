from collections import deque

def bfs_shortest_path(graph: dict, start, goal):
    q = deque([(start, [start])])
    seen = {start}
    while q:
        node, path = q.popleft()
        if node == goal:
            return path
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, path + [nxt]))
    return None

if __name__ == "__main__":
    g = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    print(bfs_shortest_path(g, "A", "D"))
