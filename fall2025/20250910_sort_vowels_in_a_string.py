def sortVowels(s):
    vowels = "aeiouAEIOU"
    vowel_order = []
    for i in s:
        if i in vowels:
            vowel_order.append(i)
    vowel_order.sort()
    result = []
    j = 0
    for i in s:
        if i in vowels:
            result.append(vowel_order[j])
            j += 1
        else:
            result.append(i)
    return "".join(result)