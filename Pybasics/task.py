def number_factors(number, position):
    print("Check")
    listToAppend = []
    print("The factors of", number, "are:")
    for i in range(1, number + 1):
        if number % i == 0:
            listToAppend.append(i)

    print(listToAppend)
    # print(listToAppend[position])
    print(len(listToAppend))  #8


    if position > len(listToAppend):
        return 0
    else:
        return(listToAppend, listToAppend[position])



def side():
    x = 10
    y = 2
    final_answer = number_factors(x, y)
    print(final_answer)

side()
