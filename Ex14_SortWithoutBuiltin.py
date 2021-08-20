# method one (Without sort method)
# Also look at sorting algorithme
from ColorText import color

def Printer(li, i, j):
  for item in li: print(color(50, 250, 100, item), end=", ") if item == i or item == j else print(item, end=", ")
  print()

def MySorter(list_, reverse=False):
  # if reverse:
  #   for i in range(len(list_)):
  #     for j in range(len(list_)):
  #       if list_[j] < list_[i]: list_[j], list_[i] = list_[i], list_[j]
  #   return list_

  for i in range(len(list_)):
      print(f"Round: {i}")
      for j in range(len(list_)):
          if list_[j] > list_[i]: 
            list_[j], list_[i] = list_[i], list_[j]
            Printer(list_, list_[i], list_[j])
  return list_


sam_li = [2, 7, 8, 9, 5, 6, 1, 3]
MySorter(sam_li)
