def group_anagram(n):
    anagram={}
    for i in n:
        key="".join(sorted(i)) 
        if key in anagram:
            anagram[key].append(i)
        else:
            anagram[key]=[i]
    return list(anagram.values())
n=['eat','tea','tan','ate','nat','bat']
a=group_anagram(n)
print(a)

