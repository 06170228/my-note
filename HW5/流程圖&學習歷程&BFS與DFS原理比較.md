# BFS & DFS 原理
## BFS（廣度優先搜尋）

廣度優先搜尋法，是一種圖形(graph)搜索演算法。
從圖的某一節點(vertex, node)開始走訪，接著走訪此一節點所有相鄰且未拜訪過的節點，由走訪過的節點繼續進行先廣後深的搜尋。
以樹(tree)來說即把同一深度(level)的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點。
因此，進行 breadth-first search 時，需要使用 queue ，以便記錄拜訪的順序。


## DFS（深度優先搜尋）

深度優先搜尋法，是一種用來遍尋一個樹(tree)或圖(graph)的演算法。
由樹的根(或圖的某一點當成 根)來開始探尋，先探尋邊(edge)上未搜尋的一節點(vertex or node)，並儘可能深的搜索，直到該節點的所有邊上節點都已探尋；
就回溯(backtracking)到前一個節點，重覆探尋未搜尋的節點，直到找到目的節點或遍尋全部節點。
深度優先搜尋法屬於盲目搜索(uninformed search)是利用堆疊(Stack)來處理，通常以遞迴的方式呈現。


## BFS & DFS之比較
bfs會把狀態逐個加入佇列，因此通常需要與狀態數成正比的記憶體空間。再求最短路徑時比較好。
dfs使用遞迴函式程式可以簡潔地進行書寫，並且狀態管理也很簡單，所以大多數情況還是用dfs來實現相關問題。dfs是與遞迴深度成正比的。一般與狀態數相比，遞迴深度並不會太大，所以dfs更加省記憶體。

## BFS流程圖

![image](https://github.com/06170228/my-note/blob/master/Image/BFS%E6%B5%81%E7%A8%8B%E5%9C%96.png)

# BFS學習歷程


原本一開始沒有想到要寫 “if s in self.graph:”這段 ，但想到老師也有可能丟了一個根本不存在GRAPH裡面的值，所以加進去。
![image](https://github.com/06170228/my-note/blob/master/Image/BFS%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E4%B8%80.png)



其實BFS和DFS沒有差太多，在這邊看到一個是queue 另一個則是stack。一個是先進先出，另一個則是最後進的先出。
![image](https://github.com/06170228/my-note/blob/master/Image/BFS%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E4%BA%8C.png)
![image](https://github.com/06170228/my-note/blob/master/Image/BFS%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E4%B8%89.png)


## Reference
[BFS廣度優先搜尋](https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)

[DFS深度優先搜尋](http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)

與厲彥伯同學討論。
