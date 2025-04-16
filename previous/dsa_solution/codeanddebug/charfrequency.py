def charFreq():
    st = "nkwefhwefwefwefhkfjkjkjjkhkjytuybmfnew"
    h = {}
    for ch in st:
        h[ch] = h.get(ch, 0) + 1

    for c in h:
        print(f"{c} : {h[c]}")


charFreq()
