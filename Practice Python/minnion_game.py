def minion_game(string):
    # your code goes here
    sub_str =[]
    kevin =[]
    stuart=[]   
    for i in range (0,len(string)+1):
        s= string
        s = string[i:]
        for j in range (1,len(s)+1):
            sub_str.append(s[:j])
            
        
    for word in sub_str:
        if word[0].lower() in ('a','e','i','o','u'):
            kevin.append(word)
        else:
            stuart.append(word)



    if len(kevin)>len(stuart):
        print("KEVIN"+" "+str(len(kevin)))

    elif len(stuart)>len(kevin):
        print("STUART"+" "+str(len(stuart)))
    else:
        print('Draw')


def minion_game2(string):
    s=len(string)
    vowel = 0
    consonant = 0
     
    for i in range(s):
        if string[i] in 'AEIOU':
           vowel+=(s-i)
        else:
           consonant+=(s-i)
                
    if vowel < consonant:
        print('Stuart ' + str(consonant))
    elif vowel > consonant:
        print('Kevin ' + str(vowel))
    else:
        print('Draw')

                     

if __name__ == '__main__':
    s = input()
    minion_game(s)
