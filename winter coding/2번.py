def unkey(encrypted_text, key):
    alphavet = list('0abcdefghijklmnopqrstuvwxyz')
    i = 0
    for text, key in zip(encrypted_text, key):
        print(text, key)
        temp = alphavet.index(text)-alphavet.index(key)
        if temp < 1: temp+=26
        encrypted_text = encrypted_text[:i] + alphavet[temp] + encrypted_text[i+1:]
        i+=1
    return encrypted_text

def solution(encrypted_text, key, rotation):
    return encrypted_text[rotation:]+encrypted_text[:rotation]