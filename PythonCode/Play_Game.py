from Game import make_category

class Play_Game:
    
    def __init__(self):
        self.attempts_remaining = 4 # how many lives they have, they lose one after each incorrect guess
        self.cats_remaining = 4 # the number of correct categories left to guess

    # sets up the game board, adding items to it
    def start_game(cat1, cat2, cat3, cat4):
        a, a1, a2, a3, a4 = make_category("Wide Receivers", "Calvin Johnson", "Jerry Rice", "Julio Jones", "Stefon Diggs")
        b, b1, b2, b3, b4 = make_category("Running Backs", "James Cook", "Keaton Mitchell", "Devin Singletary", "Zach Charbonnet")
        c, c1, c2, c3, c4 = make_category("Quarterbacks", "Jared Goff", "Josh Rosen", "Colt McCoy", "Tyrod Taylor")
        d, d1, d2, d3, d4 = make_category("Defensive Ends under 25", "Aidan Hutchinson", "Micah Parsons", "Travon Walker", "George Karlaftis")

    
    # lets user select the 4 they want to input (will end up making this its own separate game mode)

    # function that checks if the input is correct, and lets them know if they are one off
    def check_input(self, *items):
        categories = [item.category for item in items]
        num_categories = len(set(categories))

        # if all 4 guessed are in the same category
        if num_categories == 1: 
            print("all are in the same")
            self.cats_remaining -= 1
            Play_Game.correct_category() 
        # if they are one away from the correect category
        elif num_categories == 2:
            category_count = {category: categories.count(category) for category in set(categories)}
            if 3 in category_count.values():
                print("Incorrect but you are one away!")
                self.attempts_remaining -= 1
                return
            print("testing: 2 categories with 2 items in each")
        # if they are neither of above and completely wrong
        else:
            print("incorrect")
            self.attempts_remaining -= 1
            
    

    # function that handles when the user gets a category correct
    def correct_category():
       None 

