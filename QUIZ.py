print("welcome to my Quiz game!")

play = input("Do you want to play? ")

if play.lower() != "yes":
    quit();

True1 = 0;

print("okay! let's play :) ")

que1 = input("What comes next in the sequence: 2, 4, 8, 16, ?  ").lower()
if que1 == "32" :
    print("correct")
    True1+=1;
else :
    print("incorrect")


que2 = input("If A = 1, B = 2, C = 3, what is Z? ").lower()
if que2 == "26" :
    print("correct")
    True1+=1;
else :
    print("incorrect")


que3 = input("Which is the odd one out: Cat, Dog, Elephant, Car  ").lower()
if que3 == "Car" :
    print("correct")
    True1+=1;
else :
    print("incorrect")


que4 = input("Which number should come next: 1, 1, 2, 3, 5, 8, ? ").lower()
if que4 == "13" :
    print("correct")
    True1+=1;
else :
    print("incorrect")


que5 = input("Find the missing number: 9, 18, 36, ?, 144  ").lower()
if que5 == "72" :
    print("correct")
    True1+=1;
else :
    print("incorrect")

print(f"your score is {True1}.")
    
                