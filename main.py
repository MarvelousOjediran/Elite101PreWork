#python for displaying song based on age

thirteen_under = "Songs: Bandana, Only Me, and Great Guy are awesome choices with steady beats and good vocals!"
fourteen_to_twenty_five = "Songs: Lonely at the Top, Amapiano, and New Religion are fire songs with catchy lyrics!"
twenty_five_plus ="Songs: Ototo, Nzaza, and Dull are perfect songs with their deep meanings and strong vocals!"

def new_rec(user_choice, collect_age):
    if user_choice == 1:
        if collect_age <= 13:
            return "Since you're 13 or under, here are some different recommendations:\n" + twenty_five_plus
        elif 14 <= collect_age <= 25:
            return "Since you're 14-25, here are some different recommendations:\n" + thirteen_under
        else:  # age > 25
            return "Since you're 25+, here are some different recommendations:\n" + fourteen_to_twenty_five
    return "" 

def continue_bot(collect_name, collect_age): 
    while True:  # Keep showing menu until user exits
        print("\n1. New Recommendations")
        print("2. Learn About Asake") 
        print("3. Next Asake Concert")
        print("4. Exit")
        
        user_choice = int(input("Pick an option from the menu for help: "))
        
        if user_choice == 1:
            new_recommendations = new_rec(user_choice, collect_age)
            print(new_recommendations)
            
        elif user_choice == 2:
            print("Asake is a Nigerian singer and songwriter known for his amazing afrobeats and amapiano music! He rose to fame in 2022 with his hit songs.")
        elif user_choice == 3:
            print("Next Asake concert: December 15th, 2024 at Lagos Arena! Tickets available soon.")
        elif user_choice == 4:
            print("Thanks for trying out Asake Chatbot, "+collect_name+"! Have a great day!")
            return False  # Exit the loop and function
        else:
            print("Invalid choice. Please try again.")

def recommend_songs(age):
    #Function to recommend songs based on user's age
    if age <= 13:
        return thirteen_under
    elif 14 <= age <= 25:
        return fourteen_to_twenty_five
    else:  # age > 25
        return twenty_five_plus

print("Hello, Welcome to the Asake ChatBot!")
#collect name and age for song recommendation
collect_name = str(input("What is your name?: "))
collect_age = int(input("What is your age?: ")) 

print("Hello", collect_name+"!", "Asake ChatBot will give you songs based on your age of ",collect_age," to match your vibe!","I'll find something that you'll like!" )  
 
print("####################################################################################################################################")
song_rec = recommend_songs(collect_age)
print(song_rec)

continue_chatbot = str(input("Would you like to test out more features? (Yes) or (No) "))

if continue_chatbot.lower() == "yes":
    # Call the continue_bot function with the loop
    continue_bot(collect_name, collect_age)
else:
    print("Thanks for trying out Asake Chatbot, Have a great day, "+ collect_name+"!")

print("Bye", collect_name+"!", "see you next time!")