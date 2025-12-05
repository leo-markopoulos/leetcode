from collections import defaultdict

def findCommonResponse(responses):
    count = defaultdict(int)
    for day in responses:
        for response in set(day):
            count[response] += 1

    return min(response for response, cnt in count.items() if cnt == max(count.values()))