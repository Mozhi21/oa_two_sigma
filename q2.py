"""
二分猜答案
一堆服务器， 处理能力 为 list， 如果让一个服务器算力 +1倍， 费用有一个list
给一个费用上线，要求 服务器串联在一起，处理能力高
"""

def maximum_throughput(throughput, scaling_cost, budget):
    lo = min(throughput) - 1
    hi = budget // scaling_cost[0] + throughput[0] + 1
    n = len(throughput)

    def _validate(guss_throughput):
        total_spent = 0
        # nums_holder =[]
        # cost_holder= []
        for i in range(n):
            # print(i, throughput[i], scaling_cost[i],guss_throughput, guss_throughput // throughput[i] )
            nums_of_needed_instance = guss_throughput // throughput[i]
            if  guss_throughput % throughput[i]:
                nums_of_needed_instance += 1
            total_spent += max(0, (nums_of_needed_instance - 1)) * scaling_cost[i]
            # nums_holder.append(max(0, (nums_of_needed_instance - 1)))
            # cost_holder.append(max(0, (nums_of_needed_instance - 1)) * scaling_cost[i])
        # print(guss_throughput, total_spent,nums_holder,cost_holder)
        if total_spent <= budget:
            return True
        return False

    while lo < hi - 1:
        mid = (lo + hi) // 2
        if _validate(mid):
            lo = mid
        else:
            hi = mid
    
    return lo

print(maximum_throughput([4,2,7], [3,5,6], 32))