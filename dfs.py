

def dfs(graph, start, target, visited=None):
    if visited is None:
        visited = set()
    if start == target:
        return True
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    return False


if __name__ == "__main__":
    # Graph represented as adjacency list
    graph = {
        1: [2, 3],
        2: [4],
        3: [5],
        4: [],
        5: []
    }

    start_node = 1
    target_node = 5

    if dfs(graph, start_node, target_node):
        print(f"Element {target_node} found starting from node {start_node}.")
    else:
        print(f"Element {target_node} NOT found starting from node {start_node}.")
