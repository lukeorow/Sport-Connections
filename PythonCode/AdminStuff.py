from PythonCode.DB import *

class AdminStuff:

    # this is for adding new daily game to the database (scheduled by the date)
    def add_new_daily_game():
        date = "2024-03-29" # date that the game will be stored under

        # Very Hard category
        c1_name = "Lowest FG% this Season"
        c1i1 = "Jordan Hawkins"
        c1i2 = "Scoot Henderson"
        c1i3 = "Alec Burks"
        c1i4 = "Royce O'Neal"

        # Hard category
        c2_name = "Former Suns Still in the League"
        c2i1 = "Chris Paul"
        c2i2 = "Jock Landale"
        c2i3 = "Kelly Oubre"
        c2i4 = "Richaun Holmes"

        # Medium category
        c3_name = "Players Traded by the Pistons"
        c3i1 = "Marvin Bagley"
        c3i2 = "Andre Drummond"
        c3i3 = "Tobias Harris"
        c3i4 = "Saddiq Bey"

        # Easy category 
        c4_name = "Last 4 #2 Overall Picks"
        c4i1 = "Chet Holmgren"
        c4i2 = "Jalen Green"
        c4i3 = "Brandon Miller"
        c4i4 = "James Wiseman"

        cat1 = c1_name+"!!"+c1i1+"!!"+c1i2+"!!"+c1i3+"!!"+c1i4
        cat2 = c2_name+"!!"+c2i1+"!!"+c2i2+"!!"+c2i3+"!!"+c2i4
        cat3 = c3_name+"!!"+c3i1+"!!"+c3i2+"!!"+c3i3+"!!"+c3i4
        cat4 = c4_name+"!!"+c4i1+"!!"+c4i2+"!!"+c4i3+"!!"+c4i4

        DB.insert_game(date, cat1, cat2, cat3, cat4)


        

    # need to decide on a way to choose which categories actually get used while playing the game
    # can either 
    #   1. add a bunch of categories and have the system randomly choose 4 of them to play the game
    #       - this would be best for replayability but would have to add a ton of categories for it to not get old
    #   2. manually have 4 each day that could be scheduled somehow to be used on each day
    #       - put date for the category group in the database entry
    #   3. have both a daily game and another infinitely replayable game that chooses random ones
    #       - basically this combines both 1 and 2 and lets the system do both

