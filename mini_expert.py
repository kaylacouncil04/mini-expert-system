############################################################
# Travel Recommendation Mini Expert System
# CSC 330: Intro to AI/ML
# Kayla Council, Gabrielle Olds, & Chloe Washington
############################################################


# ==========================================================
# SECTION 1 - USER INTERFACE & DATA COLLECTION
# Kayla Council
# ==========================================================


import csv    # We're storing the users answers in a CSV file for future analysis


def show_intro():
   
    print("==========================================================")
    print("Welcome to our Travel Recommendation System!")
    print("==========================================================")
    print("This system will recommend a travel destination based on your preferences.")
    print("You will answer 10 questions.")
    print("At the end, we will give you a recommendation based on your preferences! \n")


def get_valid_input(prompt, options):
    
    while True:
        print(prompt)

        # Displaying the optiones (numbered)
        for number, value in options.items():
            print(f"{number}. {value}")
        
        choice = input("Please enter the number of your choice: ")

        # Checking if the input is valid
        if choice in options:
            return options[choice]
        else:
            print("Invalid input, please enter the correct input. \n")



def collect_user_preferences():

    user_preferences = {}

    # 1. Budget range
    budget_options = {
        "1": "low",
        "2": "medium",
        "3": "high"
    }
    user_preferences["budget"] = get_valid_input("\n 1) What is your budget range?", budget_options)

    
    # 2. Continent
    continent_options = {
        "1": "North America",
        "2": "South America",
        "3": "Europe",
        "4": "Asia",
        "5": "Africa",
    }
    user_preferences["continent"] = get_valid_input("\n 2) Which continent do you prefer?", continent_options)

    
    # 3. Language Comfort
    language_options = {
        "1": "English-speaking",
        "2": "Open to other languages"
    }
    user_preferences["language"] = get_valid_input("\n 3) Are you comfortable with non-English speaking countries?", language_options)

    
    # 4. Reason for travel
    reason_options = {
        "1": "Relaxing",
        "2": "Adventure",
        "3": "Culture/History"
    }
    user_preferences["reason"] = get_valid_input("\n 4) What is your main reason for traveling?", reason_options)

   
    # 5. Preferred Season
    season_options = {
        "1": "Summer",
        "2": "Fall",
        "3": "Winter",
        "4": "Spring"
    }
    user_preferences["season"] = get_valid_input("\n 5) What season do you want to travel in?", season_options)

    
    # 6. Temperature Preference
    temperature_options = {
        "1": "Hot",
        "2": "Warm/Mild",
        "3": "Cold"
    }
    user_preferences["temperature"] = get_valid_input("\n 6) What temperature do you prefer?", temperature_options)

    
    # 7. Preferred Landscape
    landscape_options = {
        "1": "Beach",
        "2": "Mountain",
        "3": "City",
        "4": "Rural"
    }
    user_preferences["landscape"] = get_valid_input("\n 7) What type of landscape do you prefer?", landscape_options)

    
    # 8. Modesty Preference
    modesty_options = {
        "1": "Open culture",
        "2": "More modest, strict culture"
    }
    user_preferences["modesty"] = get_valid_input("\n 8) Do you prefer open cultures or more modest, strict cultures?", modesty_options)
    

    # 9. Population Preference
    population_options = {
        "1": "Low population/isolated",
        "2": "High population/busy"
    }
    user_preferences["population"] = get_valid_input("\n 9) Do you prefer low population or busy cities?", population_options)

    
    # 10. Group Size (Collected but NOT used in the scoring)
    group_options = {
        "1": "Solo",
        "2": "Couple",
        "3": "Family/Friends"
    }
    user_preferences["group_size"] = get_valid_input("\n 10) Who are you traveling with?", group_options)


    return user_preferences


