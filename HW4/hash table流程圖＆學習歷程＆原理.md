# Hash Table
## Hash function 
Hash Table希望能夠將存放資料的「Table」的大小(size)降到「真正會存放進Table的資料的數量」，也就是「有用到的Key的數量」：

* 若有用到的Key之數量為n，Table的大小為m，那麼目標就是m=Θ(n)。
要達到這個目標，必須引入Hash Function，將Key對應到符合Table大小m的範圍內，index=h(Key)，即可成為Hash Table的index。

觀念圖（這裡的index就像是一個個的抽屜，依照你的編號進入你該去的抽屜裡。）

![image](https://github.com/06170228/my-note/blob/master/Image/hash%20table%20%E8%A7%80%E5%BF%B5%E5%9C%96.png)



## Hash table 學習歷程
我們使用MD5，將一般文字轉換成一串亂碼，也就是key。key/5的餘數就是index的編號。依照編號放進去。

我這邊是不會放入相同的值，所以不會重複，刪除的時候刪除一項即可。

原本沒有想到重複值的問題，但若有重複值再刪除及查詢時很麻煩，所以改成若遇到重複值就不加入。

其中有遇到的問題在下圖：
![image](https://github.com/06170228/my-note/blob/master/Image/hash%20table%20%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B.png)

在第4、5行:

          curr = self.data[index].val

          curr.next = self.data[index].next.val
          
我的想法錯誤，導致下面while迴圈無法正常跑

應該要改為:

          curr = self.data[index]

while迴圈中也要改成下面這樣才對。

          if curr.val == key:
                return True
            else:
                curr = curr.next
         

## Hash table流程圖
![image]()
