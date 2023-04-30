def count_duplicate_pairs(n, nums):
    # convert each number to binary form and compute sum of bits
    sums = [bin(num).count('1') for num in nums]

    # create dictionary that maps each sum to a list of numbers
    num_dict = {}
    for i in range(n):
        if sums[i] in num_dict:
            num_dict[sums[i]].append(nums[i])
        else:
            num_dict[sums[i]] = [nums[i]]

    # count duplicate pairs for each list of numbers with the same sum
    count = 0
    for key in num_dict:
        lst = num_dict[key]
        if len(lst) >= 2:
            count += len(lst) * (len(lst) - 1) // 2

    return count
print(count_duplicate_pairs(2, [1, 2]))
print(count_duplicate_pairs(2, [2, 3]))
