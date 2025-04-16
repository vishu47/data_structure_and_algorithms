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

# print(marks.keys())

# for k in marks.keys():
#     print(k)
#     print(marks[k])


# for k in marks.values():
#     print(k)


x = marks.items()
print(x)
# set like object and not indexing elements
# print(x[0])
# dict_items([('history', 78), ('hindi', 43), ('sci', 22), ('computer', 11), ('english', 22), ('chemistry', 33)])


# for key, value in x:
#     print(f"{key}: {value}")


for item in x:
    key, value = item
    print(f"{key}: {value}")
