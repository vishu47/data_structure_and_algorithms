marks = {
    "history": 78,
    "hindi": 43,
}


marks["history"] = 990
marks["english"] = 99
print(marks)

marks.update({"math": 90})
marks.update({"english": 0})
print(marks)
marks.update({"mm": 0, "nn": 0})
print(marks)


# del marks["history"]
# print(marks)


# membership operators
print(43 in marks)  # search by keys so value will not search
print("history" in marks)  # true
print("historyi" in marks)  # false
