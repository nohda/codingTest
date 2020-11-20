from collections import Counter
def solution(genres, plays):
    answer = []
    answer_gen = []

    lis = [[i,genres[i],plays[i]] for i in range(len(genres))]
    c = sorted(lis, key = lambda x : [x[2]], reverse = True)
    print(c)

    for i in range(len(c)):
        gen = c[i][1]
        print(i,c[i],gen)
        j = i+1
        while j in range(len(c)):
            print(j,c[j])
            if gen == c[j][1]:
                if answer_gen.count(c[i][1]) < 2 :
                    answer.append(c[i][0])
                    answer_gen.append(c[i][1])
                    print(answer,answer_gen)

            j += 1
    print(answer)
    return answer

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]

solution(genres,plays)
