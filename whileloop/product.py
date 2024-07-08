def ProductOfNumbers(num: int) -> int:
    prod = 1
    i = 1
    while i <= num:
        prod = prod * i
        i += 1

    return prod


print(ProductOfNumbers(5))
# print("Vishnu")
