def asteroidCollision(asteroids):
    i = 0
    while len(asteroids) - 1 > i:
        if asteroids[i] > 0 > asteroids[i+1]:
            if abs(asteroids[i]) == abs(asteroids[i+1]):
                del asteroids[i:i+2]
                i = 0
            elif abs(asteroids[i]) > abs(asteroids[i+1]):
                asteroids.pop(i+1)
                i = 0
            else:
                asteroids.pop(i)
                i = 0
        else:
            i += 1
    return asteroids