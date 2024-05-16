#For Else Loop in Python
#For else loope printts else block only if for loop executed succeessfully.Else will not be executed it for loop terminated
teams=["Sunrisers Hyderabd","Kolkatta Knight Riders","Rajastan Royals","Chennai Super Kings"]
for team in teams:
    print("Team Name is: ",team)
else:
    print("These Are My Predicted Teams Top Four Teams of IPL-2024")

print("\"For Else With For Termination\"")
captains=["Shreyas Iyyer","Patrick James Cummins","Sanju Samson","Ruturaj Gaikwad"]
for captain in captains:
    print(captain)
    if captain=="Patrick James Cummins":
        break
else:
    print("Captains of Top Four Teams of IPL")# It will not be executed because else will not work for loop terminations

#Output
# Team Name is:  Rajastan Royals
# Team Name is:  Chennai Super Kings
# These Are My Predicted Teams Top Four Teams of IPL-2024
# "For Else With For Termination"
# Shreyas Iyyer
# Patrick James Cummins