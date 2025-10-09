class Solution:
    def floydWarshall(self, graph):
        n = len(graph)
        dist = [[graph[i][j] for j in range(n)] for i in range(n)]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist