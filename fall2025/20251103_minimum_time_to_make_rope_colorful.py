def minCost(colors, neededTime):
    result = 0
    left = 0
    for right in range(len(colors)):
        if colors[left] != colors[right]:
            result += sum(neededTime[left:right]) - max(neededTime[left:right])
            left = right

    return result + sum(neededTime[left:len(colors)]) - max(neededTime[left:len(colors)])