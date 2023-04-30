def count_groups(n):
    # create list of friends for each user
    friends = {i: set() for i in range(2, n+2)}
    for i in range(2, n+2):
        for j in range(i, n+2, i):
            if i != j:
                friends[i].add(j)
                friends[j].add(i)

    # initialize parent array for union-find algorithm
    parent = {i: i for i in range(2, n+2)}

    # union-find algorithm to group users together based on friendship
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for i in range(2, n+2):
        for j in friends[i]:
            parent[find(j)] = find(i)

    # count the number of unique groups
    groups = set()
    for i in range(2, n+2):
        groups.add(find(i))
    return len(groups)


# assert count_groups(5) == 2

# assert count_groups(10) == 3


n = 5
output = count_groups(n)
print(output)  # should print 2

n = 10
output = count_groups(n)
print(output)  # should print 3





