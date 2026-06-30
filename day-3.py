import random
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=random.choice(arr)
    left=[i for i in arr if i<pivot ]
    middle=[i for i in arr if i==pivot ]
    right=[i for i in arr if i>pivot ]
    return quicksort(left)+quicksort(middle)+quicksort(right)

arr=[3,2,15,7,9,16]
print("Before:",arr)
print("After:",quicksort(arr))

