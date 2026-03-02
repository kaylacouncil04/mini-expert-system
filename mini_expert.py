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
        # ==========================================================
        # NORTH AMERICA
        # ==========================================================
        {"name": "New York City, USA", "budget": "high", "continent": "North America", "language": "English-speaking", "reason": "Culture/History", "season": "Summer", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Miami, USA", "budget": "high", "continent": "North America", "language": "English-speaking", "reason": "Relaxing", "season": "Summer", "temperature": "Hot", "landscape": "Beach", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Los Angeles, USA", "budget": "high", "continent": "North America", "language": "English-speaking", "reason": "Adventure", "season": "Summer", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Las Vegas, USA", "budget": "medium", "continent": "North America", "language": "English-speaking", "reason": "Adventure", "season": "Summer", "temperature": "Hot", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Cancún, Mexico", "budget": "low", "continent": "North America", "language": "Open to other languages", "reason": "Relaxing", "season": "Summer", "temperature": "Hot", "landscape": "Beach", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Orlando, USA", "budget": "medium", "continent": "North America", "language": "English-speaking", "reason": "Relaxing", "season": "Summer", "temperature": "Hot", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Toronto, Canada", "budget": "medium", "continent": "North America", "language": "English-speaking", "reason": "Culture/History", "season": "Fall", "temperature": "Cold", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Punta Cana, Dominican Republic", "budget": "low", "continent": "North America", "language": "Open to other languages", "reason": "Relaxing", "season": "Winter", "temperature": "Hot", "landscape": "Beach", "modesty": "Open culture", "population": "Low population/isolated"},
        {"name": "Vancouver, Canada", "budget": "medium", "continent": "North America", "language": "English-speaking", "reason": "Relaxing", "season": "Spring", "temperature": "Warm/Mild", "landscape": "Mountain", "modesty": "Open culture", "population": "Low population/isolated"},
        {"name": "San Francisco, USA", "budget": "high", "continent": "North America", "language": "English-speaking", "reason": "Culture/History", "season": "Spring", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},

        # ==========================================================
        # AFRICA
        # ==========================================================
        {"name": "Cape Town, South Africa", "budget": "medium", "continent": "Africa", "language": "English-speaking", "reason": "Adventure", "season": "Summer", "temperature": "Warm/Mild", "landscape": "Mountain", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Stone Town, Tanzania", "budget": "low", "continent": "Africa", "language": "Open to other languages", "reason": "Culture/History", "season": "Summer", "temperature": "Hot", "landscape": "Beach", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Cairo, Egypt", "budget": "low", "continent": "Africa", "language": "Open to other languages", "reason": "Culture/History", "season": "Winter", "temperature": "Warm/Mild", "landscape": "City", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Addis Ababa, Ethiopia", "budget": "low", "continent": "Africa", "language": "Open to other languages", "reason": "Culture/History", "season": "Spring", "temperature": "Warm/Mild", "landscape": "Mountain", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Maputo, Mozambique", "budget": "low", "continent": "Africa", "language": "Open to other languages", "reason": "Relaxing", "season": "Fall", "temperature": "Hot", "landscape": "Beach", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Nairobi, Kenya", "budget": "medium", "continent": "Africa", "language": "English-speaking", "reason": "Adventure", "season": "Summer", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Essaouira, Morocco", "budget": "low", "continent": "Africa", "language": "Open to other languages", "reason": "Relaxing", "season": "Summer", "temperature": "Warm/Mild", "landscape": "Beach", "modesty": "More modest, strict culture", "population": "Low population/isolated"},
        {"name": "Johannesburg, South Africa", "budget": "medium", "continent": "Africa", "language": "English-speaking", "reason": "Culture/History", "season": "Fall", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Marrakech, Morocco", "budget": "medium", "continent": "Africa", "language": "Open to other languages", "reason": "Culture/History", "season": "Fall", "temperature": "Hot", "landscape": "City", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Kigali, Rwanda", "budget": "medium", "continent": "Africa", "language": "English-speaking", "reason": "Culture/History", "season": "Summer", "temperature": "Warm/Mild", "landscape": "City", "modesty": "More modest, strict culture", "population": "Low population/isolated"},
        {"name": "Luxor, Egypt", "budget": "low", "continent": "Africa", "language": "Open to other languages", "reason": "Culture/History", "season": "Winter", "temperature": "Warm/Mild", "landscape": "Rural", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Stellenbosch, South Africa", "budget": "medium", "continent": "Africa", "language": "English-speaking", "reason": "Relaxing", "season": "Fall", "temperature": "Warm/Mild", "landscape": "Rural", "modesty": "Open culture", "population": "Low population/isolated"},

        # ==========================================================
        # EUROPE
        # ==========================================================
        {"name": "Paris, France", "budget": "high", "continent": "Europe", "language": "Open to other languages", "reason": "Culture/History", "season": "Summer", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "London, UK", "budget": "high", "continent": "Europe", "language": "English-speaking", "reason": "Culture/History", "season": "Fall", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Rome, Italy", "budget": "medium", "continent": "Europe", "language": "Open to other languages", "reason": "Culture/History", "season": "Summer", "temperature": "Hot", "landscape": "City", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Istanbul, Turkey", "budget": "low", "continent": "Europe", "language": "Open to other languages", "reason": "Culture/History", "season": "Spring", "temperature": "Warm/Mild", "landscape": "City", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Barcelona, Spain", "budget": "medium", "continent": "Europe", "language": "Open to other languages", "reason": "Adventure", "season": "Summer", "temperature": "Hot", "landscape": "Beach", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Lisbon, Portugal", "budget": "low", "continent": "Europe", "language": "Open to other languages", "reason": "Relaxing", "season": "Spring", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Amsterdam, Netherlands", "budget": "high", "continent": "Europe", "language": "English-speaking", "reason": "Relaxing", "season": "Fall", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Prague, Czech Republic", "budget": "low", "continent": "Europe", "language": "Open to other languages", "reason": "Culture/History", "season": "Winter", "temperature": "Cold", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Athens, Greece", "budget": "low", "continent": "Europe", "language": "Open to other languages", "reason": "Culture/History", "season": "Summer", "temperature": "Hot", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Berlin, Germany", "budget": "medium", "continent": "Europe", "language": "Open to other languages", "reason": "Adventure", "season": "Fall", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Reykjavik, Iceland", "budget": "high", "continent": "Europe", "language": "English-speaking", "reason": "Adventure", "season": "Winter", "temperature": "Cold", "landscape": "Rural", "modesty": "Open culture", "population": "Low population/isolated"},

        # ==========================================================
        # SOUTH AMERICA
        # ==========================================================
        {"name": "Buenos Aires, Argentina", "budget": "medium", "continent": "South America", "language": "Open to other languages", "reason": "Culture/History", "season": "Spring", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Rio de Janeiro, Brazil", "budget": "high", "continent": "South America", "language": "Open to other languages", "reason": "Relaxing", "season": "Summer", "temperature": "Hot", "landscape": "Beach", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "La Paz, Bolivia", "budget": "low", "continent": "South America", "language": "Open to other languages", "reason": "Adventure", "season": "Winter", "temperature": "Cold", "landscape": "Mountain", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Santiago, Chile", "budget": "medium", "continent": "South America", "language": "Open to other languages", "reason": "Adventure", "season": "Fall", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Cusco, Peru", "budget": "low", "continent": "South America", "language": "Open to other languages", "reason": "Culture/History", "season": "Winter", "temperature": "Warm/Mild", "landscape": "Mountain", "modesty": "More modest, strict culture", "population": "Low population/isolated"},
        {"name": "Cartagena, Colombia", "budget": "medium", "continent": "South America", "language": "Open to other languages", "reason": "Relaxing", "season": "Winter", "temperature": "Hot", "landscape": "Beach", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Quito, Ecuador", "budget": "low", "continent": "South America", "language": "Open to other languages", "reason": "Culture/History", "season": "Summer", "temperature": "Warm/Mild", "landscape": "Mountain", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Montevideo, Uruguay", "budget": "medium", "continent": "South America", "language": "Open to other languages", "reason": "Relaxing", "season": "Fall", "temperature": "Warm/Mild", "landscape": "Beach", "modesty": "Open culture", "population": "Low population/isolated"},
        {"name": "Medellín, Colombia", "budget": "low", "continent": "South America", "language": "Open to other languages", "reason": "Adventure", "season": "Spring", "temperature": "Warm/Mild", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
    
        # ==========================================================
        # ASIA
        # ==========================================================
        {"name": "Tokyo, Japan", "budget": "high", "continent": "Asia", "language": "Open to other languages", "reason": "Culture/History", "season": "Spring", "temperature": "Warm/Mild", "landscape": "City", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Bangkok, Thailand", "budget": "low", "continent": "Asia", "language": "Open to other languages", "reason": "Adventure", "season": "Winter", "temperature": "Hot", "landscape": "City", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Bali, Indonesia", "budget": "low", "continent": "Asia", "language": "Open to other languages", "reason": "Relaxing", "season": "Summer", "temperature": "Hot", "landscape": "Beach", "modesty": "Open culture", "population": "Low population/isolated"},
        {"name": "Seoul, South Korea", "budget": "high", "continent": "Asia", "language": "Open to other languages", "reason": "Adventure", "season": "Fall", "temperature": "Warm/Mild", "landscape": "City", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Singapore, Singapore", "budget": "high", "continent": "Asia", "language": "English-speaking", "reason": "Culture/History", "season": "Spring", "temperature": "Hot", "landscape": "City", "modesty": "Open culture", "population": "High population/busy"},
        {"name": "Hanoi, Vietnam", "budget": "low", "continent": "Asia", "language": "Open to other languages", "reason": "Culture/History", "season": "Spring", "temperature": "Warm/Mild", "landscape": "City", "modesty": "More modest, strict culture", "population": "High population/busy"},
        {"name": "Kyoto, Japan", "budget": "medium", "continent": "Asia", "language": "Open to other languages", "reason": "Culture/History", "season": "Fall", "temperature": "Warm/Mild", "landscape": "City", "modesty": "More modest, strict culture", "population": "Low population/isolated"},
        {"name": "Luang Prabang, Laos", "budget": "low", "continent": "Asia", "language": "Open to other languages", "reason": "Relaxing", "season": "Winter", "temperature": "Warm/Mild", "landscape": "Rural", "modesty": "More modest, strict culture", "population": "Low population/isolated"}    
    
    ]

    return destinations



# ==========================================================
# SECTION 3 - INFERENCE ENGINE / SCORING LOGIC
# (Person 3 Responsible)
# ==========================================================

def calculate_score(user_preferences, destination):
    """
    Compare user preferences with destination attributes.
    We use a scoring system where budget is heavily weighted 
    to prevent recommending expensive trips to low-budget users.
    """
    score = 0
    
    # Weights: Budget and Continent are usually the most important "dealbreakers"
    weights = {
        "budget": 10,      #prioritize budget match
        "continent": 5,    #prioritize continent
        "language": 2,
        "reason": 2,
        "season": 1,
        "temperature": 1,
        "landscape": 2,
        "modesty": 1,
        "population": 1
    }

    for key, weight in weights.items():
        if user_preferences.get(key) == destination.get(key):
            score += weight

    return score


def rank_destinations(user_preferences, destinations):
    """
    Finds the destination with the highest match score.
    """
    best_destination = None
    highest_score = -1

    for destination in destinations:
        current_score = calculate_score(user_preferences, destination)
        if current_score > highest_score:
            highest_score = current_score
            best_destination = destination

    return best_destination, highest_score


def explain_recommendation(best_destination, score, user_preferences):
    """
    Displays the recommendation and explains the match.
    """
    # Total possible points is 25 based on the weights above
    max_possible = 25
    match_percentage = (score / max_possible) * 100

    print("\n" + "="*60)
    print("OUR RECOMMENDATION FOR YOU")
    print("="*60)
    
    if best_destination:
        print(f"Based on your preferences, we recommend: {best_destination['name']}!")
        print(f"Match Score: {match_percentage:.1f}%")
        print("\nWhy we chose this for you:")
        
        # --- WHAT MATCHES ---
    print("\n WHAT MATCHES:")
    if user_preferences['budget'] == best_destination['budget']:
        print(f"- Budget: It is a {best_destination['budget']} budget destination.")
    if user_preferences['continent'] == best_destination['continent']:
        print(f"- Continent: It is in {best_destination['continent']}.")
    if user_preferences['language'] == best_destination['language']:
        print(f"- Language: It is {best_destination['language']}.")
    if user_preferences['reason'] == best_destination['reason']:
        print(f"- Goal: It is perfect for {best_destination['reason']}.")
    if user_preferences['landscape'] == best_destination['landscape']:
        print(f"- Landscape: It has a {best_destination['landscape']} landscape.")
    if user_preferences['season'] == best_destination['season']:
        print(f"- Season: The timing matches your preference for {best_destination['season']}.")
    if user_preferences['temperature'] == best_destination['temperature']:
        print(f"- Weather: It features {best_destination['temperature']} weather.")
    if user_preferences['modesty'] == best_destination['modesty']:
        print(f"- Culture: It has a {best_destination['modesty']} environment.")
    if user_preferences['population'] == best_destination['population']:
        print(f"- Vibe: It matches your {best_destination['population']} preference.")

    # --- WHAT IS DIFFERENT ---
    print("\n WHAT IS DIFFERENT:")
    if user_preferences['budget'] != best_destination['budget']:
        print(f"- Budget: You wanted {user_preferences['budget']}, but this is {best_destination['budget']}.")
    if user_preferences['continent'] != best_destination['continent']:
        print(f"- Continent: You wanted {user_preferences['continent']}, but this is in {best_destination['continent']}.")
    if user_preferences['language'] != best_destination['language']:
        print(f"- Language: You preferred {user_preferences['language']}, but it is {best_destination['language']}.")
    if user_preferences['reason'] != best_destination['reason']:
        print(f"- Goal: You wanted {user_preferences['reason']}, but this is better for {best_destination['reason']}.")
    if user_preferences['landscape'] != best_destination['landscape']:
        print(f"- Landscape: You wanted {user_preferences['landscape']}, but it is {best_destination['landscape']}.")
    if user_preferences['season'] != best_destination['season']:
        print(f"- Season: You preferred {user_preferences['season']}, but this is best in {best_destination['season']}.")
    if user_preferences['temperature'] != best_destination['temperature']:
        print(f"- Weather: You wanted {user_preferences['temperature']} weather, but it is typically {best_destination['temperature']}.")
    if user_preferences['modesty'] != best_destination['modesty']:
        print(f"- Culture: You picked {user_preferences['modesty']}, but this is a {best_destination['modesty']} area.")
    if user_preferences['population'] != best_destination['population']:
        print(f"- Vibe: You wanted a {user_preferences['population']} vibe, but it is {best_destination['population']}.")
    
    print("="*60 + "\n")



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
    explain_recommendation(best_destination, score, user_preferences)

    # 6. Save user data to CSV
    save_user_data(user_preferences)


if __name__ == "__main__":
    main()
