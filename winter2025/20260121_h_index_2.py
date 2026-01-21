def hIndex(citations):
    h = 0
    for i in range(len(citations)):
        papers = len(citations) - i
        if citations[i] >= papers:
            h = papers
            break
    return h