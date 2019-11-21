# Binary Search Tree 流程圖及學習歷程
## insert

insert的時候如果遇到重複值該怎麼辦？
基本上不能破壞原本的結構，但如果有重複值，需要放在離root最近的地方。

insert流程圖
![image]()

## delete

一開始看到刪除的時候沒有想太多，覺得直接刪除就好，後來想想有分三種類型。
  * if no child : 可以直接刪除。
  
  * if 1 child ： child直接與上面連接。
  
  * if 2 children ：先找self.right，再找self.right.left，將self.right.left換到被delete的位置。
   但又有一個問題，如果沒有self.right.left怎麼辦？只好將self.left換到被delete的位置，即可完成。
   
## search


## modify
