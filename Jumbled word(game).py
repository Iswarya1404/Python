
        
#Jumbled word
import random
def choose():
    words = ["namjoon","seokjin","yoongi","hoseok","jimin","taehyung","jungkook"]
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def thank(p1n,p2n,p1,p2):
    print(p1n,"your score is:",p1)
    print(p2n,"your score is:",p2)
    print("thanks for playing")
def play():
    player1 = str(input("enter name of player 1:"))
    player2 = str(input("enter name of player 2:"))
    pp1 = 0
    pp2 = 0
    turn=0

    while(1):
        #computer's task
        picked_word = choose()
        #create question
        question = jumble(picked_word)
        print(question)
        #player1
        if turn%2==0:
            print(player1,"your turn")
            ans = input("what's on your mind? ")
            if ans==picked_word:
                print("correct")
                pp1 = pp1+1
                print("your score is:",pp1)
            else:
                print("better luck next time","  ","correct word:",picked_word)
            c=input("press 1 to continue and 0 to quit")
            if c==0:
                thank(player1,player2,pp1,pp2)
                break
        #player2
        if turn%3==0:
            print(player2,"your turn")
            ans = input("what's on your mind? ")
            if ans==picked_word:
                print("correct")
                pp2 = pp2+1
                print("your score is:",pp2)
            else:
                print("better luck next time","  ","correct word:",picked_word)
            c=input("press 1 to continue and 0 to quit")
            if c==0:
                thank(player1,player2,pp1,pp2)
                break
            turn=turn+1
play()
        
        
     
  
     

        

