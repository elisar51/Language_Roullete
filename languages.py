import json
import random
import os

# The topics and languages of the roulete
languages = ("Arabic", "English", "German")
#saved topics in JSON
with open("topics.json", "r") as file:
    topics = json.load(file)
activities = ("Speaking", "Writing")
if os.path.exists("topic_status.json"):
    with open("topic_status.json", "r") as file:
        topic_status = json.load(file)
else:
    topic_status = {}

    for language in languages:
        topic_status[language] = {}

        for topic in topics:
            topic_status[language][topic] = {
                "Writing": False,
                "Speaking": False
            }
# defining a function to count the remaining and return it to the program to be saved
def count_remaining(topic_status):
    remaining = 0

    for language in languages:
        for topic in topics:
            for activity in activities:
                if not topic_status[language][topic][activity]:
                    remaining += 1
                    
                    

    return remaining

remaining = count_remaining(topic_status)

# So the program doesnt keep running and tracing back, when all topics are done the program says that

if remaining == 0:
    print("🎉 You completed all your Language Roulette combinations!")
    exit()

#Here the roullette happens after making sure it wasnt chosen before
# And returning the chosen one to the program

def choose_combination(languages, topics, activities, topic_status):
    while True:
        language = random.choice(languages)
        topic = random.choice(topics)
        activity = random.choice(activities)

        if not topic_status[language][topic][activity]:
            break

    return language, topic, activity
language, topic, activity = choose_combination (languages, topics, activities, topic_status)

topic_status[language][topic][activity] = True

# open file, and chnage into what was chosen and save
# defining a new function to save the status 
def save_status(topic_status):
    with open("topic_status.json", "w") as file: 
        json.dump(topic_status, file, indent=4)
save_status(topic_status)

# print out to the user what is the topic and language this time
# We then defined one function to display the results rather than having severla prints
def display_result(language, topic, activity):
    print("🌍 LANGUAGE ROULETTE 🌍")
    print("Today's language is:", language)
    print("Your Topic is:", topic)
    print("Your Activity is:", activity)
    print("Now go do your research!")
display_result(language, topic, activity)
