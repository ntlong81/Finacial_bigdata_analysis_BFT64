words = "aa bb aa a a a ccc".split()
fre_word = {}
for word in words:
    if word in fre_word:
        fre_word[word] += 1
    else:
        fre_word[word] = 1
print(fre_word)

def is_prime(n):
    if n<=1:
        return False
    else:
        for d in range(2,int(n**0.5)+1):
            if n%d==0:
                return False   
    return True
is_prime(29)