import matplotlib.pyplot as plt

def mergeSort(list):
    if (
        len(list) > 1
        and not len(list) < 1
        and len(list) != 0
    ):
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        mergeSort(left)
        mergeSort(right)

        left_index = 0
        right_index = 0
        i = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                list[i] = left[left_index]
                left_index += 1
            else:
                list[i] = right[right_index]
                right_index += 1
            i += 1

        while left_index < len(left):
            list[i] = left[left_index]
            left_index += 1
            i += 1

        while right_index < len(right):
            list[i] = right[right_index]
            right_index += 1
            i += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
