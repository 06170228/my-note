# Heap sort

## 最大堆積(Max Heap):父節點的值大於子節點，樹根(root)一定最所有節點的最大值
![image](https://github.com/06170228/my-note/blob/master/Image/max%20heap.png)

## 最小堆積(Min Heap):父節點的值小於子節點，樹根(root)一定最所有節點的最小值
![image](https://github.com/06170228/my-note/blob/master/Image/min%20heap.png)

其實一開始看到heap sort的影片根本看不懂，一直交換來交換去><後來看文字及圖片解說才比較懂
## Heap Sort流程圖]
![image](https://github.com/06170228/my-note/blob/master/Image/Heap%20Sort%E6%B5%81%E7%A8%8B%E5%9C%96.jpg)

又是困難的心路歷程。。。。。好想哭

我要從何下手ㄋ(◞‸◟)
![image](https://github.com/06170228/my-note/blob/master/Image/heap%20sort%E6%AD%B7%E7%A8%8B%E3%84%A7.png)
![image](https://github.com/06170228/my-note/blob/master/Image/heap%20sort%20%E6%AD%B7%E7%A8%8B%E4%BA%8C.png)
又是一堆錯誤....◢▆▅▄▃崩╰(〒皿〒)╯潰▃▄▅▇◣

後來發現錯誤在於少了"heapify(arr, n, largest)"這行，再次確認下面的節點

參考資料： [堆積排序法](http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html)
