def inp_out(inou, output=0):
    inputlist = []
    if inou == 'in':
        cond = input('How many students do you have? ')
        for i in range(int(cond)):
            inputlist.append(input('please enter student code: '))
    elif inou == 'out':
        for i in output:
            print(i)
    return inputlist
def sorter(list_to_sort):
    numeric_list = [int(a) for a in list_to_sort]
    numeric_list.sort()
    return [str(a) for a in numeric_list]

inp_out('out', sorter(inp_out('in')))
