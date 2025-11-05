def maximumWhiteTiles(tiles, carpetLen):
    tiles.sort()
    prefixs = [0] * (len(tiles) + 1)
    for i in range(len(tiles)):
        prefixs[i+1] = prefixs[i] + (tiles[i][1] - tiles[i][0] + 1)
    result = 0
    j = 0 
    for i in range(len(tiles)): 
        end = tiles[i][0] + carpetLen - 1 
        while j < len(tiles) and tiles[j][1] < end:
            j += 1

        full_cover = prefixs[j] - prefixs[i]  
        if j < len(tiles) and tiles[j][0] <= end:
            partial_cover = end - tiles[j][0] + 1
        else: 
            partial_cover = 0

        result = max(result, full_cover + partial_cover)
        
    return result