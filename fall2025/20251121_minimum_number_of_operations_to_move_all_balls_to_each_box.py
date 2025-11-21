def minOperations(boxes):
    result = [0] * len(boxes)
    total, num_balls = 0, 0
    for l in range(len(boxes)):
        total += num_balls
        result[l] += total
        if boxes[l] == '1':
            num_balls += 1

    total, num_balls = 0, 0
    for r in range(len(boxes)-1, -1, -1):
        total += num_balls
        result[r] += total
        if boxes[r] == '1':
            num_balls += 1

    return result