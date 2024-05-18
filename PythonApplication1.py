import numpy
import pandas as pd
import csv
import copy
import statistics
import math

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = "C:/Users/thana/Desktop/University/Year3/AI/sid2029975/Akinator/Footballers.csv"


# Use the read_csv function to import the CSV file into a DataFrame
df = pd.read_csv(file_path)
# print(df)


# Create an empty database to add all the elements from the excel file
database = [

]

# Reading each line of the database and writing it in 'new'
for i in range(0, 18278):
    new = {'sofifa_id': df.at[i, "sofifa_id"], 'player_url': df.at[i, "player_url"], 'short_name': df.at[i, "short_name"],
         'age': df.at[i, "age"], 'height_cm': df.at[i, "height_cm"], 'preferred_foot': df.at[i, "preferred_foot"], "value_eur":df.at[i, "value_eur"]
        , 'real_face': df.at[i, "real_face"], 'weight_kg': df.at[i, "weight_kg"], 'club': df.at[i, "club"], 'pace': df.at[i, "pace"]
           , 'shooting': df.at[i, "shooting"], 'passing': df.at[i, "passing"], 'attacking_crossing': df.at[i, "attacking_crossing"]
           , 'defending_marking': df.at[i, "defending_marking"], 'power_strength': df.at[i, "power_strength"]
           , 'international_reputation': df.at[i, "international_reputation"], 'weak_foot': df.at[i, "weak_foot"]}

    # Appends the 'new' dataframe to the 'database'
    database.append(new)
    #database.remove(new)



# Welcoming the user
print("Welcome to Football Akinator!")
print()

# Create an empty database to add all the elements that will be removed
removed = [

]

# Create an empty database to add all the elements that will be removed (based on probably/probably not answers)
probRemoved = [

]

def removedAppend():
    new = {'sofifa_id': df.at[i, "sofifa_id"], 'player_url': df.at[i, "player_url"],
         'short_name': df.at[i, "short_name"],
         'age': df.at[i, "age"], 'height_cm': df.at[i, "height_cm"],
         'preferred_foot': df.at[i, "preferred_foot"], 'value_eur': df.at[i, "value_eur"], 'real_face': df.at[i, "real_face"]
           , 'weight_kg': df.at[i, "weight_kg"], 'club': df.at[i, "club"], 'pace': df.at[i, "pace"]
           , 'shooting': df.at[i, "shooting"], 'passing': df.at[i, "passing"], 'attacking_crossing': df.at[i, "attacking_crossing"]
           , 'defending_marking': df.at[i, "defending_marking"], 'power_strength': df.at[i, "power_strength"]
           , 'international_reputation': df.at[i, "international_reputation"], 'weak_foot': df.at[i, "weak_foot"]}

    # Avoiding Duplicates and appending the player
    if new not in removed:
        removed.append(new)
    else:
        pass


def probRemovedAppend():
    new = {'sofifa_id': df.at[i, "sofifa_id"], 'player_url': df.at[i, "player_url"],
         'short_name': df.at[i, "short_name"],
         'age': df.at[i, "age"], 'height_cm': df.at[i, "height_cm"],
         'preferred_foot': df.at[i, "preferred_foot"], 'value_eur': df.at[i, "value_eur"], 'real_face': df.at[i, "real_face"]
           , 'weight_kg': df.at[i, "weight_kg"], 'club': df.at[i, "club"], 'pace': df.at[i, "pace"]
           , 'shooting': df.at[i, "shooting"], 'passing': df.at[i, "passing"], 'attacking_crossing': df.at[i, "attacking_crossing"]
           , 'defending_marking': df.at[i, "defending_marking"], 'power_strength': df.at[i, "power_strength"]
           , 'international_reputation': df.at[i, "international_reputation"], 'weak_foot': df.at[i, "weak_foot"]}

    # Avoiding Duplicates and appending the player
    if new not in probRemoved:
        probRemoved.append(new)
    else:
        pass

def checker():
    # checking for non existing elements
    for i in removed:
        if i in database:
            database.remove(i)
        else:
            pass

    if len(database) == 1:
        print("found him!")
        print(database)


# QUESTION 1
# Preferred Foot
# If the preferred foot is right add all left-footed players in the "removed" list
preferredFoot = input("Is the player right footed?")
if preferredFoot == 'y':
    for i in range(0, len(database)):
        if df.at[i, "preferred_foot"] != "Right":
            removedAppend()

# If the preferred foot is left add all right-footed players in the "removed" list
if preferredFoot == 'n':
    for i in range(0, len(database)):
        if df.at[i, "preferred_foot"] != "Left":
            removedAppend()

# If the preferred foot is right add all left-footed players in the "probRemoved" list
if preferredFoot == 'probably':
    for i in range(0, len(database)):
        if df.at[i, "preferred_foot"] != "Right":
            probRemovedAppend()

# If the preferred foot is left add all right-footed players in the "probRemoved" list
if preferredFoot == 'probably not':
    for i in range(0, len(database)):
        if df.at[i, "preferred_foot"] != "Left":
            probRemovedAppend()



# QUESTION 2 and QUESTION 3
# Height
# if Height is 181 or more (>=181) cm remove all the players below 181 (<181)
height_cm = input("Is the player 181cm or over?")
if height_cm == 'y':
    for i in range(0, len(database)):
        if df.at[i, "height_cm"] < 181:
            removedAppend()
        else:
            playerValue = ''

    height_cm = input("Is the player 190cm or over?")
    if height_cm == 'y':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] < 190:
                removedAppend()
                height_cm = ''
            else:
                playerValue = ''

    if height_cm == 'n':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] >= 190:
                removedAppend()
                height_cm = ''
            else:
                playerValue = ''

    if height_cm == 'probably':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] < 190:
                probRemovedAppend()
                height_cm = ''
            else:
                playerValue = ''

    if height_cm == 'probably not':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] >= 190:
                probRemovedAppend()
                height_cm = ''
            else:
                playerValue = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if height_cm == 'n':
    for i in range(0, len(database)):
        if df.at[i, "height_cm"] >= 181:
            removedAppend()
        else:
            playerValue = ''

    height_cm = input("Is the player 175cm or over?")
    if height_cm == 'y':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] < 175:
                removedAppend()
                height_cm = ''
            else:
                playerValue = ''

    if height_cm == 'n':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] >= 175:
                removedAppend()
                height_cm =''
            else:
                playerValue = ''

    if height_cm == 'probably':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] < 175:
                probRemovedAppend()
                height_cm = ''
            else:
                playerValue = ''

    if height_cm == 'probably not':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] >= 175:
                probRemovedAppend()
                height_cm =''
            else:
                playerValue = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if height_cm == 'probably':
    for i in range(0, len(database)):
        if df.at[i, "height_cm"] < 181:
            probRemovedAppend()
        else:
            playerValue = ''

    height_cm = input("Is the player 190cm or over?")
    if height_cm == 'probably':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] < 190:
                probRemovedAppend()
                height_cm = ''
            else:
                playerValue = ''

    if height_cm == 'probably not':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] >= 190:
                probRemovedAppend()
                height_cm =''
            else:
                playerValue = ''

    if height_cm == 'y':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] < 190:
                removedAppend()
                height_cm = ''
            else:
                playerValue = ''

    if height_cm == 'n':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] >= 190:
                removedAppend()
                height_cm = ''
            else:
                playerValue = ''



# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if height_cm == 'probably not':
    for i in range(0, len(database)):
        if df.at[i, "height_cm"] >= 181:
            probRemovedAppend()
        else:
            playerValue = ''

    height_cm = input("Is the player 175cm or over?")
    if height_cm == 'probably':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] < 175:
                probRemovedAppend()
                height_cm = ''
            else:
                playerValue = ''

    if height_cm == 'probably not':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] >= 175:
                probRemovedAppend()
                height_cm =''
            else:
                playerValue = ''

    if height_cm == 'y':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] < 175:
                removedAppend()
                height_cm = ''
            else:
                playerValue = ''

    if height_cm == 'n':
        for i in range(0, len(database)):
            if df.at[i, "height_cm"] >= 175:
                removedAppend()
                height_cm =''
            else:
                playerValue = ''

# checker()


# QUESTION 4
# average value eur: 2484038| median is 700000
playerValue = input('Is the players value 700000 or over?')

if playerValue == 'y':
    for i in range(0, len(database)):
        if df.at[i, "value_eur"] < 700000:
            removedAppend()
        else:
            playerValue = ''

    playerValue = input('Is the players value 2100000 or over?')
    if playerValue == 'y':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] < 2100000:
                removedAppend()
                playerValue = ''
            else:
                playerValue = ''

    if playerValue == 'n':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] >= 2100000:
                removedAppend()
                playerValue = ''
            else:
                playerValue = ''


    if playerValue == 'probably':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] < 2100000:
                probRemovedAppend()
                playerValue = ''
            else:
                playerValue = ''

    if playerValue == 'probably not':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] >= 2100000:
                probRemovedAppend()
                playerValue = ''
            else:
                playerValue = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerValue == 'n':
    for i in range(0, len(database)):
        if df.at[i, "value_eur"] >= 700000:
            removedAppend()

    playerValue = input("Is the players value 325000 or over?")
    if playerValue == 'y':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] < 325000:
                removedAppend()
                playerValue = ''

    if playerValue == 'n':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] >= 325000:
                removedAppend()
                playerValue =''

    if playerValue == 'probably':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] < 325000:
                probRemovedAppend()
                playerValue = ''

    if playerValue == 'probably not':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] >= 325000:
                probRemovedAppend()
                playerValue =''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerValue == 'probably':
    for i in range(0, len(database)):
        if df.at[i, "value_eur"] < 700000:
            probRemovedAppend()

    playerValue = input("Is the players value 2100000 or over?")
    if playerValue == 'probably':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] < 2100000:
                probRemovedAppend()
                playerValue = ''
                print('I AM HERE')

    if playerValue == 'probably not':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] >= 2100000:
                probRemovedAppend()
                playerValue =''

    if playerValue == 'y':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] < 2100000:
                removedAppend()
                playerValue = ''

    if playerValue == 'n':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] >= 2100000:
                removedAppend()
                playerValue = ''



# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerValue == 'probably not':
    for i in range(0, len(database)):
        if df.at[i, "value_eur"] >= 700000:
            probRemovedAppend()

    playerValue = input("Is the players value 325000 or over?")
    if playerValue == 'probably':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] < 325000:
                probRemovedAppend()

    if playerValue == 'probably not':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] >= 325000:
                probRemovedAppend()
                playerValue =''

    if playerValue == 'y':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] < 325000:
                removedAppend()
                playerValue = ''

    if playerValue == 'n':
        for i in range(0, len(database)):
            if df.at[i, "value_eur"] >= 325000:
                removedAppend()
                playerValue =''

# checker()


# Question 5
# Real face or not
realFace = input("Is the player real?")
if realFace == 'y':
    for i in range(0, len(database)):
        if df.at[i, "real_face"] != "Yes":
            removedAppend()

# If the preferred foot is left add all right-footed players in the "removed" list
if realFace == 'n':
    for i in range(0, len(database)):
        if df.at[i, "real_face"] != "No":
            removedAppend()

# If the preferred foot is right add all left-footed players in the "probRemoved" list
if realFace == 'probably':
    for i in range(0, len(database)):
        if df.at[i, "preferred_foot"] != "Yes":
            probRemovedAppend()

# If the preferred foot is left add all right-footed players in the "probRemoved" list
if realFace == 'probably not':
    for i in range(0, len(database)):
        if df.at[i, "preferred_foot"] != "No":
            probRemovedAppend()

# Remove duplicates from the two databases (removed, probRemoved)
for i in removed:
    if i in probRemoved:
        probRemoved.remove(i)
    else:
        pass

# checker()


# QUESTION 6 and 7
# AGE

# Finding median age and removing all the "removed" elements from "database"
def findMedianAge():

    global median
    global median2
    # Removing the "removed" elements from the "database"
    # Removing only from the "removed" and not from "probRemoved" too. Because if we remove from both of them it could lead to not finding the player
    #(The probRemoved are not certain and could misslead the rest of the algorithm)
    for i in removed:
        if i in database:
            database.remove(i)
        else:
            pass

    # Creating a duplicate database for "probRemoved" operations to be done inside it.
    global database2
    database2 = copy.deepcopy(database)

    # # Removing the "probRemoved" and "removed" elements from the "database2".
    for i in removed:
        if i in database2:
            database.remove(i)
        else:
            pass

    for i in probRemoved:
        if i in database2:
            database2.remove(i)
        else:
            pass

    # Taking the age from the remaining players, sorting it and finding the median. (For "probRemoved")
    list2 = []
    for i in database2:
        list2.append(i['age'])
    list2 = sorted(list2)

    # Finding the "median2"
    median2 = (len(list2)/2).__round__()
    if median2 != 0:
        median2 = list2[median2 - 1]
    else:
        pass


    # Taking the age from the remaining players, sorting it and finding the median. (For "removed")

    list = []
    for i in database:
        list.append(i['age'])
    list = sorted(list)

    # Finding the median
    median = (len(list)/2).__round__()
    if median != 0:
        median = list[median-1]
    else:
        pass

findMedianAge()

# Performing the questions
# NOTE: If the user answers "probably" or "probably not" the calculations of the median will be performed in a duplicate of "database".
# This way it will not interfere with the final result.
playerAge = input('Is the players age '+ str(median) + ' or over?')

