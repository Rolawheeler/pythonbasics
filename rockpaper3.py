choice = ["rock" ,"scissors" , "paper"]
#to show that these are the only choices that p1 and p2 can choose
p1 = input("enter your choice: ")
p2 = input("enter your choice: ")
#condition 1 : compare rock and scissors
if p1 =="rock" and p2 =="scissors" :
        print("rock wins")
#condition 2 : compare paper and rock
elif p1 == "rock":
    if p2 == "paper":
        print("paper wins")
#condition 3 : compare scissors and paper
elif p1 == "scissors":
    if p2 == "paper":
        print("scissors wins")
