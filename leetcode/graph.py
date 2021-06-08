from typing import List, Deque
from collections import deque

def dfs(g: dict, start: int, vis =[]) -> None:
    vis.append(start)
    print(start, end = ", ")
    for next in g[start]:
        if next not in vis:
            dfs(g, next, vis)


def permutation(nums: list, j = 0) -> None:
    for i in range(len(nums[j:])):
        nums[j], nums[i+j] = nums[i+j], nums[j]
        if j<len(nums)-2:
            permutation(nums, j+1)
        else:
            print(nums)
        nums[j], nums[i+j] = nums[i+j], nums[j]


def phonestring(d: Deque, stack=[]) -> None:
    pc = {2:list("ABC"), 3:list("DEF"),9:list("WXYZ")}
    x = d.popleft()
    for char in pc[x]:
        stack.append(char)
        if len(stack) == 3:
            print(stack)
        else:
            phonestring(d, stack)
        stack.pop()
    d.appendleft(x)


def combi(s: List[str], k:int, stack=[], j = 0, used=[]):
    for i in range(len(s[j:])):
        s[j] , s[j+i] = s[j+i], s[j]
        if s[j] in used:
            continue
        stack.append(s[j])
        if len(stack)==k:
            print(stack)
        else:
            combi(s, k, stack, j + 1, used)
        stack.pop()
        s[j], s[j + i] = s[j + i], s[j]

        if j == 0:
            used.append(s[i])



if __name__ == "__main__":
    graph = {1: [2, 3], 2: [1, 4, 5], 3: [1, 6, 7], 4:[2,8,9], 5:[2,10,11], 6:[3,12,13], 7:[3,14,15],
             8:[4], 9:[4], 10:[5],11:[5],12:[6],13:[6],14:[7], 15:[7]}

    nums = deque([2,3,9])

    phonestring(nums)

    # l = ['A','B','C','D']
    # combi(l,3)