if playerAge == 'y':
    for i in database:
        if i['age'] < median:
            removed.append(i)
        else:
            playerAge = ''

    findMedianAge()
    playerAge = input('Is the players age '+ str(median) + ' or over?')

    if playerAge == 'y':
        for i in database:
            if i['age'] < median:
                removed.append(i)
            else:
                playerAge = ''

    if playerAge == 'n':
        for i in database:
            if i['age'] >= median:
                removed.append(i)
            else:
                playerAge = ''

    if playerAge == 'probably':
        for i in range(0, len(database)):
            for i in database:
                if i['age'] < median:
                    probRemoved.append(i)
                else:
                    playerAge = ''

    if playerAge == 'probably not':
        for i in range(0, len(database)):
            for i in database:
                if i['age'] >= median:
                    probRemoved.append(i)
                else:
                    playerAge = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerAge == 'n':
    for i in database:
        if i['age'] >= median:
            removed.append(i)
        else:
            playerAge = ''
    findMedianAge()
    playerAge = input('Is the players age '+ str(median) + ' or over?')
    if playerAge == 'y':
        for i in database:
            if i['age'] < median:
                removed.append(i)
            else:
                playerAge = ''

    if playerAge == 'n':
        for i in database:
            if i['age'] >= median:
                removed.append(i)
            else:
                playerAge = ''

    if playerAge == 'probably':
        for i in range(0, len(database)):
            for i in database:
                if i['age'] < median:
                    probRemoved.append(i)
                else:
                    playerAge = ''

    if playerAge == 'probably not':
        for i in range(0, len(database)):
            for i in database:
                if i['age'] >= median:
                    probRemoved.append(i)
                else:
                    playerAge = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerAge == 'probably':
    for i in database:
        if i['age'] < median:
            removed.append(i)
        else:
            playerAge = ''
    findMedianAge()
    playerAge = input('Is the players age '+ str(median2) + ' or over?')
    if playerAge == 'probably':
        for i in database:
            if i['age'] < median2:
                removed.append(i)
            else:
                playerAge = ''

    if playerAge == 'probably not':
        for i in database:
            if i['age'] >= median2:
                removed.append(i)
            else:
                playerAge = ''

    if playerAge == 'y':
        for i in database:
            if i['age'] < median2:
                removed.append(i)
            else:
                playerAge = ''

    if playerAge == 'n':
        for i in database:
            if i['age'] >= median2:
                removed.append(i)
            else:
                playerAge = ''



# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerAge == 'probably not':
    for i in database:
        if i['age'] >= median:
            removed.append(i)
        else:
            playerAge = ''
    findMedianAge()
    playerAge = input('Is the players age '+ str(median2) + ' or over?')
    if playerAge == 'probably':
        for i in database:
            if i['age'] < median2:
                removed.append(i)
            else:
                playerAge = ''

    if playerAge == 'probably not':
        for i in database:
            if i['age'] >= median2:
                removed.append(i)
            else:
                playerAge = ''

    if playerAge == 'y':
        for i in database:
            if i['age'] < median2:
                removed.append(i)
            else:
                playerAge = ''

    if playerAge == 'n':
        for i in database:
            if i['age'] >= median2:
                removed.append(i)
            else:
                playerAge = ''


# Question 8 and 9
# Weight average (75) (min70) (max80)

playerWeight = input("Is the players weight 75kg or over?")
if playerWeight == 'y':
    for i in range(0, len(database)):
        if df.at[i, "weight_kg"] < 75:
            removedAppend()
        else:
            playerWeight = ''

    playerWeight = input("Is the players weight 80kg or over?")
    if playerWeight == 'y':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] < 80:
                removedAppend()
                playerWeight = ''
            else:
                playerWeight = ''

    if playerWeight == 'n':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] >= 80:
                removedAppend()
            else:
                playerWeight = ''

    if playerWeight == 'probably':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] < 80:
                probRemovedAppend()
                playerWeight = ''
            else:
                playerWeight = ''

    if playerWeight == 'probably not':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] >= 80:
                probRemovedAppend()
                playerWeight = ''
            else:
                playerWeight = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerWeight == 'n':
    for i in range(0, len(database)):
        if df.at[i, "weight_kg"] >= 75:
            removedAppend()
        else:
            playerWeight = ''

    playerWeight = input("Is the players weight 70kg or over?")
    if playerWeight == 'y':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] < 70:
                removedAppend()
                playerWeight = ''
            else:
                playerWeight = ''

    if playerWeight == 'n':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] >= 70:
                removedAppend()
                playerWeight =''
            else:
                playerWeight = ''

    if playerWeight == 'probably':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] < 70:
                probRemovedAppend()
                playerWeight = ''
            else:
                playerWeight = ''

    if playerWeight == 'probably not':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] >= 70:
                probRemovedAppend()
                playerWeight =''
            else:
                playerWeight = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerWeight == 'probably':
    for i in range(0, len(database)):
        if df.at[i, "weight_kg"] < 75:
            probRemovedAppend()
        else:
            playerWeight = ''

    playerWeight = input("Is the players weight 80kg or over?")
    if playerWeight == 'probably':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] < 80:
                probRemovedAppend()
                playerWeight = ''
            else:
                playerWeight = ''

    if playerWeight == 'probably not':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] >= 80:
                probRemovedAppend()
                playerWeight =''
            else:
                playerWeight = ''

    if playerWeight == 'y':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] < 80:
                removedAppend()
                playerWeight = ''
            else:
                playerWeight = ''

    if playerWeight == 'n':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] >= 80:
                removedAppend()
                playerWeight = ''
            else:
                playerWeight = ''



# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerWeight == 'probably not':
    for i in range(0, len(database)):
        if df.at[i, "weight_kg"] >= 75:
            probRemovedAppend()
        else:
            playerWeight = ''

    playerWeight = input("Is the players weight 70kg or over?")
    if playerWeight == 'probably':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] < 70:
                probRemovedAppend()
                playerWeight = ''
            else:
                playerWeight = ''

    if playerWeight == 'probably not':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] >= 70:
                probRemovedAppend()
                playerWeight =''
            else:
                playerWeight = ''

    if playerWeight == 'y':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] < 70:
                removedAppend()
                playerWeight = ''
            else:
                playerWeight = ''

    if playerWeight == 'n':
        for i in range(0, len(database)):
            if df.at[i, "weight_kg"] >= 70:
                removedAppend()
                playerWeight =''
            else:
                playerWeight = ''



# Question 10 and 11
# attacking_crossing



