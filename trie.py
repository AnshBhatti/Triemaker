layers = {}
trie = {}
leaf = set()
num = [0]


def add(keyword):
    nums = []
    new = True
    for i in range(len(keyword)):
        if i not in layers:
            layers[i] = {}
        if num[0] not in trie:
            trie[num[0]] = set()
        if True:
            not_found = True
            if i > 0:
                for each in trie[nums[i-1]]:
                    if layers[i][each] == keyword[i]:
                        trie[nums[i-1]].add(each)
                        nums.append(each)
                        not_found = False
                        break
            else:
                for each in layers[i]:
                    if layers[i][each] == keyword[i]:
                        nums.append(each)
                        not_found = False
                        break
            if not_found:
                layers[i][num[0]] = keyword[i]
                if i > 0:
                    trie[nums[i-1]].add(num[0])
                nums.append(num[0])
                num[0] += 1
        if i == len(keyword)-1:
            leaf.add(nums[-1])


stack = []


def remove(keyword, i, k):
    if i == 0:
        for j in range(len(stack)-1, -1, -1):
            del stack[j]
    not_found = True
    for each in layers[i]:
        if (k == None or each in trie[k]) and layers[i][each] == keyword[i]:
            not_found = False
            key = each
    if not_found:
        return False
    stack.append(key)
    if i == len(keyword)-1:
        if stack[i] in leaf:
            leaf.remove(stack[i])
        else:
            return False
        while i >= 0:
            if stack[i] not in leaf and len(trie[stack[i]]) == 0:
                trie.pop(stack[i])
                layers[i].pop(stack[i])
                if i > 0:
                    trie[stack[i-1]].remove(stack[i])
            else:
                break
            i -= 1
        return True
    else:
        return remove(keyword, i+1, key)


suggestions = []


def suggest(prefix, i, st, k):
    if i == 0:
        for j in range(len(suggestions)-1, -1, -1):
            del suggestions[j]
    if i < len(prefix):
        if i not in layers:
            return
        not_found = True
        for each in layers[i]:
            if (k == None or each in trie[k]) and layers[i][each] == prefix[i]:
                key = each
                not_found = False
        if not_found:
            return False
        suggest(prefix, i+1, st+prefix[i], key)
    else:
        if k in leaf:
            suggestions.append(st)
        if i not in layers:
            return
        for each in trie[k]:
            suggest(prefix, i+1, st+layers[i][each], each)


def check(keyword, i, key):
    not_found = True
    if i not in layers:
        return False
    for each in layers[i]:
        if (key == None or each in trie[key]) and layers[i][each] == keyword[i]:
            not_found = False
            key = each
    if not_found:
        return False
    if i == len(keyword)-1:
        print(key, leaf)
        return key in leaf
    return check(keyword, i+1, key)


def display():
    grid = [[]]
    v = set()
    maxl = [0]

    def dfs(node, i):
        if i == len(grid):
            grid.append([])
        grid[i] += ["  "]*(len(grid[i-1])-len(grid[i])-1)
        v.add(node)
        grid[i].append(layers[i][node]+' ')
        for each in trie[node]:
            if each not in v:
                dfs(each, i+1)
        m = 0
        for j in range(len(grid)):
            m = max(m, len(grid[j]))
        for j in range(len(grid)):
            while len(grid[j]) < m:
                grid[j].append("  ")
    if not layers:
        return "The trie is empty..."
    for each in layers[0]:
        dfs(each, 0)
        for i in range(len(grid)):
            grid[i].append("| ")
    out = ''
    for row in grid:
        out += ''.join(row)+'\n'
    return out
