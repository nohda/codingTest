def solution(money, expected, actual):
    answer = -1
    answer = process(money, expected, actual)
    return answer

def process(money, expected, actual):
    i = 0
    bet = 100
    while i < len(expected):
        print("bet",bet)
        if money <= 0:
            break
        if money < bet:
            bet = money

        if expected[i] == actual[i]:
            money += bet
            bet = 100

        else :
            money -= bet
            bet = bet * 2

        print(i,money,expected[i],actual[i])

        i += 1
    return money

money = 1200
expected = ['T', 'T', 'H', 'H', 'H']
actual = ['H', 'H', 'T', 'H', 'T']
process(money, expected, actual)
