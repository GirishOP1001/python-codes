friends = ["Arush","Anushka","Yashraj","Bhumika","Tanvi"]
print("Original 5 friends : ",friends)
friends.append("Aarish")                                                               #adds at the end
print("I met Aarish, so my updated list of friends is : ",friends)
friends.extend(["Shravani","Soham","Aryan"])                                           #merges 2 lists
print("I made new friends in another class, my updated list of friends is : ",friends)
friends.remove("Arush")                                                                #removes element from the list
print("Arush moved to another city, updated list is : ",friends)
