def find_winner(participants):
    winner=None
    highest_score=-1
    

    for name,score in participants.items():
        if score>highest_score:
            highest_score=score
            winner=name
            
    return winner, highest_score

print("Welcome to 'winner of the day' program!")
n=int(input("Enter the number of participants: "))

participants={}

for i in range(n):
    name=input(f"Enter Name of participant {i+1}: ")
    score=int(input(f"Enter score of {name}: "))
    participants[name]=score
    
winner_name, winner_score=find_winner(participants)
print("\n winner of the Day ")
print(f"name:{winner_name}")
print(f"score:{winner_score}")