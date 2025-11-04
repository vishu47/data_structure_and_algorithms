def MergeToSortedArray(arr, low ,mid , high):
    c = []
    left = low
    right = mid+1
    
    while left <= mid and high >= right:
        print(arr[left], arr[right], 'ccc')
        if arr[left] <= arr[right]:
            c.append(arr[left])
            left+=1
        else:
            c.append(arr[right])
            right+=1
            
    while left <= mid:
        c.append(arr[left])
        left+=1
        
    while right <= high:
        c.append(arr[right])
        right+=1

    
    # replace the sorted array in to original array
    arr[low : high + 1] = c
            

def MergeSort(arr, low , high):
    print(low,high)
    # recursion base case
    # if single element is there
    if low == high:
        return
    
    mid = (low + high) // 2
    MergeSort(arr , low , mid)
    MergeSort(arr , mid + 1 , high)
    MergeToSortedArray(arr , low , mid , high)
    



a = [70,50,90,30]
print(MergeSort(a , 0 , len(a) - 1))