def playerAtcCr():

    global median
    global median2
    # Removing the "removed" elements from the "database"
    # Removing only from the "removed" and not from "probRemoved" too. Because if we remove from both of them it could lead to not finding the player
    #(The probRemoved are not certain and could misslead the rest of the algorithm)
    for i in removed:
        if i in database:
            database.remove(i)
        else:
            pass

    # Creating a duplicate database for "probRemoved" operations to be done inside it.
    global database2
    database2 = copy.deepcopy(database)

    # # Removing the "probRemoved" and "removed" elements from the "database2".
    for i in removed:
        if i in database2:
            database.remove(i)
        else:
            pass

    for i in probRemoved:
        if i in database2:
            database2.remove(i)
        else:
            pass

    # Taking the attacking_crossing from the remaining players, sorting it and finding the median. (For "probRemoved")
    list2 = []
    for i in database:
        if (math.isnan(i['attacking_crossing'])) != True:
            list2.append(i['attacking_crossing'])
        else:
            pass
    list2 = sorted(list2)

    # Finding the "median2"
    median2 = (len(list2)/2).__round__()
    if median2 != 0:
        median2 = list2[median2 - 1]
    else:
        pass


    # Taking the attacking_crossing from the remaining players, sorting it and finding the median. (For "removed")

    list = []
    for i in database:
        if (math.isnan(i['attacking_crossing'])) != True:
            list.append(i['attacking_crossing'])
        else:
            pass

    list = sorted(list)
    # Finding the median
    median = (len(list)/2).__round__()
    if median != 0:
        median = list[median-1]
    else:
        pass

playerAtcCr()

# Performing the questions
# NOTE: If the user answers "probably" or "probably not" the calculations of the median will be performed in a duplicate of "database".
# This way it will not interfere with the final result.
playerAtcCross = input('Is the players attacking_crossing '+ str(median) + ' or over?')

if playerAtcCross == 'y':
    for i in database:
        if i['attacking_crossing'] < median:
            removed.append(i)
        else:
            playerAtcCross = ''

    playerAtcCr()

    playerAtcCross = input('Is the players attacking_crossing '+ str(median) + ' or over?')

    if playerAtcCross == 'y':
        for i in database:
            if i['attacking_crossing'] < median:
                removed.append(i)
            else:
                playerAtcCross = ''

    if playerAtcCross == 'n':
        for i in database:
            if i['attacking_crossing'] >= median:
                removed.append(i)
            else:
                playerAtcCross = ''

    if playerAtcCross == 'probably':
        for i in range(0, len(database)):
            for i in database:
                if i['attacking_crossing'] < median:
                    probRemoved.append(i)
                else:
                    playerAtcCross = ''

    if playerAtcCross == 'probably not':
        for i in range(0, len(database)):
            for i in database:
                if i['attacking_crossing'] >= median:
                    probRemoved.append(i)
                else:
                    playerAtcCross = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerAtcCross == 'n':
    for i in database:
        if i['attacking_crossing'] >= median:
            removed.append(i)
        else:
            playerAtcCross = ''
    playerAtcCr()
    playerAtcCross = input('Is the players attacking_crossing '+ str(median) + ' or over?')
    if playerAtcCross == 'y':
        for i in database:
            if i['attacking_crossing'] < median:
                removed.append(i)
            else:
                playerAtcCross = ''

    if playerAtcCross == 'n':
        for i in database:
            if i['attacking_crossing'] >= median:
                removed.append(i)
            else:
                playerAtcCross = ''

    if playerAtcCross == 'probably':
        for i in range(0, len(database)):
            for i in database:
                if i['attacking_crossing'] < median:
                    probRemoved.append(i)
                else:
                    playerAtcCross = ''

    if playerAtcCross == 'probably not':
        for i in range(0, len(database)):
            for i in database:
                if i['attacking_crossing'] >= median:
                    probRemoved.append(i)
                else:
                    playerAtcCross = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerAtcCross == 'probably':
    for i in database:
        if i['attacking_crossing'] < median:
            removed.append(i)
        else:
            playerAtcCross = ''
    playerAtcCr()
    playerAtcCross = input('Is the players attacking_crossing '+ str(median2) + ' or over?')
    if playerAtcCross == 'probably':
        for i in database:
            if i['attacking_crossing'] < median2:
                removed.append(i)
            else:
                playerAtcCross = ''

    if playerAtcCross == 'probably not':
        for i in database:
            if i['attacking_crossing'] >= median2:
                removed.append(i)
            else:
                playerAtcCross = ''

    if playerAtcCross == 'y':
        for i in database:
            if i['attacking_crossing'] < median2:
                removed.append(i)
            else:
                playerAtcCross = ''

    if playerAtcCross == 'n':
        for i in database:
            if i['attacking_crossing'] >= median2:
                removed.append(i)
            else:
                playerAtcCross = ''



# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerAtcCross == 'probably not':
    for i in database:
        if i['attacking_crossing'] >= median:
            removed.append(i)
        else:
            playerAtcCross = ''
    playerAtcCr()
    playerAtcCross = input('Is the players attacking_crossing '+ str(median2) + ' or over?')
    if playerAtcCross == 'probably':
        for i in database:
            if i['attacking_crossing'] < median2:
                removed.append(i)
            else:
                playerAtcCross = ''

    if playerAtcCross == 'probably not':
        for i in database:
            if i['attacking_crossing'] >= median2:
                removed.append(i)
            else:
                playerAtcCross = ''

    if playerAtcCross == 'y':
        for i in database:
            if i['attacking_crossing'] < median2:
                removed.append(i)
            else:
                playerAtcCross = ''

    if playerAtcCross == 'n':
        for i in database:
            if i['attacking_crossing'] >= median2:
                removed.append(i)
            else:
                playerAtcCross = ''




# Question 12 and 13
# defending_marking

def playerDefMar():

    global median
    global median2
    # Removing the "removed" elements from the "database"
    # Removing only from the "removed" and not from "probRemoved" too. Because if we remove from both of them it could lead to not finding the player
    #(The probRemoved are not certain and could misslead the rest of the algorithm)
    for i in removed:
        if i in database:
            database.remove(i)
        else:
            pass

    # Creating a duplicate database for "probRemoved" operations to be done inside it.
    global database2
    database2 = copy.deepcopy(database)

    # # Removing the "probRemoved" and "removed" elements from the "database2".
    for i in removed:
        if i in database2:
            database.remove(i)
        else:
            pass

    for i in probRemoved:
        if i in database2:
            database2.remove(i)
        else:
            pass

    # Taking the defending_marking from the remaining players, sorting it and finding the median. (For "probRemoved")
    list2 = []
    for i in database:
        if (math.isnan(i['defending_marking'])) != True:
            list2.append(i['defending_marking'])
        else:
            pass
    list2 = sorted(list2)

    # Finding the "median2"
    median2 = (len(list2)/2).__round__()
    if median2 != 0:
        median2 = list2[median2 - 1]
    else:
        pass


    # Taking the defending_marking from the remaining players, sorting it and finding the median. (For "removed")

    list = []
    for i in database:
        if (math.isnan(i['defending_marking'])) != True:
            list.append(i['defending_marking'])
        else:
            pass

    list = sorted(list)
    # Finding the median
    median = (len(list)/2).__round__()
    if median != 0:
        median = list[median-1]
    else:
        pass

