# Hash Table
## Hash function 
Hash Table希望能夠將存放資料的「Table」的大小(size)降到「真正會存放進Table的資料的數量」，也就是「有用到的Key的數量」：

* 若有用到的Key之數量為n，Table的大小為m，那麼目標就是m=Θ(n)。
要達到這個目標，必須引入Hash Function，將Key對應到符合Table大小m的範圍內，index=h(Key)，即可成為Hash Table的index。

觀念圖

![image](https://github.com/06170228/my-note/blob/master/Image/hash%20table%20%E8%A7%80%E5%BF%B5%E5%9C%96.png)

這裡的index就像是一個個的抽屜，依照你的編號進入你該去的抽屜裡。
我們使用MD5，將一般文字轉換成一串亂碼
