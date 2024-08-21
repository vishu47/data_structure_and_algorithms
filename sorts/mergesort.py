class Solution:
    def merge(self, left, right):
        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        # remaining
        while i < len(left):
            res.append(left[i])
            i += 1

        while j < len(right):
            res.append(right[j])
            j += 1

        return res

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        h1 = arr[:mid]
        h2 = arr[mid:]
        left = self.mergeSort(h1)
        right = self.mergeSort(h2)
        return self.merge(left, right)


a = [4, 1, 3, 1, 3, 4, 9, 7]
s = Solution()
cc = s.mergeSort(a)
# cc = s.merge([2, 25, 35, 45], [1, 24, 36, 47])
print(cc)
