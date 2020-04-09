'''
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example:
                      
  Input: [[10,20],[30,200],[400,50],[30,20]]
  Output: 110
  Why?
  The first person goes to city A for a cost of 10.
  The second person goes to city A for a cost of 30.
  The third person goes to city B for a cost of 50.
  The fourth person goes to city B for a cost of 20.

  The total minimum cost is 10 + 30 + 50 + 20 = 110 
  to have half the people interviewing in each city.
'''
def min_cost(arr):
    totsl = 0
    for i in arr:
        totsl += min(i[0], i[1])
    return totsl

arr = [[10,20],[30,200],[400,50],[30,20]]
print(min_cost(arr))