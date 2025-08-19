def canPlaceFlowers(flowerbed, n):
    plantable_plots = 0
    empty_plots = 1
    for plots in flowerbed:
        if plots == 1:
            empty_plots = 0
        elif plots == 0:
            empty_plots += 1
            if empty_plots == 3:
                plantable_plots += 1
                empty_plots = 1
                
    if empty_plots == 2:
        plantable_plots += 1

    return plantable_plots >= n