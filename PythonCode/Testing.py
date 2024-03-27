from Play_Game import *
from DB import *
from GameScheduler import *
from AdminStuff import *

# works
#a, a1, a2, a3, a4 = make_category("Wide Receivers", "Calvin Johnson", "Jerry Rice", "Julio Jones", "Stefon Diggs")
#b, b1, b2, b3, b4 = make_category("Running Backs", "James Cook", "Keaton Mitchell", "Devin Singletary", "Zach Charbonnet")
#c, c1, c2, c3, c4 = make_category("Quarterbacks", "Jared Goff", "Josh Rosen", "Colt McCoy", "Tyrod Taylor")
#d, d1, d2, d3, d4 = make_category("Defensive Ends under 25", "Aidan Hutchinson", "Micah Parsons", "Travon Walker", "George Karlaftis")

# all work
#game = Play_Game()
##game.check_input(a1, a2, a3, a4)
#game.check_input(c1, c4, c2, d4)
#game.check_input(a1, c3, d2, b4)

#DB.startup_db()
#date = GameScheduler.get_current_date()


# First, let's create some categories and items
#category1, item1_1, item1_2, item1_3, item1_4 = make_category("Category 1", "Item 1-1", "Item 1-2", "Item 1-3", "Item 1-4")
#category2, item2_1, item2_2, item2_3, item2_4 = make_category("Category 2", "Item 2-1", "Item 2-2", "Item 2-3", "Item 2-4")
#category3, item3_1, item3_2, item3_3, item3_4 = make_category("Category 3", "Item 3-1", "Item 3-2", "Item 3-3", "Item 3-4")
#category4, item4_1, item4_2, item4_3, item4_4 = make_category("Category 4", "Item 4-1", "Item 4-2", "Item 4-3", "Item 4-4")

# Now, let's create a list of categories to represent a game
#game_categories = [category1, category2, category3, category4]

#AdminStuff.add_new_daily_game()
cats = DB.get_game("2024-03-16")

print(cats[3].items[1].title)