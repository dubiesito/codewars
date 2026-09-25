def apples_distribution(apples, capacity, max_left):
    count = 0
    for N in range (1, capacity +1):
        boxes = apples // N
        used = boxes * N
        left_over = apples - used
        if left_over <= max_left and left_over <=N:
            count += 1
    return count