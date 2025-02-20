words = "aa bb aa a a a ccc".split()
fre_word = {}
for word in words:
    if word in fre_word:
        fre_word[word] += 1
    else:
        fre_word[word] = 1
print(fre_word)