def canVisitAllRooms(rooms):
    keys = rooms[0]
    s = set([0])
    while keys:
        key = keys.pop()
        if key not in s:
            s.add(key)
            keys += rooms[key]
    return True if len(s) == len(rooms) else False