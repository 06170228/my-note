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

![image](https://github.com/06170228/my-note/blob/master/Image/dijkstra%20.png)

## Kruska

設連通網N=(V,{E})，令最小生成樹

（1）初始狀態為只有n個頂點而無邊的非連通圖T=(V,{NULL})，每個頂點自成一個連通分量

（2）在E中選取代價最小的邊，若該邊依附的頂點落在T中不同的連通分量上，則將此邊加入到T中；否則，捨去此邊，選取下一條代價最小的邊

（3）依此類推，直至T中所有頂點都在同一連通分量上為止

![image](https://github.com/06170228/my-note/blob/master/Image/Kruskal.png)

## Shortest Path 流程圖

![image]()
