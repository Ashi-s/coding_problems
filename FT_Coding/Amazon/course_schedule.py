'''
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
'''
from collections import OrderedDict 
class Solution():
    
    # def bfs(self,d, each, remain, stack):
    #     if each not in d:
    #         print('e--', each)
    #         if each not in stack:
    #             stack.append(each)
    #             print('stack-----', stack)
    #             return True

    #     else:
    #         if len(remain) > 0:
    #             return self.bfs(d, remain[0], remain[1:], stack)
    #         return False


    # def findOrder(self, numCourses, prerequisites):
    #     """
    #     :type numCourses: int
    #     :type prerequisites: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     d = OrderedDict()
    #     stack = []
    #     for each in prerequisites:
    #         if each[0] not in d:
    #             d[each[0]] = [each[1]]
    #         else:
    #             d[each[0]].append(each[1])
    #     print('d----', d)
        
    #     for node in d:
    #         print('---------',node)
    #         if len(d[node]) > 0:
    #             self.bfs(d, d[node][0], d[node][1:], stack)
    #         else:
    #             self.bfs(d, [], [],stack)
    #         # for each in d[node]:

    #         #     print('-------', each)
    #         #     if each in stack:
    #         #         continue
    #         #     else:

    #         #         x = self.bfs(d, each, stack)
    #         #         print('x------',x)
    #         #         if x is True:
    #         #             continue
                
    #         # if node not in stack:
    #         #     stack.append(node)
    #     return stack
    def bfs(self, d, key, stack, length):
        for i in range(length):
            if d[key][length] not in d:
                if d[key][length] not in stack:
                    stack.append(d[key][length])
            else:
                new_length = len(d[d[key][length]])
                print('######', d[d[key][length]])
                self.bfs(d, d[d[key][length]], stack, new_length)
            
            print('helper---', d, d[d[key][length]], stack, new_length)
        return True

    def findOrder(self, prerequisites):
        stack = []
        d = OrderedDict()
        for each in prerequisites:
            if each[0] not in d:
                d[each[0]] = [each[1]]
            else:
                d[each[0]].append(each[1])
        print('d----', d)
        for key in d:
            length = len(d[key])
            print('----length', length)
            print('findOrder--', d, key, stack, length)
            self.bfs(d, key, stack, length)
            
            stack.append(key)
        return stack

    
    



g = Solution()
#print(g.findOrder(4, [['1','0'],['2','0'],['3','1'],['3','2']]))
print(g.findOrder([['A','F'],['A','E'],['A','C'],['B','A'], ['B','C'], ['D','F'], ['F','G'], ['F','E'] ]))