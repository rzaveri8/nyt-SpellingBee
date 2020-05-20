
def getWords():
    with open('words_alpha.txt', 'r') as f:
        x = f.readlines()
        x = map(lambda s: s.strip(), x)
    return x


# Function to print words which can be created 
# using given set of characters 
  
  
def charCount(word): 
    dict = {} 
    for i in word: 
        dict[i] = dict.get(i, 0) + 1
        #print dict
    return dict

  
def possible_words(charSet, mainChar): 
    lwords = getWords()
    for word in lwords: 
        flag = 0
        chars = charCount(word) 
        for key in chars: 
            if key not in charSet: 
                flag =0
                break
            else: 
                if key == mainChar:
                    flag = 1 
                    #print("HEY",chars[key])

                    #flag = 0
        if flag == 1 and len(word) >3: 

            print(word) 
  
if __name__ == "__main__": 
    mainChar = 'l'
    charSet = ['t', 'i', 'b', 'l', 'g', 'e', 'y'] 
    possible_words(charSet, mainChar) 

#charCount('hey')
