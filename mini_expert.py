############################################################
# Travel Recommendation Mini Expert System
# CSC 330: Intro to AI/ML
# Kayla Council, Gabrielle Olds, & Chloe Washington
############################################################


# ==========================================================
# SECTION 1 - USER INTERFACE & DATA COLLECTION
# Kayla Council
# ==========================================================

def show_intro():
    """
    Display welcome message.
    Explain what the system does.
    Inform user they will answer 10 questions.
    """
    pass


def get_valid_input(prompt, options):
    """
    Display numbered options.
    Validate user input using a loop.
    Return selected value.
    """
    pass


def collect_user_preferences():
    """
    Ask all 10 questions.
    Store responses in a dictionary.
    Return user_preferences.
    """

    user_preferences = {}

    # 1. Budget range
    # user_preferences["budget"] = ?

    # 2. Continent
    # user_preferences["continent"] = ?

    # 3. Language Comfort
    # user_preferences["language"] = ?

    # 4. Reason for travel
    # user_preferences["reason"] = ?

    # 5. Preferred Season
    # user_preferences["season"] = ?

    # 6. Temperature Preference
    # user_preferences["temperature"] = ?

    # 7. Preferred Landscape
    # user_preferences["landscape"] = ?

    # 8. Modesty Preference
    # user_preferences["modesty"] = ?

    # 9. Population Preference
    # user_preferences["population"] = ?

    # 10. Group Size (Collected but NOT used in scoring)
    # user_preferences["group_size"] = ?

    return user_preferences


def save_user_data(user_preferences):
    """
    Append user data to a CSV file.
    Save for future analysis.
    """
    pass



# ==========================================================
# SECTION 2 - KNOWLEDGE BASE (DESTINATIONS)
# (Person 2 Responsible)
# ==========================================================

def load_destinations():
    """
    Create and return a list of destinations.
    Each destination must include attributes that
    match the scoring questions.
    (Group size is NOT included here.)
    """

    destinations = [

        {
            "name": "",
            "budget": "",
            "continent": "",
            "language": "",
            "reason": "",
            "season": "",
            "temperature": "",
            "landscape": "",
            "modesty": "",
            "population": ""
        },

        # Add more destinations here (at least 10)

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