playerDefMar()

# Performing the questions
# NOTE: If the user answers "probably" or "probably not" the calculations of the median will be performed in a duplicate of "database".
# This way it will not interfere with the final result.
playerDefMarking = input('Is the players defending_marking '+ str(median) + ' or over?')

if playerDefMarking == 'y':
    for i in database:
        if i['defending_marking'] < median:
            removed.append(i)
        else:
            playerDefMarking = ''

    playerDefMar()

    playerDefMarking = input('Is the players defending_marking '+ str(median) + ' or over?')

    if playerDefMarking == 'y':
        for i in database:
            if i['defending_marking'] < median:
                removed.append(i)
            else:
                playerDefMarking = ''

    if playerDefMarking == 'n':
        for i in database:
            if i['defending_marking'] >= median:
                removed.append(i)
            else:
                playerDefMarking = ''

    if playerDefMarking == 'probably':
        for i in range(0, len(database)):
            for i in database:
                if i['defending_marking'] < median:
                    probRemoved.append(i)
                else:
                    playerDefMarking = ''

    if playerDefMarking == 'probably not':
        for i in range(0, len(database)):
            for i in database:
                if i['defending_marking'] >= median:
                    probRemoved.append(i)
                else:
                    playerDefMarking = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerDefMarking == 'n':
    for i in database:
        if i['defending_marking'] >= median:
            removed.append(i)
        else:
            playerDefMarking = ''
    playerDefMar()
    playerDefMarking = input('Is the players defending_marking '+ str(median) + ' or over?')
    if playerDefMarking == 'y':
        for i in database:
            if i['defending_marking'] < median:
                removed.append(i)
            else:
                playerDefMarking = ''

    if playerDefMarking == 'n':
        for i in database:
            if i['defending_marking'] >= median:
                removed.append(i)
            else:
                playerDefMarking = ''

    if playerDefMarking == 'probably':
        for i in range(0, len(database)):
            for i in database:
                if i['defending_marking'] < median:
                    probRemoved.append(i)
                else:
                    playerDefMarking = ''

    if playerDefMarking == 'probably not':
        for i in range(0, len(database)):
            for i in database:
                if i['defending_marking'] >= median:
                    probRemoved.append(i)
                else:
                    playerDefMarking = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerDefMarking == 'probably':
    for i in database:
        if i['defending_marking'] < median:
            removed.append(i)
        else:
            playerDefMarking = ''
    playerDefMar()
    playerDefMarking = input('Is the players defending_marking '+ str(median2) + ' or over?')
    if playerDefMarking == 'probably':
        for i in database:
            if i['defending_marking'] < median2:
                removed.append(i)
            else:
                playerDefMarking = ''

    if playerDefMarking == 'probably not':
        for i in database:
            if i['defending_marking'] >= median2:
                removed.append(i)
            else:
                playerDefMarking = ''

    if playerDefMarking == 'y':
        for i in database:
            if i['defending_marking'] < median2:
                removed.append(i)
            else:
                playerDefMarking = ''

    if playerDefMarking == 'n':
        for i in database:
            if i['defending_marking'] >= median2:
                removed.append(i)
            else:
                playerDefMarking = ''



# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerDefMarking == 'probably not':
    for i in database:
        if i['defending_marking'] >= median:
            removed.append(i)
        else:
            playerDefMarking = ''
    playerDefMar()
    playerDefMarking = input('Is the players defending_marking '+ str(median2) + ' or over?')
    if playerDefMarking == 'probably':
        for i in database:
            if i['defending_marking'] < median2:
                removed.append(i)
            else:
                playerDefMarking = ''

    if playerDefMarking == 'probably not':
        for i in database:
            if i['defending_marking'] >= median2:
                removed.append(i)
            else:
                playerDefMarking = ''

    if playerDefMarking == 'y':
        for i in database:
            if i['defending_marking'] < median2:
                removed.append(i)
            else:
                playerDefMarking = ''

    if playerDefMarking == 'n':
        for i in database:
            if i['defending_marking'] >= median2:
                removed.append(i)
            else:
                playerDefMarking = ''




# Question 14 and 15
# power_strength

def playerPowerStr():

    global median
    global median2
    # Removing the "removed" elements from the "database"
    # Removing only from the "removed" and not from "probRemoved" too. Because if we remove from both of them it could lead to not finding the player
    #(The probRemoved are not certain and could misslead the rest of the algorithm)
    for i in removed:
        if i in database:
            database.remove(i)
        else:
            pass

    # Creating a duplicate database for "probRemoved" operations to be done inside it.
    global database2
    database2 = copy.deepcopy(database)

    # # Removing the "probRemoved" and "removed" elements from the "database2".
    for i in removed:
        if i in database2:
            database.remove(i)
        else:
            pass

    for i in probRemoved:
        if i in database2:
            database2.remove(i)
        else:
            pass

    # Taking the power_strength from the remaining players, sorting it and finding the median. (For "probRemoved")
    list2 = []
    for i in database:
        if (math.isnan(i['power_strength'])) != True:
            list2.append(i['power_strength'])
        else:
            pass
    list2 = sorted(list2)

    # Finding the "median2"
    median2 = (len(list2)/2).__round__()
    if median2 != 0:
        median2 = list2[median2 - 1]
    else:
        pass


    # Taking the power_strength from the remaining players, sorting it and finding the median. (For "removed")

    list = []
    for i in database:
        if (math.isnan(i['power_strength'])) != True:
            list.append(i['power_strength'])
        else:
            pass

    list = sorted(list)
    # Finding the median
    median = (len(list)/2).__round__()
    if median != 0:
        median = list[median-1]
    else:
        pass

playerPowerStr()

# Performing the questions
# NOTE: If the user answers "probably" or "probably not" the calculations of the median will be performed in a duplicate of "database".
# This way it will not interfere with the final result.
playerPowerStrength = input('Is the players power_strength '+ str(median) + ' or over?')

