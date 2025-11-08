
#python for displaying song based on age

     
thirteen_under = "Songs: Bandana, Only Me, and Great Guy are awesome choices with steady beats and good vocals!"
eighteen_to_twenty_five = ""


print("Hello, Welcome to the Asake ChatBot!");
#collect name and age for song reccomendation
collect_name = str(input("What is your name?: "));
collect_age = int(input("What is your age?: ")); 

print("Hello"", "+collect_name+"!", "Asake ChatBot will give you songs based on your age of ",collect_age," to match your vibe!","I'll find something that you'll like!" );  


print("1. Placeholder 1");
print("2. Placeholder 2"); 
print("3. Placeholder 3");
print("4. Placeholder 4");

user_choice = int(input("Pick an option from the menu for help: "));

if user_choice == 1:
    print("Placeholder 1 selected.")
elif user_choice == 2:
    print("Placeholder 2 selected.")
elif user_choice == 3:
    print("Placeholder 3 selected.")
elif user_choice == 4:
    print("Placeholder 4 selected.")
else:
    print("Invalid choice"); 
print("Bye",collect_name+"!","see you next time!")
                        