def save_user_data(user_preferences):
    
    file_name = "user_data.csv"

    # Checking to see if the file exists and it writes the header only once
    try:
        with open(file_name, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(user_preferences.keys())
    except FileExistsError:
        pass


    # Appending the users' data
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(user_preferences.values())
    
    # Letting the user know that their data has been saved
    print("\nYour data has been saved for future analysis.")



# ==========================================================
# SECTION 2 - KNOWLEDGE BASE (DESTINATIONS)
# Chloe Washington
# ==========================================================

def load_destinations():

    destinations = [
        {
            "name": "Paris",
            "budget": "high",
            "continent": "Europe",
            "language": "Open to other languages",
            "reason": "Culture/History",
            "season": "Spring",
            "temperature": "Warm/Mild",
            "landscape": "City",
            "modesty": "Open culture",
            "population": "High population/busy"
        },
        {
            "name": "Tokyo",
            "budget": "high",
            "continent": "Asia",
            "language": "Open to other languages",
            "reason": "Adventure",
            "season": "Fall",
            "temperature": "Warm/Mild",
            "landscape": "City",
            "modesty": "More modest, strict culture",
            "population": "High population/busy"
        },
        {
            "name": "New York",
            "budget": "medium",
            "continent": "North America",
            "language": "English-speaking",
            "reason": "Adventure",
            "season": "Summer",
            "temperature": "Warm/Mild",
            "landscape": "City",
            "modesty": "Open culture",
            "population": "High population/busy"
        },
        {
            "name": "Cape Town",
            "budget": "medium",
            "continent": "Africa",
            "language": "English-speaking",
            "reason": "Relaxing",
            "season": "Winter",
            "temperature": "Warm/Mild",
            "landscape": "Beach",
            "modesty": "Open culture",
            "population": "Low population/isolated"
        },
        {
            "name": "Bali",
            "budget": "low",
            "continent": "Asia",
            "language": "Open to other languages",
            "reason": "Relaxing",
            "season": "Summer",
            "temperature": "Hot",
            "landscape": "Beach",
            "modesty": "Open culture",
            "population": "Low population/isolated"
        },
        {
            "name": "Reykjavik",
            "budget": "medium",
            "continent": "Europe",
            "language": "Open to other languages",
            "reason": "Adventure",
            "season": "Winter",
            "temperature": "Cold",
            "landscape": "Rural",
            "modesty": "Open culture",
            "population": "Low population/isolated"
        },
        {
            "name": "Rio de Janeiro",
            "budget": "low",
            "continent": "South America",
            "language": "Open to other languages",
            "reason": "Relaxing",
            "season": "Summer",
            "temperature": "Hot",
            "landscape": "Beach",
            "modesty": "Open culture",
            "population": "High population/busy"
        },
        {
            "name": "Cairo",
            "budget": "low",
            "continent": "Africa",
            "language": "Open to other languages",
            "reason": "Culture/History",
            "season": "Fall",
            "temperature": "Hot",
            "landscape": "City",
            "modesty": "More modest, strict culture",
            "population": "High population/busy"
        },
        {
            "name": "Vancouver",
            "budget": "medium",
            "continent": "North America",
            "language": "English-speaking",
            "reason": "Relaxing",
            "season": "Spring",
            "temperature": "Warm/Mild",
            "landscape": "Mountain",
            "modesty": "Open culture",
            "population": "Low population/isolated"
        },
        {
            "name": "Buenos Aires",
            "budget": "high",
            "continent": "South America",
            "language": "Open to other languages",
            "reason": "Culture/History",
            "season": "Spring",
            "temperature": "Warm/Mild",
            "landscape": "City",
            "modesty": "Open culture",
            "population": "High population/busy"
        }
    ]

    return destinations



# ==========================================================
# SECTION 3 - INFERENCE ENGINE / SCORING LOGIC
# (Person 3 Responsible)
# ==========================================================

def calculate_score(user_preferences, destination):
    """
    Compare user preferences with destination attributes.
    Add weighted points when attributes match.
    Return total score.
    """

    score = 0

    # If budget matches - add points
    # If continent matches - add points
    # If language matches - add points
    # If reason matches - add points
    # If season matches - add points
    # If temperature matches - add points
    # If landscape matches - add points
    # If modesty matches - add points
    # If population matches - add points

    return score


def rank_destinations(user_preferences, destinations):
    """
    Loop through all destinations.
    Calculate score for each.
    Store scores.
    Identify highest score.
    Optionally determine top 3.
    Return best destination and score.
    """
    pass


def explain_recommendation(best_destination, score):
    """
    Display final recommendation.
    Explain why it was selected.
    Optionally show match percentage.
    """
    pass



# ==========================================================
# MAIN PROGRAM FLOW
# ==========================================================

def main():

    # 1. Show system introduction
    show_intro()

    # 2. Collect user preferences
    user_preferences = collect_user_preferences()

    # 3. Load knowledge base
    destinations = load_destinations()

    # 4. Run scoring system
    best_destination, score = rank_destinations(
        user_preferences,
        destinations
    )

    # 5. Display recommendation
    explain_recommendation(best_destination, score)

    # 6. Save user data to CSV
    save_user_data(user_preferences)


if __name__ == "__main__":
    main()
