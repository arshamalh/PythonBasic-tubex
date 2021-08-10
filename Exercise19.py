def element_search(li, num):
    li = list(set(li))
    print(li)
    center = 1
    while center != 0:
        center = len(li) // 2
        print(f"center index is: {center}")
        if li[center] == num:
            print(f'{num} is in the list')
            break
        elif li[center] > num:
            li = li[:center]
            print(f'cut list is: {li}')
        elif li[center] < num:
            li = li[center + 1:]
            print(f'cut list is: {li}')
    else:
        print("the number isn't in the list")


# there are lot's of methods for receiving a list
# I've just told one of them, try others by yourself
inp_list = input('Enter a list: ').split(' ')
managed_list = []
for x in inp_list:
    if x.isdigit():
        managed_list.append(int(x))
del inp_list
element_search(managed_list, int(input('enter a number: ')))


"""
another method:
inp_list = []
try:
    while True:
        inp_list.append(int(input(f'the {len(inp_list)} of your list: ')))
except:
    pass
print(inp_list)
"""