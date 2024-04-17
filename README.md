# Sport Connections
Live Deployed at: https://nfl-connectionss.onrender.com/

Daily sports trivia game with a new game each day!
Current Sports: NFL, NBA, NHL, MLB

Game Objective: 
- Find groups of 4 sports players that all share a common category (same team, play the same position, went to the same college, etc.) 
- Each game is comprised of the names of 16 sports players, with 4 players in each of the 4 categories that the player must find.
- Find all 4 categories before making 4 mistakes to win!

How to Play:
- Select 4 players that you believe all belong to the same category and submit the answer.
- If your guess is correct, then the category name will be revealed to you, and the game continues with the remaining items.
- If your guess is incorrect, then you lose a life. The game ends when 4 mistakes are made.

Features:
- SQLite databases that stores the games for each sport using the date as the primary key
- HTML/CSS/JavaScript interface with animations on some items using CSS
- Python for formatting and storing games to the database
- Flask web framework
- Deployed on Render

Future Implementations:
- Better experience on mobile (currently only works well on computers and iPads)
- "Previous Games" button to allow the user to select a past date and play that day's game
- "How to Play" button that pops up a modal with info on how to play
- Handling when the game is won (modal, animation, etc.)
- Handling when the game is lost (modal, show correct cateogories, etc.)
- Add a function to copy and paste the player's results and share with friends
- Change the database to simplify adding to it

  
