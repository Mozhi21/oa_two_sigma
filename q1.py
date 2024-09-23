"""
经典题， 给我开会时间轴，求峰值多少人开会
"""

def server_traffic_monitor(start, end):
    counter = 0
    max_counter = 0
    max_traffic_idx = -1
    holder = []
    for i in start:
        holder.append([i, 1])
    for i in end:
        holder.append([i+1, -1])
    holder.sort()
    for idx, is_start in holder:
        if is_start == 1:
            counter += 1
            if max_counter < counter:
                max_traffic_idx = idx
                max_counter = counter
        else:
            counter -= 1
    print(max_counter, max_traffic_idx)
    return max_traffic_idx

print(server_traffic_monitor([1,6,2,9], [8,7,6,10]))

            