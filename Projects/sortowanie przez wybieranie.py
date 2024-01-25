def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

#def bubble_sort(arr):
#    n = len(arr)
#    for i in range(n):
#        for j in range(n):
#            if arr[i] > arr[i+1]
#                arr[i], arr[i+1] = arr[i+1], arr[i]

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Posortowana lista:", arr)

zez = [10, 8, 4, 2, 1]
n = len(zez)
swapped = True
licznik = 0
while swapped == True:
    for i in range(n - 1):
        print("licze")
        for j in range(0, n - 1 - i):
            if zez[j] > zez[j + 1]:
                zez[j], zez[j + 1] = zez[j + 1], zez[j]
                swapped = True
                print("licze")
            else:
                swapped = False
print(zez)

