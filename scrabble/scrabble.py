import random

#Task 1
def word_score(word):
    score = 0
    word = word.upper()
    for letter in word:
        if letter in 'E, A, I, O, N, R, T, L, S, U':
            score += 1
        elif letter in 'D, G':
            score += 2
        elif letter in 'B, C, M, P':
            score += 3
        elif letter in 'F, H, V, W, Y':
            score += 4
        elif letter == 'K': 
            score += 5
        elif letter in 'J, X':
            score += 6
        else:
            score += 10
        
    return score

#Task 2
def generateRackRandomly():
    rack = []
    alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    

    while len(rack)<7:       
        tile = random.choice(alphabet)
        rack.append(tile.upper())
        alphabet.remove(tile)
    return rack
    
        
       

#Task 3
def generateRackFromTiles():
    letters=[]
    twelve_times = ['E']
    no_entered = 0
    while no_entered<12:
        for tile in twelve_times:
            letters.append(tile)
        no_entered += 1

    nine_times = ['A', 'I']
    no_entered = 0
    while no_entered<9:
        for tile in nine_times:
            letters.append(tile)
        no_entered += 1

    eight_times = ['O']
    no_entered = 0
    while no_entered<8:
        for tile in eight_times:
            letters.append(tile)
        no_entered += 1

    six_times = ['N','R','T']
    no_entered = 0
    while no_entered<6:
        for tile in six_times:
            letters.append(tile)
        no_entered += 1

    four_times = ['L','S','U','D']
    no_entered = 0
    while no_entered<4:
        for tile in four_times:
            letters.append(tile)
        no_entered += 1

    three_times=['G']
    no_entered = 0
    while no_entered<3:
        for tile in three_times:
            letters.append(tile)
        no_entered += 1

    two_times=['B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y']
    no_entered = 0
    while no_entered<3:
        for tile in two_times:
            letters.append(tile)
        no_entered += 1

    once = ['K','J','X','Q','Z']
    no_entered = 0
    while no_entered<1:
        for tile in once:
            letters.append(tile)
        no_entered += 1
    
    rack = []
    while len(rack)<7:       
        tile = random.choice(letters)
        rack.append(tile)
        letters.remove(tile)
    return rack
  
    
file = open('dictionary.txt','r')
words = file.readlines()

def valid_words(rack,words):
    for word in words:

        if len(word) > len(rack):
            words.remove(word)
        
        else:
            word_allowed = True
            for letter in word:
                if letter not in rack:
                    word_allowed = False
                elif word.count(letter) > rack.count(letter):
                    word_allowed = False
                else:
                    pass
            if word_allowed == False:
                words.remove(word)
            else:
                pass
    return words        

#Task 4       
def find_a_valid_word(rack,words):
    options = valid_words(rack,words)
    return options[0]

#Task 5
def longest_valid_word(rack,words):
    options = valid_words(rack,words)
    options.sort(key=lambda word: len(word))
    return options[-1]

#Task 6
def highest_scoring_word(rack,words):
    options = valid_words(rack,words)
    options.sort(key=lambda word: word_score(word))
    return options[-1]

rack = generateRackRandomly()
print(valid_words(rack,words))