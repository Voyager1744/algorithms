class TreeNode:
    def __init__(self, parent, cost, company):
        self.parent = parent
        self.cost = cost
        self.company = company
        self.children = []

    def __str__(self):
        return f"({self.parent}, {self.cost}, {self.company})"


def build_tree(n, companies, descriptions):
    nodes = {}
    root = None

    for i in range(1, n + 1):
        pi, ai, ci = descriptions[i - 1]
        pi = int(pi)
        ai = int(ai)
        node = TreeNode(pi, ai, ci)

        if pi == 0:
            root = node
        else:
            parent_node = nodes[pi]
            parent_node.children.append(node)

        nodes[i] = node

    return root, nodes


n, k = map(int, input().split())
company_names = [input() for _ in range(k)]

descriptions = [list(input().split()) for _ in range(n)]

root, nodes = build_tree(n, company_names, descriptions)


def find_min_cost(root, target_companies):
    min_cost = float('inf')
    min_cost_node = None

    def dfs(node, current_set, current_cost):
        nonlocal min_cost, min_cost_node

        if not node:
            return

        current_set.add(node.company)
        current_cost += node.cost

        if current_set == target_companies:
            if current_cost < min_cost:
                min_cost = current_cost
                min_cost_node = node

        for child in node.children:
            dfs(child, set(current_set), current_cost)

    dfs(root, set(), 0)

    return min_cost if min_cost_node else -1


result = find_min_cost(root, set(company_names))
print(result)

"""
5 2
A
B
0 1 A
1 2 A
1 2 B
1 1 B
4 2 A

"""
