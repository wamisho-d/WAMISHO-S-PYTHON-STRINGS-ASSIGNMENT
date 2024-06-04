# Question 1 Task 1:  Keyword Highlighter

keywords = ["good", "excellent", "bad", "poor", "average"]
def keyword_highlighter(reviews, keywords):
    highlighted_reviews = []
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper()) 
            highlighted_reviews.append(review)
            return highlighted_reviews
        highlighted_reviews = highlight_keywords(review, keywords) # type: ignore
        for review in highlighted_reviews:
            print(review)

# Question 1 Task 2: Sentiment Tally
def sentiment_tally (reviews, positive_words, negative_words):
    sentiment_counts = []
    for review in reviews:
        positive_count = sum(review.lower().count(word) for word in positive_words)
        negative_count = sum(review.lower().count(word)for word in negative_words)
        sentiment_counts.append((positive_count,negative_count))
        return sentiment_counts
    sentiment_counts = sentiment_tally(reviews, positive_words,negative_words)
    for i,(pos,neg) in enumerate(sentiment_counts):
        print(f"Review {i+1}: {pos} positive words, {neg} negative words")

# Question 1 Task 3: Review Summary
def create_a_summary(review, length = 30):
    if len(review) <= length:
        return review
    else:
        end = review.rfind('',0)

# Question 2 Task 1: Input Length Validator
def validate_name(first_name, last_name):
    if len(first_name) >= 2 or len(last_name) >= 2:
        print("Name Validation Passed")
    else:
        print("Error: Both should be at least 2 characters long")

# Question 2 Task 2: Password Complexity Checker
import re
def check_password_complexity(password):
    if len(password) < 8:
        print("The password must be at least 8 characters long")
    elif not re.search("[a-z], password"):
        print("The password must contain at least one lowercase letter.")
    elif not re.search("[A-Z], password"):
        print("The password must contain at least one uppercase letter.")
    elif not re.search("[0-9], password"):
         print("The password must contain at least one number.")
    else:
        print("The password complexity is an adequate")

# Question 2 Task 3: Email Formatter
def format_email(email):
    formatted_email = email.lower()
    print("Formatted email:", formatted_email)

# Question 3 Task 1: Command Parser
def command_parser(user_input):
    commands = {"help": "How may I assist you today?",
        "issue": "Please describe your problem in detail.",
        "contact support": "You could contact support at support@example.com."
    }

    for command in commands:
        if command in user_input.lower():
            print(commands[command])
            return
        print("command is not recognized. please try again")

# Question 3 Task 2: Issue Categorizer
def issue_categorizer(user_input):
    categories = {"login": "Login Issue",
        "performance": "Performance Issue",
        "error": "Error Issue"
    }
    if "issue" in user_input.lower():
        for keyword, category in categories.items():
            if keyword in user_input.lower():
                print(f"Issue Category: {category}")
                return
                print(f"Issue Category: Ultimate Issue")
            else:
                print("No issue found in the input")


            




    
    
        


      






