import random
def word():
    while True:
        a=input("Enter a word at least 4 letters long: ")
        if len(a)>=4:
            b=input("Enter a hint sentence for that word: ")
            return a.upper(),b
        elif len(a)<4:
            print(a)
        
def splitWords(a):
    tokens=[]
    for item in a:
        split=len(item)//2
        split1= item[:split]
        split2= item[split:]
        tokens.append(split1)
        tokens.append(split2)
    return tokens

def main():
    print("Welcome to the CS1 Six Little Words Puzzle Maker")
    hint=[]
    words=[]
    for i in range(6):
        a,b=word()
        words.append(a)
        hint.append(b)
    t=splitWords(words)
    random.shuffle(t)
    print("Partial Words:")
    k=0
    for i in range(3):
        for j in range(4):
            print(t[k],end="\t")
            k=k+1
        print(" ")
    print("Hints:")
    for x in hint:
        print(x)

    print("Answer Key:")       
    for x in words:
        print(x)
    

if __name__=="__main__":
    main()
    
    
    
    