if playerPowerStrength == 'y':
    for i in database:
        if i['power_strength'] < median:
            removed.append(i)
        else:
            playerPowerStrength = ''

    playerPowerStr()

    playerPowerStrength = input('Is the players power_strength '+ str(median) + ' or over?')

    if playerPowerStrength == 'y':
        for i in database:
            if i['power_strength'] < median:
                removed.append(i)
            else:
                playerPowerStrength = ''

    if playerPowerStrength == 'n':
        for i in database:
            if i['power_strength'] >= median:
                removed.append(i)
            else:
                playerPowerStrength = ''

    if playerPowerStrength == 'probably':
        for i in range(0, len(database)):
            for i in database:
                if i['power_strength'] < median:
                    probRemoved.append(i)
                else:
                    playerPowerStrength = ''

    if playerPowerStrength == 'probably not':
        for i in range(0, len(database)):
            for i in database:
                if i['power_strength'] >= median:
                    probRemoved.append(i)
                else:
                    playerPowerStrength = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerPowerStrength == 'n':
    for i in database:
        if i['power_strength'] >= median:
            removed.append(i)
        else:
            playerPowerStrength = ''
    playerPowerStr()
    playerPowerStrength = input('Is the players power_strength '+ str(median) + ' or over?')
    if playerPowerStrength == 'y':
        for i in database:
            if i['power_strength'] < median:
                removed.append(i)
            else:
                playerPowerStrength = ''

    if playerPowerStrength == 'n':
        for i in database:
            if i['power_strength'] >= median:
                removed.append(i)
            else:
                playerPowerStrength = ''

    if playerPowerStrength == 'probably':
        for i in range(0, len(database)):
            for i in database:
                if i['power_strength'] < median:
                    probRemoved.append(i)
                else:
                    playerPowerStrength = ''

    if playerPowerStrength == 'probably not':
        for i in range(0, len(database)):
            for i in database:
                if i['power_strength'] >= median:
                    probRemoved.append(i)
                else:
                    playerPowerStrength = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerPowerStrength == 'probably':
    for i in database:
        if i['power_strength'] < median:
            removed.append(i)
        else:
            playerPowerStrength = ''
    playerPowerStr()
    playerPowerStrength = input('Is the players power_strength '+ str(median2) + ' or over?')
    if playerPowerStrength == 'probably':
        for i in database:
            if i['power_strength'] < median2:
                removed.append(i)
            else:
                playerPowerStrength = ''

    if playerPowerStrength == 'probably not':
        for i in database:
            if i['power_strength'] >= median2:
                removed.append(i)
            else:
                playerPowerStrength = ''

    if playerPowerStrength == 'y':
        for i in database:
            if i['power_strength'] < median2:
                removed.append(i)
            else:
                playerPowerStrength = ''

    if playerPowerStrength == 'n':
        for i in database:
            if i['power_strength'] >= median2:
                removed.append(i)
            else:
                playerPowerStrength = ''



# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerPowerStrength == 'probably not':
    for i in database:
        if i['power_strength'] >= median:
            removed.append(i)
        else:
            playerPowerStrength = ''
    playerPowerStr()
    playerPowerStrength = input('Is the players power_strength '+ str(median2) + ' or over?')
    if playerPowerStrength == 'probably':
        for i in database:
            if i['power_strength'] < median2:
                removed.append(i)
            else:
                playerPowerStrength = ''

    if playerPowerStrength == 'probably not':
        for i in database:
            if i['power_strength'] >= median2:
                removed.append(i)
            else:
                playerPowerStrength = ''

    if playerPowerStrength == 'y':
        for i in database:
            if i['power_strength'] < median2:
                removed.append(i)
            else:
                playerPowerStrength = ''

    if playerPowerStrength == 'n':
        for i in database:
            if i['power_strength'] >= median2:
                removed.append(i)
            else:
                playerPowerStrength = ''

# Question 16 17
#international_reputation

def playerIntRep():

    global median
    global median2
    # Removing the "removed" elements from the "database"
    # Removing only from the "removed" and not from "probRemoved" too. Because if we remove from both of them it could lead to not finding the player
    #(The probRemoved are not certain and could misslead the rest of the algorithm)
    for i in removed:
        if i in database:
            database.remove(i)
        else:
            pass

    # Creating a duplicate database for "probRemoved" operations to be done inside it.
    global database2
    database2 = copy.deepcopy(database)

    # # Removing the "probRemoved" and "removed" elements from the "database2".
    for i in removed:
        if i in database2:
            database.remove(i)
        else:
            pass

    for i in probRemoved:
        if i in database2:
            database2.remove(i)
        else:
            pass

    # Taking the international_reputation from the remaining players, sorting it and finding the median. (For "probRemoved")
    list2 = []
    for i in database:
        if (math.isnan(i['international_reputation'])) != True:
            list2.append(i['international_reputation'])
        else:
            pass
    list2 = sorted(list2)

    # Finding the "median2"
    median2 = (len(list2)/2).__round__()
    if median2 != 0:
        median2 = list2[median2 - 1]
    else:
        pass


    # Taking the international_reputation from the remaining players, sorting it and finding the median. (For "removed")

    list = []
    for i in database:
        if (math.isnan(i['international_reputation'])) != True:
            list.append(i['international_reputation'])
        else:
            pass

    list = sorted(list)
    # Finding the median
    median = (len(list)/2).__round__()
    if median != 0:
        median = list[median-1]
    else:
        pass

playerIntRep()

# Performing the questions
# NOTE: If the user answers "probably" or "probably not" the calculations of the median will be performed in a duplicate of "database".
# This way it will not interfere with the final result.
playerInterRep = input('Is the players international_reputation '+ str(median) + ' or over?')

if playerInterRep == 'y':
    for i in database:
        if i['international_reputation'] < median:
            removed.append(i)
        else:
            playerInterRep = ''

    playerIntRep()

    playerInterRep = input('Is the players international_reputation '+ str(median) + ' or over?')

    if playerInterRep == 'y':
        for i in database:
            if i['international_reputation'] < median:
                removed.append(i)
            else:
                playerInterRep = ''

    if playerInterRep == 'n':
        for i in database:
            if i['international_reputation'] >= median:
                removed.append(i)
            else:
                playerInterRep = ''

    if playerInterRep == 'probably':
        for i in range(0, len(database)):
            for i in database:
                if i['international_reputation'] < median:
                    probRemoved.append(i)
                else:
                    playerInterRep = ''

    if playerInterRep == 'probably not':
        for i in range(0, len(database)):
            for i in database:
                if i['international_reputation'] >= median:
                    probRemoved.append(i)
                else:
                    playerInterRep = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerInterRep == 'n':
    for i in database:
        if i['international_reputation'] >= median:
            removed.append(i)
        else:
            playerInterRep = ''
    playerIntRep()
    playerInterRep = input('Is the players international_reputation '+ str(median) + ' or over?')
    if playerInterRep == 'y':
        for i in database:
            if i['international_reputation'] < median:
                removed.append(i)
            else:
                playerInterRep = ''

    if playerInterRep == 'n':
        for i in database:
            if i['international_reputation'] >= median:
                removed.append(i)
            else:
                playerInterRep = ''

    if playerInterRep == 'probably':
        for i in range(0, len(database)):
            for i in database:
                if i['international_reputation'] < median:
                    probRemoved.append(i)
                else:
                    playerInterRep = ''

    if playerInterRep == 'probably not':
        for i in range(0, len(database)):
            for i in database:
                if i['international_reputation'] >= median:
                    probRemoved.append(i)
                else:
                    playerInterRep = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerInterRep == 'probably':
    for i in database:
        if i['international_reputation'] < median:
            removed.append(i)
        else:
            playerInterRep = ''
    playerIntRep()
    playerInterRep = input('Is the players international_reputation '+ str(median2) + ' or over?')
    if playerInterRep == 'probably':
        for i in database:
            if i['international_reputation'] < median2:
                removed.append(i)
            else:
                playerInterRep = ''

    if playerInterRep == 'probably not':
        for i in database:
            if i['international_reputation'] >= median2:
                removed.append(i)
            else:
                playerInterRep = ''

    if playerInterRep == 'y':
        for i in database:
            if i['international_reputation'] < median2:
                removed.append(i)
            else:
                playerInterRep = ''

    if playerInterRep == 'n':
        for i in database:
            if i['international_reputation'] >= median2:
                removed.append(i)
            else:
                playerInterRep = ''



# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerInterRep == 'probably not':
    for i in database:
        if i['international_reputation'] >= median:
            removed.append(i)
        else:
            playerInterRep = ''
    playerIntRep()
    playerInterRep = input('Is the players international_reputation '+ str(median2) + ' or over?')
    if playerInterRep == 'probably':
        for i in database:
            if i['international_reputation'] < median2:
                removed.append(i)
            else:
                playerInterRep = ''

    if playerInterRep == 'probably not':
        for i in database:
            if i['international_reputation'] >= median2:
                removed.append(i)
            else:
                playerInterRep = ''

    if playerInterRep == 'y':
        for i in database:
            if i['international_reputation'] < median2:
                removed.append(i)
            else:
                playerInterRep = ''

    if playerInterRep == 'n':
        for i in database:
            if i['international_reputation'] >= median2:
                removed.append(i)
            else:
                playerInterRep = ''


# Question 18 19
# weak_foot
def playerWkFoot():

    global median
    global median2
    # Removing the "removed" elements from the "database"
    # Removing only from the "removed" and not from "probRemoved" too. Because if we remove from both of them it could lead to not finding the player
    #(The probRemoved are not certain and could misslead the rest of the algorithm)
    for i in removed:
        if i in database:
            database.remove(i)
        else:
            pass

    # Creating a duplicate database for "probRemoved" operations to be done inside it.
    global database2
    database2 = copy.deepcopy(database)

    # # Removing the "probRemoved" and "removed" elements from the "database2".
    for i in removed:
        if i in database2:
            database.remove(i)
        else:
            pass

    for i in probRemoved:
        if i in database2:
            database2.remove(i)
        else:
            pass

    # Taking the weak_foot from the remaining players, sorting it and finding the median. (For "probRemoved")
    list2 = []
    for i in database:
        if (math.isnan(i['weak_foot'])) != True:
            list2.append(i['weak_foot'])
        else:
            pass
    list2 = sorted(list2)

    # Finding the "median2"
    median2 = (len(list2)/2).__round__()
    if median2 != 0:
        median2 = list2[median2 - 1]
    else:
        pass


    # Taking the weak_foot from the remaining players, sorting it and finding the median. (For "removed")

    list = []
    for i in database:
        if (math.isnan(i['weak_foot'])) != True:
            list.append(i['weak_foot'])
        else:
            pass

    list = sorted(list)
    # Finding the median
    median = (len(list)/2).__round__()
    if median != 0:
        median = list[median-1]
    else:
        pass

playerWkFoot()

# Performing the questions
# NOTE: If the user answers "probably" or "probably not" the calculations of the median will be performed in a duplicate of "database".
# This way it will not interfere with the final result.
playerWeakFoot = input('Is the players weak_foot '+ str(median) + ' or over?')

if playerWeakFoot == 'y':
    for i in database:
        if i['weak_foot'] < median:
            removed.append(i)
        else:
            playerWeakFoot = ''

    playerWkFoot()

    playerWeakFoot = input('Is the players weak_foot '+ str(median) + ' or over?')

    if playerWeakFoot == 'y':
        for i in database:
            if i['weak_foot'] < median:
                removed.append(i)
            else:
                playerWeakFoot = ''

    if playerWeakFoot == 'n':
        for i in database:
            if i['weak_foot'] >= median:
                removed.append(i)
            else:
                playerWeakFoot = ''

    if playerWeakFoot == 'probably':
        for i in range(0, len(database)):
            for i in database:
                if i['weak_foot'] < median:
                    probRemoved.append(i)
                else:
                    playerWeakFoot = ''

    if playerWeakFoot == 'probably not':
        for i in range(0, len(database)):
            for i in database:
                if i['weak_foot'] >= median:
                    probRemoved.append(i)
                else:
                    playerWeakFoot = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerWeakFoot == 'n':
    for i in database:
        if i['weak_foot'] >= median:
            removed.append(i)
        else:
            playerWeakFoot = ''
    playerWkFoot()
    playerWeakFoot = input('Is the players weak_foot '+ str(median) + ' or over?')
    if playerWeakFoot == 'y':
        for i in database:
            if i['weak_foot'] < median:
                removed.append(i)
            else:
                playerWeakFoot = ''

    if playerWeakFoot == 'n':
        for i in database:
            if i['weak_foot'] >= median:
                removed.append(i)
            else:
                playerWeakFoot = ''

    if playerWeakFoot == 'probably':
        for i in range(0, len(database)):
            for i in database:
                if i['weak_foot'] < median:
                    probRemoved.append(i)
                else:
                    playerWeakFoot = ''

    if playerWeakFoot == 'probably not':
        for i in range(0, len(database)):
            for i in database:
                if i['weak_foot'] >= median:
                    probRemoved.append(i)
                else:
                    playerWeakFoot = ''

# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerWeakFoot == 'probably':
    for i in database:
        if i['weak_foot'] < median:
            removed.append(i)
        else:
            playerWeakFoot = ''
    playerWkFoot()
    playerWeakFoot = input('Is the players weak_foot '+ str(median2) + ' or over?')
    if playerWeakFoot == 'probably':
        for i in database:
            if i['weak_foot'] < median2:
                removed.append(i)
            else:
                playerWeakFoot = ''

    if playerWeakFoot == 'probably not':
        for i in database:
            if i['weak_foot'] >= median2:
                removed.append(i)
            else:
                playerWeakFoot = ''

    if playerWeakFoot == 'y':
        for i in database:
            if i['weak_foot'] < median2:
                removed.append(i)
            else:
                playerWeakFoot = ''

    if playerWeakFoot == 'n':
        for i in database:
            if i['weak_foot'] >= median2:
                removed.append(i)
            else:
                playerWeakFoot = ''



# = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # = # =

