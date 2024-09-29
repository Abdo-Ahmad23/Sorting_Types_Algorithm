class Insertionsort():

    def AscInsertionSort(arr:list):

        for i in range(1,len(arr)):
            key = arr[i]
            j = i - 1
            while j>=0 and key<arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1]=key
        return arr

    def DesInsertionSort(arr:list):
        
        for i in range(1,len(arr)):
            key = arr[i]
            j = i - 1
            while j>=0 and key>arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1]=key
        return arr



arr = [1,2,3,5,4,3,6]
print(Insertionsort.AscInsertionSort(arr))

print(Insertionsort.DesInsertionSort(arr))
