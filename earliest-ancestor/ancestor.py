from collections import defaultdict

def earliest_ancestor(ancestors, vertex):
    # 1. create a dict of {child: parents_list}
    child_parent = defaultdict(list)

    for parent, child in ancestors:
        child_parent[child].append(parent)

    # 2. if child has many parents, pick smallest one and iteratively find its parent
    if vertex in child_parent.keys():
        while child_parent[vertex]:
            vertex = min(child_parent[vertex])
        return vertex
    else:
        return -1
    

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(ancestors, 2))