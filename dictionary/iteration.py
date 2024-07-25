my_dict = {
    "name": "Anirudh",
    "age": 18,
    "gender": "Male",
    100: 200,
    "name": "Xyz",
    2: 100,
}
marks = {
    "history": 78,
    "hindi": 43,
    "sci": 22,
    "computer": 11,
    "english": 22,
    "chemistry": 33,
}

# for k in marks:
#     print(f"{k} : {marks[k]}")


total = 0
for k in marks:
    total += marks[k]

print(max, k)
max = 0
for k in marks:
    if marks[k] >= max:
        max = marks[k]
        name = k


print(max, k)
