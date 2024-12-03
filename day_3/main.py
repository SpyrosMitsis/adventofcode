import re


with open("input", "r") as buffer:
    input_data = buffer.read().rstrip()



def mul(s: str) -> int:

    matches = re.findall(r"mul\(\d+,\s*\d+\)", input_data)
    sum = 0

    for i in matches:
        numbers = (re.findall(r"\((\d+),\s*(\d+)\)",i))

        numbers = tuple(map(int, numbers[0]))
        sum += numbers[0] * numbers[1]

    return sum


def mul_with_conditionals(s: str) -> int:

    matches = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\s*\d+\)", input_data)
    sum = 0
    enabled = True


    for i in matches:

        if i == "do()":
            enabled = True
            continue
        elif i == "don't()":
            enabled = False
            continue
            
        if enabled:
            numbers = (re.findall(r"\((\d+),\s*(\d+)\)",i))
            numbers = tuple(map(int, numbers[0]))
            sum += numbers[0] * numbers[1]

    return sum


print(mul(input_data))
print(mul_with_conditionals(input_data))

