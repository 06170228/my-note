```
class Solution():
    def merge(self, arr, left, middle, right): #類別(class)內的函式須先加self

        numleft = middle-left+1 #計算分割後 左串列的數量
        numright = right-middle #計算分割後 右串列的數量
        
        L = arr[left:left+numleft] #提取原串列 左串列索引數值
        R = arr[middle+1:middle+1+numright] #同上 右串列索引數值

        i = 0 #初始化 i j m
        j = 0
        m = left
        while i < numleft and j < numright: #當i 和 j皆在串列範圍值時
            if L[i] <= R[j]: #左串列i 小於等於 右串列j
                arr[m] = L[i] #將左串列值 更新於原串列排序
                i += 1     #移動左串引 i列索
                m += 1     #移動原串列索引 m
            else:          # 左串列i 大於 右串列j
                arr[m] = R[j]    # 將右串列值 更新於原串列排序
                j += 1      #移動左串引 i列索
                m += 1      #移動原串列索引 m
        while j < numright: #當左串列i超出範圍 則左串列整理完畢
            arr[m] = R[j]   #將剩餘右串列值 更新於原串列
            m += 1
            j += 1
        while i < numleft: #同上 反之
            arr[m] = L[i]
            m += 1
            i += 1


    def merge_sort(self, arr, left, right):
        if left < right: #右索引值 大於 左索引值

            middle = int((left+right)/2)   #取串列中間索引值
            Solution().merge_sort(arr, left, middle) #再次分割串列 形成左串列
            Solution().merge_sort(arr, middle+1, right) #同上 形成右串列
            Solution().merge(arr, left, middle, right) #合併並排序



a = [3, 5, -3, 4, 8]
n = len(a)
Solution().merge_sort(a, 0, n-1)

print(a)


