choice = ["rock" , "paper" , "scissors"]
#this gives the only choices p1 and p2 can choose from
p1 = input("enter your choice: ")
p2 = input("enter your choice: ")

#condition 1: compares rock to paper
if p1=="rock" and p2=="paper":
    print("paper wins")
else:
    print("rock wins")

#condition 2: compares scissors to paper
if p1=="paper" and p2=="scissors":
    print("scissors wins")
else:
    print("paper wins")

#condition 3: compares rock to scissors
if p1=="rock" or p2=="scissors":
    print("rock wins")
    