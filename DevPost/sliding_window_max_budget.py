'''
Given a list of land plots with their prices and a maximum budget.

Find the size of largest contiguous plot of land you can purchase under the given budget

Example:
                      
  Input: [1, 1, 3, 2, 4, 3, 2], budget = 7
  Output: 4
  Why? [1, 1, 3, 2]

'''
import queue
def maximum_budget(arr, budget):
    global_max = 0
    global_len = 0
    current_max = 0
    current_len = 0
    q = queue.Queue()
    for i in arr:
        if current_max + i <= budget:
            q.put(i)
            current_max += i
            current_len += 1
        else:
            if global_max < current_max:
                global_max = current_max
                #print(global_max)
                global_len = current_len
                current_max -= q.get()
                q.put(i)
                current_max += i
    return global_len

def max_budget(arr, budget):
    current_max = 0
    current_len = 0
    global_max = 0
    q = queue.Queue()
    for i in arr:
        if current_max + i <= budget:
            current_max += i
            current_len += 1
            q.put(i)
        else:
            global_max = current_max
            q.get()
            global_max += i
            current_max = global_max
            current_len -= 1
    return current_len



#print(max_budget([1, 1, 3, 2, 4, 3, 2], budget = 7))
print(maximum_budget([5, 1, 1, 2, 1, 1, 2], budget = 7))


    