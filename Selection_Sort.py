class SelectionSort():

    def AscSelectionSort(arr:list):
        for i in range(len(arr)-1):
            min_index=i
            for j in range(i,len(arr)):
                if arr[j]<arr[min_index]:
                    min_index=j
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr
    
    def DesSelectionSort(arr:list):
        for i in range(len(arr)-1):
            min_index=i
            for j in range(i,len(arr)):
                if arr[j]>arr[min_index]:
                    min_index=j
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr
    
    


arr=[4,3,2,1,5]
print(SelectionSort.AscSelectionSort(arr))
print(SelectionSort.DesSelectionSort(arr))
