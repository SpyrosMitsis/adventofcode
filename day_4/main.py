input_data = """
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


input_data = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""

    # if input_data[i:i+4] == 'XMAS' or input_data[i-4: i] == 'XMAS':
    # print(f"forward {input_data[i: i + 4]}", end=" ")
    # print(f"backwards {input_data[i - 4: i]} {i}")

input_data = open('input').read()

count = 0
target = "XMAS"
t_length = len(target)

input_data = [i.strip() for i in input_data.strip().split("\n")]



for i in range(len(input_data)):
    for j in range(len(input_data[0])):
        if (input_data[i][j: j + t_length] == target) | (input_data[i][j: j + t_length] == target[::-1]):
            count += 1

        if i + t_length <= len(input_data):
            vertical = ''.join(input_data[k][j] for k in range(i, i + t_length))
            if vertical == target or vertical == target[::-1]:
                count += 1
        


        if i + t_length <= len(input_data) and j + t_length <= len(input_data[0]):
            forward_diag = ''.join(input_data[i + k][j + k] for k in range(t_length))
            if forward_diag == target or forward_diag == target[::-1]:
                count += 1

        # Backward diagonal check (top-right to bottom-left)
        if i + t_length <= len(input_data) and j - t_length + 1 >= 0:
            backward_diag = ''.join(input_data[i + k][j - k] for k in range(t_length))
            if backward_diag == target or backward_diag == target[::-1]:
                count += 1


new_target = "MAS"
new_t_length = len(new_target)

x_mas_count = 0

counter = 0
for i in range(1, len(input_data) - 1):
    for j in range(1, len(input_data[0]) - 1):
        if input_data[i][j] != 'A':
            continue
        try:
            forward_diag = ''.join(input_data[i + k - 1][j + k - 1] for k in range(new_t_length))
            backward_diag = ''.join(input_data[i + k - 1][j - k + 1] for k in range(new_t_length))
            if (forward_diag == new_target or forward_diag == new_target[::-1]) and \
                (backward_diag == new_target or backward_diag == new_target[::-1]):
                x_mas_count += 1
        except IndexError:
            pass

print(x_mas_count)

