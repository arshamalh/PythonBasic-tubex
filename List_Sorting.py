# method one
sam_li = [2, 7, 8, 12, 5, 6, 1, 3]
for i in range(len(sam_li)):
    for j in range(len(sam_li)):
        if sam_li[j] > sam_li[i]:
            temp = sam_li[j]
            sam_li[j] = sam_li[i]
            sam_li[i] = temp
        print(sam_li, '\n')
print(sam_li)

# method two
print('method two:')
sam_li2 = [2, 7, 8, 12, 5, 6, 1, 3]
sam_li2.sort()
print(sam_li2)
