def totalFruit(fruits):
    if len(fruits) <= 2:
        return len(fruits)

    first_new_ind = 1 
    if fruits[0] != fruits[1]:
        fruit1, fruit2 = [fruits[0],0], [fruits[1],1]
    else:
        while fruits[0] == fruits[first_new_ind]:
            first_new_ind += 1 
            if first_new_ind >= len(fruits):
                return len(fruits)
        fruit1, fruit2 = [fruits[0],first_new_ind-1], [fruits[first_new_ind],first_new_ind]
    
    result = 0
    left = 0
    for right in range(first_new_ind,len(fruits)):
        if fruits[right] == fruit1[0]:
            fruit1[1] = right

        elif fruits[right] == fruit2[0]:
            fruit2[1] = right

        else:
            if fruit1[1] < fruit2[1]:
                left = fruit1[1] + 1
                fruit1[1] = right
                fruit1[0] = fruits[right]
            else:
                left = fruit2[1] + 1
                fruit2[1] = right
                fruit2[0] = fruits[right]
        
        result = max(result, right-left+1)
    return result