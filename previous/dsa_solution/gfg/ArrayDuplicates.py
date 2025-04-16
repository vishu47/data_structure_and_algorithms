from typing import List

arr = [2, 3, 1, 2, 3]
# arr = [0, 3, 1, 2]


def duplicates(n: int, arr: List[int]) -> List[int]:
    seen = set()
    st = set()
    for i in arr:
        if i in seen:
            st.add(i)
        else:
            seen.add(i)
    if not st:
        return [-1]
    return list(st)


duplicates(len(arr), arr)
