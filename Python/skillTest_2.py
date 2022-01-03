def solution(n,words):
    answer = []

    for i in range(len(words)):
        if i == 0:
            last_text = ''

        if words[i][0] == last_text:
            last_text = words[i][-1]
        else:
            answer = [len(words)/n,len(words)-i]

        print(i,words[i],len(words)/n,len(words)-i)


    if answer == []:
        answer = [0,0]

    print(answer)
    return answer

n = 3
words = ["tank", 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
# print(len(words)%n)
# solution(n,words)
