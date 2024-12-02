ls = []

with open("input", "r") as file:
    for i in file:
        ls.append([int(item) for item in i.split(" ")])




def is_monotonic(ls: list) -> int:
    count = 0 

    for item in ls:
        increasing = True
        decreasing = True

        for i in range(len(item) - 1):
            difference = abs(item[i] - item[i + 1] )
            if difference < 1 or difference > 3:
                increasing = False
                decreasing = False
                break

            if item[i] > item[i + 1]:
                decreasing = False

            if item[i] < item[i+ 1]:
                increasing = False


        if increasing or decreasing:
            count += 1
    return count
                

def is_monotonic_with_dampener(ls: list) -> int:

    count = 0
    for row in ls:
        if is_monotonic([row]) == 1:
            count += 1
            continue
    
        for j in range(0, len(row)):
            new_row = row[:j] +  row[j + 1 :]
            is_mon = is_monotonic([new_row]) == 1
            if is_mon: 
                count +=1
                break
    return count
    

print(is_monotonic(ls))
print(is_monotonic_with_dampener(ls))

