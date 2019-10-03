# 7. Reverse Integer
```python
class Solution:
    
    def reverse(self, x):
        
        if x >= 2**31-1 or x <= -2**31: #先確認範圍
            return 0
        else:
            strg = str(x)
        if x >= 0 :
            revst = strg[::-1]#將數字直接顛倒過來
        else:
            temp = strg[1:] #把負號拿掉
            temp2 = temp[::-1] #數字顛倒
            revst = "-" + temp2 #負號放回
        if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0 #再次確認顛倒後的數值是否在範圍內
        else: return int(revst)
```

