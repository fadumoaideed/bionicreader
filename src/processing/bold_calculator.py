
def bold_calculator_a(word):
    if(len(word) == 1 and len(word) <= 4):
        return 1
    elif(len(word) > 5 and len(word) <= 8):
        return 2
    elif(len(word) > 9 and len(word) <= 12):
        return 3
    elif(len(word) >= 13):
        return 5
    

#  Every two words are bold and the they whole word is bold except last two

def bold_calculator_c(word):
    if(len(word) == 1 and len(word) <= 3):
        return 1
    elif(len(word) == 4):
        return 2
    elif(len(word) >=5 and len(word) <= 6):
        return 3
    elif(len(word) >= 7):
        return int(len(word) / 2)
    