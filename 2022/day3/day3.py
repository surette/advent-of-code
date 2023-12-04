with open("day3/input.txt", "r") as file:

    # duplicates = []
    itemScore = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum = 0

    # for line in file:
    #     ruckSize = len(line)
    #     c1 = slice(0,ruckSize//2)
    #     c2 = slice(ruckSize//2,ruckSize)
    #     compartment1 = line[c1]
    #     compartment2 = line[c2]

    #     for item in compartment1:
    #         if compartment2.__contains__(item):
    #             duplicates.append(item)
    #             break

    # for item in duplicates:
    #     i = 1
    #     for score in itemScore:
    #         if item == score:
    #             sum = sum + i
    #             break
    #         i = i+1

    duplicates = []
    fileList = list(file)
    for i in range(0, len(fileList), 3):
        try:
            for item in fileList[i]:
                if fileList[i+1].__contains__(item) and fileList[i+2].__contains__(item):
                    duplicates.append(item)
                    break
        except IndexError: 
            print('Reached end of file')

    for item in duplicates:
        i = 1
        for score in itemScore:
            if item == score:
                sum = sum + i
                break
            i = i+1

    print('Total score: ' + str(sum))