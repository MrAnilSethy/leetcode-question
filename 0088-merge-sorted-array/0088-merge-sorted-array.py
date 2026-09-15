class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        arr = [None]*(m+n)
        i=0
        j=0
        k=0
        while(i<m and j<n):
            if nums1[i]<=nums2[j]:
                arr[k]=nums1[i]
                k+=1
                i+=1
            else:
                arr[k]=nums2[j]
                k+=1
                j+=1
        while(i<m):
                arr[k]=nums1[i]
                k+=1
                i+=1
        while(j<n):
                arr[k]=nums2[j]
                k+=1
                j+=1
        for x in range(m+n):
            nums1[x]=arr[x]


       
        