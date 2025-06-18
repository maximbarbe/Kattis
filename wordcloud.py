from math import ceil
cloud_num = 1
while True:
    w, n = map(int, input().split(" "))
    words = []
    max_freq = 0
    if w== 0 and n == 0:
        break
    for i in range(n):
        data = input().split(" ")
        data[1] = int(data[1])
        if data[1] > max_freq:
            max_freq = data[1]
        words.append(data)
    cur_row_width = 0
    cur_row_height = 0
    total_height = 0
    for word in words:
        font_height = 8 + ceil((40*(word[1] - 4))/(max_freq - 4))
        font_width = ceil((9/16) * len(word[0]) * font_height)
        if cur_row_width + font_width<= w:
            cur_row_width += font_width + 10
            cur_row_height = max(cur_row_height, font_height)
        else:
            total_height += cur_row_height
            cur_row_width = font_width + 10
            cur_row_height= font_height
    total_height += cur_row_height
    print(f"CLOUD {cloud_num}: {total_height}")
    cloud_num += 1