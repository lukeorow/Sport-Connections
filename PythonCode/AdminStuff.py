from PythonCode.DB import *

class AdminStuff:

    # this is for adding new daily game to the database (scheduled by the date)
    def add_new_daily_game():
        date = "2024-04-07" # date that the game will be stored under

        # uncomment the one that the new game is getting added to
        #db_name = "football_games.db"
        #db_name = "basketball_games.db"
        db_name = "hockey_games.db"
        #db_name = "baseball_games.db"

        # Very Hard category
        c1_name = "All Time Points Leaders"
        c1i1 = "Wayne Gretzky"
        c1i2 = "Jaromir Jagr"
        c1i3 = "Mark Messier"
        c1i4 = "Gordie Howe"

        # Hard category
        c2_name = "Current Assist Leaders"
        c2i1 = "Connor McDavid"
        c2i2 = "Nikita Kucherov"
        c2i3 = "Nathan MacKinnon"
        c2i4 = "Quinn Hughes"

        # Medium category
        c3_name = "Previous 4 Conn Smythe Trophy Winners"
        c3i1 = "Jonathan Marchessault"
        c3i2 = "Cale Makar"
        c3i3 = "Andrei Vasilevskiy"
        c3i4 = "Victor Hedman"

        # Easy category 
        c4_name = "Current Detroit Red Wings Defensemen"
        c4i1 = "Moritz Seider"
        c4i2 = "Jeff Petry"
        c4i3 = "Ben Chiarot"
        c4i4 = "Shayne Gostisbehere"

        cat1 = c1_name+"!!"+c1i1+"!!"+c1i2+"!!"+c1i3+"!!"+c1i4
        cat2 = c2_name+"!!"+c2i1+"!!"+c2i2+"!!"+c2i3+"!!"+c2i4
        cat3 = c3_name+"!!"+c3i1+"!!"+c3i2+"!!"+c3i3+"!!"+c3i4
        cat4 = c4_name+"!!"+c4i1+"!!"+c4i2+"!!"+c4i3+"!!"+c4i4

        DB.insert_game(db_name, date, cat1, cat2, cat3, cat4)


        

    # need to decide on a way to choose which categories actually get used while playing the game
    # can either 
    #   1. add a bunch of categories and have the system randomly choose 4 of them to play the game
    #       - this would be best for replayability but would have to add a ton of categories for it to not get old
    #   2. manually have 4 each day that could be scheduled somehow to be used on each day
    #       - put date for the category group in the database entry
    #   3. have both a daily game and another infinitely replayable game that chooses random ones
    #       - basically this combines both 1 and 2 and lets the system do both

