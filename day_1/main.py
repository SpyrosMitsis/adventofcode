from collections import defaultdict

ls = []

with open("data/input", "r") as file:
    for i in file:
        num1, num2 = i.split("   ")
        num1 = int(num1)
        num2 = int(num2)
        ls.append([num1, num2])

print(len(ls))

transposed = list(zip(*ls))
sorted_transposed = [sorted(col) for col in transposed]
sorted_ls = list(zip(*sorted_transposed))


sum_of_dist = 0
print(len(sorted_ls))
for i in sorted_ls:
    if i[0] > i[1]:
        sum_of_dist += i[0] - i[1]
    else:
        sum_of_dist += i[1] - i[0]



hash_map = defaultdict(int)

right_column = [pair[1] for pair in ls]

hash_map = {i: right_column.count(i) for i, _ in ls}


sum_of_error = 0
for i, j in hash_map.items():
    prod = i * j
    sum_of_error += prod


print(f"the sum of sum_of_error")

