"""
给一个tree 和其中3个特殊node， node 之间的距离就是 node 之间 edges 的数量
求tree 中 有几个 node， 它到 三个 特殊node 的距离可以形成勾股数
"""
from collections import defaultdict, deque
def pythagoream_triples(nums_of_nodes, tree_edges, tree_from, tree_to, x,y,z):
    graphic = defaultdict(list)
    for i in range(len(tree_from)):
        a, b = tree_from[i], tree_to[i]
        graphic[a].append(b)
        graphic[b].append(a)
    print(graphic)

    dist_to_x = defaultdict(int)
    dist_to_y = defaultdict(int)
    dist_to_z = defaultdict(int)

    def _calc_all_distance(start, dist_holder):
        level = 0
        visited = set()
        bfs_stack =deque([start])

        while bfs_stack:
            for _ in range(len(bfs_stack)):
                curr = bfs_stack.popleft()
                dist_holder[curr] = level
                visited.add(curr)
                for neighbor in graphic[curr]:
                    if neighbor not in visited:
                        bfs_stack.append(neighbor)
            level += 1
        return

    _calc_all_distance(x, dist_to_x)
    _calc_all_distance(y, dist_to_y)
    _calc_all_distance(z, dist_to_z)
    print(dist_to_x)
    print(dist_to_y)
    print(dist_to_z)

    res = 0
    for i in range(nums_of_nodes):
        if dist_to_x[i] **2 + dist_to_y[i] ** 2 == dist_to_z[i] ** 2:
            print("we find one", i)
            res += 1

    return res

print(pythagoream_triples(10,9,[0,0,1,1,3,3,5,7,8],[4,1,2,3,5,7,6,8,9],4,6,9))

    
    