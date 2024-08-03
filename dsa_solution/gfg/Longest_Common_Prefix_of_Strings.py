def longestCommonPrefix(arr):
    # print("str"[:3], "mm")
    init = arr[0]
    for str in arr:
        # print(str, "str")
        while str[: len(init)] != init and init:
            init = init[: len(init) - 1]
            # print(init)

    if not init:
        return -1

    return init


a = ["geeksforgeeks", "geeks", "geek", "geezer"]
cc = longestCommonPrefix(a)
print(cc, "cc")

# Initial State
# Input array: ["flower", "flow", "flight"]
# Initial prefix: "flower"

# Iteration 1 (Compare with "flower")
# Current prefix: "flower"
# Current string: "flower"
# Since the current string is the same as the current prefix, no changes are needed.
# Updated prefix: "flower"
# Iteration 2 (Compare with "flow")
# Current prefix: "flower"
# Current string: "flow"
# "flow" does not start with "flower", so we shorten the prefix to "flowe".
# "flow" does not start with "flowe", so we shorten the prefix to "flow".
# "flow" starts with "flow".
# Updated prefix: "flow"
# Iteration 3 (Compare with "flight")
# Current prefix: "flow"
# Current string: "flight"
# "flight" does not start with "flow", so we shorten the prefix to "flo".
# "flight" does not start with "flo", so we shorten the prefix to "fl".
# "flight" starts with "fl".
# Updated prefix: "fl"
# Final State
# The loop is completed.
# The longest common prefix is "fl".
# Now, let's do a dry run of the function with the example arr2 = ["dog", "racecar", "car"].
