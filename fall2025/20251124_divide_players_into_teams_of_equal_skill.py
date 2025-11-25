def dividePlayers(skill):
    skill.sort()
    totalSkill = skill[0] + skill[-1] 
    result = 0
    for i in range(len(skill) // 2):
        l_skill, r_skill = skill[i], skill[len(skill) - i - 1]
        if skill[i] + r_skill != totalSkill: return -1 
        result += l_skill * r_skill

    return result