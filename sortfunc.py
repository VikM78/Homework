#nums = [6, 4, 7, 3, 5, 8, 9, 1, 2]
#nums1 = nums[:]
#nums2 = nums[:]
#count_ = 0


def buble_sort(ls):
    #global count_
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True
                #count_ += 1

#nums1 = nums
#buble_sort(nums1)
#print(count_)
#print(nums1)
#count_ = 0

def selection_sort(ls):
    #global count_
    for i in range(len(ls)):
        lowest = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls [lowest]:
                lowest = j
        if i < lowest:
            ls[i], ls[lowest] = ls[lowest], ls[i]
            #count_ += 1

def insertion_sort(arr):
    # Проходим по всем элементам массива, начиная со второго
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы arr[0..i - 1], которые больше ключа, на одну позицию вперёд
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key  # Вставляем ключ на правильное место
    return arr  # Возвращаем отсортированный массив


#nums2 = nums
#print(nums2)
#selection_sort(nums2)
#print(count_)
#print(nums2)