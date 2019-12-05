# Hash Table
## Hash function 
Hash Table希望能夠將存放資料的「Table」的大小(size)降到「真正會存放進Table的資料的數量」，也就是「有用到的Key的數量」：

* 若有用到的Key之數量為n，Table的大小為m，那麼目標就是m=Θ(n)。
要達到這個目標，必須引入Hash Function，將Key對應到符合Table大小m的範圍內，index=h(Key)，即可成為Hash Table的index。

觀念圖
![image]()
