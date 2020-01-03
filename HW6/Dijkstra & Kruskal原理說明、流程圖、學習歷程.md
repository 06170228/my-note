# Shortest Path 最短路徑

最短路徑之成本w(path)=δ(X,Y)：在Graph上，所有從vertex(X)出發抵達vertex(Y)的path中，具有最小weight之path，稱為最短路徑，其weight滿足：

 δ(X,Y)=min{w(path), for all path from X to Y}。
 (可能有多條path之weight皆為極小值，那麼這些path都是最短路徑。)
 
 若δ(X,Y)=∞，則表示無法從vertex(X)走到vertex(Y)。

## Dijkstra 

* 只要Graph中的edge沒有negative weight，即使有cycle，亦可使用。

* 時間複雜度，根據實現Min-Priority Queue之資料結構將有所不同。

（1）初使時令 S={V0},T={其餘頂點}，T中頂點對應的距離值

（2）若存在<V0,Vi>，為<V0,Vi>弧上的權值

（3）若不存在<V0,Vi>，為無窮

（4）從T中選取一個其距離值為最小的頂點W，加入S

（5）對T中頂點的距離值進行修改：若加進W作中間頂點，從V0到Vi的距離值比不加W的路徑要短，則修改此距離值

（6）重複上述步驟，直到S中包含所有頂點，即S=V為止

![image]()
