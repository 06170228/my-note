# Binary Search Tree 流程圖及學習歷程
## insert

insert的時候如果遇到重複值該怎麼辦？
基本上不能破壞原本的結構，但如果有重複值，需要放在離root最近的地方。

insert流程圖
![image](https://github.com/06170228/my-note/blob/master/Image/BST_insert%E6%B5%81%E7%A8%8B%E5%9C%96.jpg)

## delete

一開始看到刪除的時候沒有想太多，覺得直接刪除就好，後來想想有分三種類型。
  * if no child : 可以直接刪除。
  
  * if 1 child ： child直接與上面連接。
  
  * if 2 children ：<情況一>選擇5，先找self.right也就是8，再找self.right.left也就是7，將self.right.left換到被delete的位置。
   但又有一個問題，如果沒有self.right.left怎麼辦？<情況二>如果選擇8被delete，沒有self.right.left，只好將self.left也就是7，換到被delete的位置，即可完成。

delete流程圖
![image](https://github.com/06170228/my-note/blob/master/Image/BST_delete%E6%B5%81%E7%A8%8B%E5%9C%96.jpg)

## search


## modify
