
#python for displaying song based on age

thirteen_under = "Songs: Bandana, Only Me, and Great Guy are awesome choices with steady beats and good vocals!"
fourteen_to_twenty_five = "Songs: Lonely at the Top, Amapiano, and New Religion are fire songs with catchy lyrics!"
twenty_five_plus ="Songs: Ototo, Nzaza, and Dull are perfect songs with their deep meanings and strong vocals!"


def continue_bot(continue_response, collect_name): 
    if continue_response.lower() == "yes": 
        print("1. New Recommendations")
        print("2. Learn About Asake") 
        print("3. Next Asake Concert")
        print("4. Exit")
        
        user_choice = int(input("Pick an option from the menu for help: "))
        
        if user_choice == 1:
            print("Placeholder 1 selected.")
        elif user_choice == 2:
            print("Placeholder 2 selected.")
        elif user_choice == 3:
            print("Placeholder 3 selected.")
        elif user_choice == 4:
            print("Thanks for trying out Asake Chatbot, "+collect_name+"! Have a great day!")
        else:
            print("Invalid choice")
            
    elif continue_response.lower() == "no":
        print("Thanks for trying out Asake Chatbot, Have a great day, "+ collect_name+"!")
        return False
    return True


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

# Call the continue_bot function
continue_bot(continue_chatbot, collect_name)
