def solution(penter, pexit, pescape, data):
    answer = ''
    answer = process(penter, pexit, pescape, data)
    return answer

def process(penter, pexit, pescape, data):
    length = len(penter)
    # data_text = map(''.join, zip(*[iter(data)]*length))
    data_text = [data[i:i+length] for i in range(0, len(data), length)]
    answer = penter
    for i in range(len(data_text)):
        print(i,data_text,data_text[i])
        if penter == data_text[i]:
            answer += pescape + data_text[i]
        elif pexit == data_text[i]:
            answer += pescape + data_text[i]
        elif pescape == data_text[i]:
            answer += pescape + data_text[i]
        else:
         answer += data_text[i]
    answer = answer + pexit
    return answer

    # print(answer)
penter ="1100"
pexit ="0010"
pescape ="1001"
data ="1101100100101111001111000000"

# process(penter, pexit, pescape, data)


length=4
li = [data[i:i+length] for i in range(0, len(data), length)]
print(li)
