When downloaded the file directory of the .csv file should be updated accordingly to your system.
Have Fun!





Akinator
Introduction:
This is an Akinator (AI algorithm). The aim of the algorithm is to find/predict a football player that the user is thinking. The way this is achieved is by asking the user questions (max20), the user can answer with ‘y’ (yes), ‘n’ (no), ‘probably’, ‘probably not, ‘don’t know’. After the questions are answered the algorithm prints the player (certain) or prints the closest player that it found (not certain) or prints a failure message (did not manage to find the player). The database is from fifa.

Code
This section briefly analyses how the code behind the algorithm works.
First of all, the programming language used is Python3.11(.py). The first thing that is done is the import of all the necessary libraries (numpy, pandas, csv, copy, statistics, and math). Next, the database (Footballers.csv) is imported inside the program and passed into a list, each element inside the list contains all the necessary information for all the questions to be performed.
After welcoming the user, lists and functions are created. Moving downwards the questions (with the operations) are met. Generally there are two (2) types of questions static and non-static. More in depth, static questions are not changing/adapting to the players left inside the database (No need to). On the contrary, non-static questions form based on the players that are left inside the database. Lastly, when all the questions are answered the algorithm performs the prediction.
How the player is located
After each question the players that don’t fit the description are added inside another list (“removed”). When all the questions are done the algorithm subtracts all the “removed” elements from the original database hoping that the wanted player is the only player left inside the database.
Except the “removed” list that contains only the yes or no answers there is another list that contains all the “probably” and “probably not” answers name “probRemoved”. This list will also be subtracted from the database in case the player is not found just from the “removed” list. The reason this happens is because the data inside “probRemoved” are not certain and could negatively affect the algorithm, but if “removed” is not enough there is no other option than also subtracting the “probRemoved” list.
Non-static questions
Some more information regarding the non-static questions:
The algorithm updates the database (mid-algorithm | removes the unwanted players until now) and then it finds the median of the players left and performs the questions based on that. It’s a simple yet effective approach. It also takes into consideration the “probRemoved” list, in order to do that without removing the “probRemoved” elements from the database mid-program a database duplicate is created and calculations are performed inside it, this way the original database is not affected but the efficiency of the algorithm is increased.
General Notes 
There are a lot of comments explaining what is happening more specifically and also some ‘lines’ (long comments) that are increasing the readability of the algorithm. On top of that, readability is also increased by defining some functions mid-program instead of creating them all at the top.









Copyrights: Athanasios Ioannidis e-mail: thanasisfirst@gmail.com
