def solution(n, wires):
    tree = [[] for _ in range(n + 1)]

    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)

    visited = [False] * (n + 1)
    child = [0] * (n + 1)

    """각자의 자식 개수 구하기"""
    def dfs(node):
        visited[node] = True

        for next in tree[node]:
            if not visited[next]:
                child[node] += dfs(next) + child[next]

        return 1

    dfs(1)
    result = n

    for c in child:
        result = min(result, abs(n - 2 * (c + 1)))

    return result

if __name__ == '__main__':
    n = 9
    wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    print(solution(n,wires))