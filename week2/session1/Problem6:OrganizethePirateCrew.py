# Captain Blackbeard needs to organize his pirate crew into different groups for a treasure hunt. Each pirate has a unique ID from 0 to n - 1.

# You are given an integer array group_sizes, where group_sizes[i] is the size of the group that pirate i should be in. For example, if group_sizes[1] = 3, then pirate 1 must be in a group of size 3.

# Return a list of groups such that each pirate i is in a group of size group_sizes[i].

# Each pirate should appear in exactly one group, and every pirate must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.


def organize_pirate_crew(group_sizes):
    freq_map = {}
    for i in range(len(group_sizes) ):
        if group_sizes[i] not in freq_map:
            freq_map[group_sizes[i]] = [i]
        else:
            freq_map[group_sizes[i]].append(i)
    # print(freq_map)
    res = []
    for k, v in freq_map.items():
        while len(v)!=0:
            res.append(v[0:k])
            v = v[k:]
            
    return res

# Example Usage:

group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2))
# Example Output:

# [[5], [0, 1, 2], [3, 4, 6]]
# [[1], [0, 5], [2, 3, 4]]
