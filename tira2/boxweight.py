from math import ceil

def min_count(weights, max_weight):
    weights = sorted(weights, reverse=True)
    if len(weights) == 0:
        return 0
    if weights[0] > max_weight:
        return -1

    capacities = []
    for w in weights:
        for i, cap in enumerate(capacities):
            if cap >= w:
                capacities[i] = cap - w
                break
        else:
            capacities.append(max_weight-w)
    upper_bound = len(capacities)
    
    suffix_sum = [0] * (len(weights)+1)
    for i in range(len(weights)-1, -1, -1):
        suffix_sum[i] = suffix_sum[i+1] + weights[i]
    suffix_heavy = [0] * (len(weights)+1)
    for i in range(len(weights)-1, -1, -1):
        suffix_heavy[i] = suffix_heavy[i+1] + (1 if weights[i] > (max_weight/2) else 0)

    boxes = []
    best = upper_bound

    def dfs(boxes, index=0, used_boxes=0):
        nonlocal best
        nonlocal suffix_heavy
        nonlocal suffix_sum
        
        if used_boxes >= best:
            return

        if index == len(weights):
            best = min(best, used_boxes)
            return

        rem_weight = suffix_sum[index]
        free_now = sum(boxes)
        cap_need = max(0, rem_weight - free_now)
        lb_add_boxes_by_weight = ceil(cap_need / max_weight)

        half_c = max_weight / 2
        heavy_left = suffix_heavy[index]
        big_boxes = sum(1 for cap in boxes if cap > half_c)
        lb_add_boxes_by_heavy = max(0, heavy_left - big_boxes)

        lower_bound_additional = max(lb_add_boxes_by_weight, lb_add_boxes_by_heavy)

        if used_boxes + lower_bound_additional >= best:
            return
        

        w = weights[index]
        tried_caps = set()
        cap = 0
        for i in range(len(boxes)):
            cap = boxes[i]
            if cap < w:
                continue
            if cap in tried_caps:
                continue

            tried_caps.add(cap)

            new_boxes = boxes[:]
            new_boxes[i] = cap - w
            new_boxes.sort(reverse=True)
            dfs(new_boxes, index+1, used_boxes)

        if used_boxes + 1 < best:
            if max_weight not in tried_caps:
                new_boxes = boxes[:]
                new_boxes.append(max_weight - w)
                new_boxes.sort(reverse=True)
                dfs(new_boxes, index+1, used_boxes+1)


    dfs(boxes)

    return best
        
if __name__ == "__main__":
    print(min_count([2, 3, 3, 5], 7)) # 2
    print(min_count([2, 3, 3, 5], 6)) # 3
    print(min_count([2, 3, 3, 5], 5)) # 3
    print(min_count([2, 3, 3, 5], 4)) # -1

    print(min_count([], 1)) # 0
    print(min_count([1], 1)) # 1
    print(min_count([1, 1, 1, 1], 1)) # 4
    print(min_count([1, 1, 1, 1], 4)) # 1

    print(min_count([3, 4, 1, 2, 3, 3, 5, 9], 10)) # 3

    print(min_count([6, 1, 6], 15)) # 1

    print(min_count([3, 4, 5, 2, 3], 9)) # 2
