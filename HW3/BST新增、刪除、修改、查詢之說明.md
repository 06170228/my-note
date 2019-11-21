# Binary Search Tree

## Insert(新增)

函式InsertBST()的概念，可以視為Search()的延伸：
1. 根據BST對Key之規則，先找到將要新增之node「適合的位置」

2. 再將欲新增的node接上BST。


## Delete(刪除)

要在BST上執行刪除資料(被刪除的node稱為A)，必須讓刪除A後的BST仍然維持BST的性質。因此，所有「具有指向A的pointer」之node(也就是A的parent、leftchild以及rightchild)都必須調整該pointer，使其指向新的記憶體位置。

刪除資料的工作，根據欲刪除之node「有幾個child pointer」分成三類：

1. Case1：欲刪除之node沒有child pointer

2. Case2：欲刪除之node只有一個child pointer(不論是leftchild或rightchild)

3. Case3：欲刪除之node有兩個child pointer。


## Modify(修改)

先看欲修改目標的值，必須小於跟節點與大於左子數，才可以直接修改。

其餘情況，直接delete數值，再新insert的值。

## Search(查詢)

BST的Search()操作，便是根據BST的特徵：Key(L)<Key(Current)<Key(R)，判斷Current應該往left subtree走，還是往right subtree走。
