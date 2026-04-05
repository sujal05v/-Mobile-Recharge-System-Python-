##---------------Mobile Recharge System-----------------------
"""1. Basic Plan - Rs199
2. Standard Plan - Rs399
3. Premium Plan - Rs599
4. Unlimited Plan - Rs799
"""

print("-------Mobile Recharge System-------")
print("1. Basic Plan")
print("2. Standard Plan")
print("3. Premium Plan")
print("4. Unlimited Plan")
print("------------------------------------")

choice = int(input("Choose Your Plan(1-4): "))
print("-------------------------------------")


if(choice == 1):
 
  print("Basic Plan - Rs199")
  print("1Gb Data Available Daily")
  print("100 Msg Avaliable")
  print("Unlimited Call")
  print("All valid for 28 Days")

elif(choice == 2):
  
  print("Standard Plan - Rs399")
  print("2.5 Gb Data Available Daily")
  print("500 Msg Avaliable")
  print("Unlimited Call")
  print("All valid for 28 Days")

elif(choice == 3):

  print("Premium Plan - Rs599")
  print("3Gb Data Available Daily")
  print("1500 Msg Avaliable")
  print("Unlimited Call")
  print("You can avail Hotstar and Prime with Jio Music")
  print("All valid for 56 Days")

elif(choice == 4):
  
  print("Unlimited Plan - Rs799")
  print("3Gb Data Available for 4G / Unlimited Data for 5G")
  print("Unlimited Msg Avaliable")
  print("Unlimited Call")
  print("You can avail 30+ Online Entertainment Platforms")
  print("Get a Free Callertune for 56Days at JioMusic ")
  print("Get 10% Off on any hotel booking from MakeMyTrip")
  print("All valid for 56 Days")

else:
  print("Choose your number properly sir/madam from (1-4)")


print("--------------------------------------------------")

accept = input("Should we Go with your choice (Yess/NO): ")
accept = accept.lower()
if (accept == "yess"):
  print("Cool Your Choice is Amazing")
else:
  print("It's Okay, we have more plan for you. Check it out")