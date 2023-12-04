with open("input.txt", "r") as file:

    mostCalories = 0
    secondMostCalories = 0
    thirdMostCalories = 0
    currentElfCalories = 0

    for line in file:
        numOrBlank = line.strip('\n')
        if (numOrBlank != ''):
            currentElfCalories = currentElfCalories + int(line)
        else:
            if (currentElfCalories > mostCalories):
                mostCalories = currentElfCalories
            elif (currentElfCalories > secondMostCalories):
                secondMostCalories = currentElfCalories
            elif (currentElfCalories > thirdMostCalories):
                thirdMostCalories = currentElfCalories
            currentElfCalories = 0

    print('Top 3 calories total: ' + str(mostCalories + secondMostCalories + thirdMostCalories))
