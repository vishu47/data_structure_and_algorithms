def remove_duplicate(arr):
    # fi = []
    # for i in arr:
    #     if i not in fi:
    #         fi.append(i)
    # arr[: len(arr)] = fi

    seen = set()
    fi = []
    for i in arr:
        if i not in seen:
            fi.append(i)
            seen.add(i)
    arr[:] = fi
    return arr


a = [32, 40, 43, 60, 72, 78, 82, 82, 82, 99]
cc = remove_duplicate(a)
print(cc)
