class BubbleSort():
    def AscBubbleSort(arr:list):
        for i in range(len(arr)-1):# 1 2
            for j in range(0,len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr

    def DesBubbleSort(arr:list):
        for i in range(len(arr)-1):
            for j in range(0,len(arr)-i-1):
                if arr[j]<arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr

arr=[5,4,3,2,1,6]
print(BubbleSort.AscBubbleSort(arr))
print(BubbleSort.DesBubbleSort(arr))