
from collections import defaultdict 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []   
        self.graph_matrix = [[0 for column in range(vertices)]
                    for row in range(vertices)] 
        

            
    def addEdge(self,u,v,w): 
        pass
    def Dijkstra(self, s): 
        
        self.Q = defaultdict(list)      
        for i in range(len(self.graph)) :
            self.Q[str(i)]=self.graph[i]
         
        
        self.pre = defaultdict(list)
        for i in range(self.V):
            self.pre[str(i)].append(-1)
            
        
        self.dis = defaultdict(list)
        for i in range(self.V):
            self.dis[str(i)]= 0
        
        
        
         
        for i in self.Q:
            if self.Q[i][s]!= 0 :
                self.pre[i] = s
                self.dis[i] = self.Q[i][s]
                
                
        
        self.S = []
        self.S.append(str(s))
            
           
        self.Q.pop(str(s))
        
        
        return self.BOJIA(self.dis)
    
    def BOJIA(self,dis):
        
        
        for m in self.dis:
            if (self.dis[m]!=0 )&( m not in self.S) :
                min = self.dis[m]
                min_key = m
                break
        for i in self.dis:
            if (self.dis[i]!=0) & (self.dis[i] < min)&( i not in self.S):
                min = self.dis[i]
                min_key = i
        
        
        
        for i in self.Q:
            if i != min_key:
                if self.Q[min_key][int(i)] != 0:
                    if (self.dis[i]==0) | (self.dis[i] > self.Q[min_key][int(i)] + self.dis[min_key]):
                        self.dis[i] = self.Q[min_key][int(i)] + self.dis[min_key]
                        self.pre[i] = min_key
        self.S.append(min_key)
        self.Q.pop(min_key)
        if len(self.Q) != 0:
            self.BOJIA(self.dis)
        return dict(self.dis)
    def Kruskal(self):
        pass
