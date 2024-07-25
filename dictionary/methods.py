marks = {
    "history": 78,
    "hindi": 43,
    "sci": 22,
    "computer": 11,
    "english": 22,
    "chemistry": 33,
}

# print(marks["history"])
# print(marks.get("history"))
# print(marks.get("historyy"))  # return none
# print(marks.get("historyy", 89))  # if key not exist then return 89 or whatever you want

# marks.pop("english")
# print(marks)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 1, "d": 2}
dict3 = {"c": 1, "d": 2, "a": 8}

# dict1.update(dict2)
dict1.update(dict3)
# print(dict1)
