def is_prime(n):
    if n<=1:
        return False
    else:
        for d in range(2,int(n**0.5)+1):
            if n%d==0:
                return False   
    return True

def normalize(text):
    text_norm = text.lower()
    special_letters = {'.',',','-','*','!',"?",':'}
    for letter in special_letters:
        text_norm = text_norm.replace(letter,' ')
    while '  ' in text_norm:
        text_norm = text_norm.replace("  "," ")
    return text_norm
def get_fre_word(text):
    fre_dict = {}
    for word in text.split():
        if word in fre_dict:
            fre_dict[word] += 1
        else:
            fre_dict[word] = 1
    return fre_dict
print('Well come to my module')

big_digit = 24248203840243802438