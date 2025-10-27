def numberOfBeams(bank):
    beams = 0
    for r in range(len(bank)):
        if '1' in bank[r]:
            i = 1
            while r + i < len(bank):
                if '1' in bank[r+i]:
                    beams += bank[r].count('1')*bank[r+i].count('1')
                    break
                i += 1
    return beams