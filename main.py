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
        print("\n" + "="*50)
        print("🎵 ASAKE CHATBOT MENU 🎵")
        print("1. New Recommendations")
        print("2. Learn About Asake") 
        print("3. Next Asake Concert")
        print("4. Exit")
        
        try:
            user_choice = int(input("Pick an option from the menu (1-4): "))
        except ValueError:
            print("❌ Please enter a valid number (1-4)")
            continue
            
        if user_choice == 1:
            new_recommendations = new_rec(user_choice, collect_age)
            print("\n" + new_recommendations)
            input("\nPress Enter to continue...")  
            
        elif user_choice == 2:
            print("\n🎤 Asake is a Nigerian singer and songwriter who rose to fame in 2022 with his debut album, Mr. Money with the Vibe. Since then he has collabed with artists like Gunna, Olamide, Ayra Starr, and Wizkid, solidifying himself as one of the modern cornerstones of Nigerian Afrobeats.")
            input("\nPress Enter to continue...")   
            
        elif user_choice == 3:
            print("\n🎭 Next Asake concert: December 15th, 2024 at Lagos Arena! Tickets available soon.")
            input("\nPress Enter to continue...")   
            
        elif user_choice == 4:
            print("\n✅ Thanks for trying out Asake Chatbot, "+collect_name+"! Have a great day!")
            break  # Exit the loop and function
        else:
            print("❌ Invalid choice. Please select a number between 1-4.")

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

print("Hello", collect_name+"!", "Asake ChatBot will give you songs based on your age of", collect_age, "to match your vibe!", "I'll find something that you'll like!" )  
 
print("="*70)
song_rec = recommend_songs(collect_age)
print(song_rec)

continue_chatbot = str(input("\nWould you like to test out more features? (Yes) or (No): "))

if continue_chatbot.lower() == "yes":
    # Call the continue_bot function with the loop
    continue_bot(collect_name, collect_age)
else:
    print("Thanks for trying out Asake Chatbot, Have a great day, "+ collect_name+"!")

print("\nBye", collect_name+"!", "see you next time!")