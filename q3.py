"""
经典题： 给一个二维list，一个值b。 然后给你一个目标点X，X.val = a， 然后把周围直接和间接相连的所有val = a 的格子的值换成b
"""

def replace_val(arr, pos, replacing_val):
    for i in arr:
        print(i)
    print()
    

    m, n = len(arr), len(arr[0]) 
    target_val = arr[pos[0]][pos[1]]
    directions =((1, 0 ),
                 (-1, 0), 
                 (0, 1),
                 (0, -1))
    
    need_replace_stack =[pos]
    while need_replace_stack:
        curr_i, curr_j = need_replace_stack.pop()
        arr[curr_i][curr_j] = replacing_val
        for x, y in directions:
            next_i, next_j = curr_i + x, curr_j + y
            if 0 <= next_i < m and  0 <= next_j < n:
                if arr[next_i][next_j] == target_val:
                    need_replace_stack.append([next_i, next_j])
    
    for i in arr:
        print(i)
    return 

replace_val([[0, 1, 0, 0, 0], [1, 1, 1, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 1, 0]],[1,2], 2)