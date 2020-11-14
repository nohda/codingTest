def search_text(encrypted_text, key):
    # letters = list(key)
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
    result = ""
    y = 0
    while y < len(encrypted_text):
        j = letters.index(encrypted_text[y])
        find_i = y + j +1
        if find_i < len(encrypted_text):
            result += letters[find_i]
        else:
            result += letters[(find_i)-len(encrypted_text)]
        y += 1
    return result

def rotation_text(encrypted_text,rotation):
    if rotation > 0:
        while rotation > 0 :
            temp = encrypted_text[-1]
            temp_text = encrypted_text[:-1]
            encrypted_text = temp + temp_text
            rotation -= 1
    else:
        while rotation < 0 :
            temp = encrypted_text[0]
            temp_text = encrypted_text[1:]
            encrypted_text = temp_text + temp
            rotation += 1

    return  encrypted_text


def solution(encrypted_text, key, rotation):
    answer = ''
    result = search_text(encrypted_text,key)
    answer = rotation_text(encrypted_text,rotation)
    print(answer)
    return answer

encrypted_text = "qyyigoptvfb"
key = "abcdefghijk"
rotation = 3

solution(encrypted_text,key,rotation)
