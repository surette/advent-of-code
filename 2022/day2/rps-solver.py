# X = need to lose
# Y = needs to draw
# Z = needs to win

# rock = 1, paper = 2, scissors = 3

def getRoundScore(p1, p2):
    if (p1 == 'A'): # p1 plays rock
        if (p2 == 'X'): # p2 plays scissors
            return 3 # loss + scissors
        if (p2 == 'Y'): # p2 plays rock
            return 4 # draw + rock
        else:
            return 8 # win + paper
    if (p1 == 'B'): # p1 plays paper
        if (p2 == 'Y'): # p2 plays paper
            return 5 # draw + paper
        if (p2 == 'Z'): # p2 plays scissors
            return 9 # win + scissors
        else:
            return 1 # loss + rock
    if (p1 == 'C'): # p1 plays scissors
        if (p2 == 'Z'): # p2 plays rock
            return 7
        if (p2 == 'X'): # p2 plays paper
            return 2
        else:
            return 6

with open("day2/input.txt", "r") as file:
    totalScore = 0

    for line in file:
        round = line.split(' ')
        player1 = round[0]
        player2 = round[1].strip('\n')
        totalScore = totalScore + getRoundScore(player1, player2)

    print('Total score: ' + str(totalScore))