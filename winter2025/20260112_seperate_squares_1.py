def separateSquares(squares):
    total_area = sum((side * side for x, y, side in squares))

    sweep_events = (
        [(y, 1, side) for x, y, side in squares] +
        [(y + side, 0, side) for x, y, side in squares]
    )
    sweep_events.sort()

    active_width = 0
    area_so_far = 0
    last_y = 0

    for i in range(len(sweep_events)):
        curr_y, is_starting, side = sweep_events[i]

        height_change = curr_y - last_y
        new_area = active_width * height_change

        if area_so_far + new_area >= total_area / 2:
            needed_height = (total_area / 2 - area_so_far) / active_width
            return last_y + needed_height

        if is_starting:
            active_width += side
        else:
            active_width -= side

        area_so_far += new_area
        last_y = curr_y