if playerWeakFoot == 'probably not':
    for i in database:
        if i['weak_foot'] >= median:
            removed.append(i)
        else:
            playerWeakFoot = ''
    playerWkFoot()
    playerWeakFoot = input('Is the players weak_foot '+ str(median2) + ' or over?')
    if playerWeakFoot == 'probably':
        for i in database:
            if i['weak_foot'] < median2:
                removed.append(i)
            else:
                playerWeakFoot = ''

    if playerWeakFoot == 'probably not':
        for i in database:
            if i['weak_foot'] >= median2:
                removed.append(i)
            else:
                playerWeakFoot = ''

    if playerWeakFoot == 'y':
        for i in database:
            if i['weak_foot'] < median2:
                removed.append(i)
            else:
                playerWeakFoot = ''

    if playerWeakFoot == 'n':
        for i in database:
            if i['weak_foot'] >= median2:
                removed.append(i)
            else:
                playerWeakFoot = ''


# Question 20
# Club

def findClub():

    global median
    global median2
    # Removing the "removed" elements from the "database"
    # Removing only from the "removed" and not from "probRemoved" too. Because if we remove from both of them it could lead to not finding the player
    #(The probRemoved are not certain and could misslead the rest of the algorithm)
    for i in removed:
        if i in database:
            database.remove(i)
        else:
            pass

    # Creating a duplicate database for "probRemoved" operations to be done inside it.
    global database2
    database2 = copy.deepcopy(database)

    # # Removing the "probRemoved" and "removed" elements from the "database2".
    for i in removed:
        if i in database2:
            database.remove(i)
        else:
            pass

    for i in probRemoved:
        if i in database2:
            database2.remove(i)
        else:
            pass

    # Taking the age from the remaining players, sorting it and finding the median. (For "probRemoved")
    list2 = []
    for i in database2:
        list2.append(i['club'])

    # Finding the "median2"
    median2 = (len(list2)/2).__round__()
    if median2 != 0:
        median2 = list2[median2 - 1]
    else:
        pass


    # Taking the age from the remaining players, sorting it and finding the median. (For "removed")

    list = []
    for i in database:
        list.append(i['club'])
    list = sorted(list)

    # Finding the median
    median = (len(list)/2).__round__()
    if median != 0:
        median = list[median-1]
    else:
        pass

findClub()

# Performing the questions
# NOTE: If the user answers "probably" or "probably not" the calculations of the median will be performed in a duplicate of "database".
# This way it will not interfere with the final result.
playerClub = input("Is the player playing for " + str(median))
if playerClub == 'y':
    for i in database:
        if i['club'] != median:
            removed.append(i)
        else:
            playerAge = ''
# If the preferred foot is left add all right-footed players in the "removed" list
if playerClub == 'n':
    for i in database:
        if i['club'] == median:
            removed.append(i)
        else:
            playerAge = ''

# If the preferred foot is right add all left-footed players in the "probRemoved" list
if playerClub == 'probably':
    for i in database:
        if i['club'] != median:
            probRemoved.append(i)
        else:
            playerAge = ''

# If the preferred foot is left add all right-footed players in the "probRemoved" list
if playerClub == 'probably not':
    for i in range(0, len(database)):
        if df.at[i, "club"] == median2:
            probRemovedAppend()







checker()

if len(database) != 1:
    for i in probRemoved:
        if i in database:
            database.remove(i)
        else:
            pass
    if len(database) == 1:
        print("found him!")
        print(database)
    if len(database) == 0:
        print('I failed :(')
    # If the player is not found the most famous is chosen (The one with the most "international_reputation")
    else:
        list = []
        for i in database:
            list.append(i['international_reputation'])
        print(max(list))

        for i in database:
            if i['international_reputation'] == max(list):
                print('This is my most probable guess' + str(i))
                exit()
#         print("I failed :(")
# print(len(database))










# NOTES:

# #Question 21
# # Club
#
# findClub()
#
# # Performing the questions
# # NOTE: If the user answers "probably" or "probably not" the calculations of the median will be performed in a duplicate of "database".
# # This way it will not interfere with the final result.
# playerClub = input("Is the player playing for " + str(median))
# if playerClub == 'y':
#     for i in database:
#         if i['club'] != median:
#             removed.append(i)
#         else:
#             playerAge = ''
# # If the preferred foot is left add all right-footed players in the "removed" list
# if playerClub == 'n':
#     for i in database:
#         if i['club'] == median:
#             removed.append(i)
#         else:
#             playerAge = ''
#
# # If the preferred foot is right add all left-footed players in the "probRemoved" list
# if playerClub == 'probably':
#     for i in database:
#         if i['club'] != median:
#             probRemoved.append(i)
#         else:
#             playerAge = ''
#
# # If the preferred foot is left add all right-footed players in the "probRemoved" list
# if playerClub == 'probably not':
#     for i in range(0, len(database)):
#         if df.at[i, "club"] == median2:
#             probRemovedAppend()




# # Reading the lenght of the database (Used in the end to check if the database has only one element inside (ie. has found the player))
# print("this is the remaining player")
# print(len(database))
# print (database)

# print("This is the 'removed' database")
# print(removed)
#
# print()
#
# print("this is the 'probably' database")
# print(probRemoved)


# for i in probRemoved:
#     database.remove(i)
# print("this is the remaining player (prob)")
# print(len(database))
# print (database)










# # Printing the excluded players
# for i in range(len(probRemoved)):
#     #    print (i)
#     print(probRemoved[i]['short_name'])

#print(removed)


# Removing the unwanted players from the dataframe (removing all the players "removed" and "probRemoved" are holding from "df")
#for i in removed:
#    print(i['age'])


# for i in removed:
#     new = [
#         {'sofifa_id': i['sofifa_id'], 'player_url': i['player_url'], 'short_name': i['short_name'],
#          'age': i['age'], 'height_cm': i['height_cm'], 'preferred_foot': i['preferred_foot']}
#     ]
#     # Appends the 'new' dataframe to the 'database'
#     database.remove(new)


# dataBaseTest = [
#     {'mame':'Thanasis', 'age':20}
# ]
#
# new1 = [
#     {'mame':'Silia', 'age':20}
# ]
#
#
# dataBaseTest.append(new)
# print(dataBaseTest)


# Get a specific element from a row
# a = df.at[0, "age"]
# print(a)

# Get a whole row
# print(df.loc[0])

# Remove duplicates
# mylist = ["a", "b", "b", "c", "a"]
# mylist = sorted(set(mylist))
# print(mylist)


# Printing the excluded players
# for i in range(len(removed)):
#     #    print (i)
#     print(removed[i]['short_name'])




# Removing the "probRemoved" elements from the "database"
# for i in probRemoved:
#     database.remove(i)
#     print("Done")


# # By removing the brackets "[]" i can access the elements inside.
# new = {'sofifa_id': df.at[1, "sofifa_id"], 'player_url': df.at[1, "player_url"], 'short_name': df.at[1, "short_name"],
#      'age': df.at[1, "age"], 'height_cm': df.at[1, "height_cm"], 'preferred_foot': df.at[1, "preferred_foot"],
#      "value_eur": df.at[1, "value_eur"], 'real_face': df.at[1, "real_face"]}
#
# # This is how to access the elements
# print(new['short_name'])



