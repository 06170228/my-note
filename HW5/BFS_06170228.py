
from collections import defaultdict 
  
class Graph:
    
    def __init__(self): 
        
        self.graph = defaultdict(list) 

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
     
    def BFS(self, s): 
        if s in self.graph:
            queue=[]
            visited = []
            result =[]
            queue.append(s)
          
            
            while queue:
                curr = queue[0]
                queue.pop(0)
                result.append(curr)
                visited.append(curr)
                
                for i in self.graph[curr]:
                    if i not in visited:
                        queue.append(i)
                        visited.append(i)
            return result
        else:
            print("error")
                
                
    def DFS(self, s):
        if s in self.graph:
            stack=[]
            visited = []
            result =[]
            stack.append(s)
          
            
            while stack:
                curr = stack[-1]
                stack.pop(-1)
                result.append(curr)
                visited.append(curr)
                
                for i in self.graph[curr]:
                    if i not in visited:
                        stack.append(i)
                        visited.append(i)
            return result
        else:
            print("error")
