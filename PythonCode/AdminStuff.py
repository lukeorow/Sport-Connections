from PythonCode.DB import *

class AdminStuff:

    # this is for adding new daily game to the database (scheduled by the date)
    def add_new_daily_game():
        date = "2024-03-26" # date that the game will be stored under

        
        c1_name = "2018-2019 Brooklyn Nets"
        c1i1 = "Caris LeVert"
        c1i2 = "D'Angelo Russell"
        c1i3 = "Jarrett Allen"
        c1i4 = "Spencer Dinwiddie"

        c2_name = "2017 Draft Top 4 Picks"
        c2i1 = "Markelle Fultz"
        c2i2 = "Lonzo Ball"
        c2i3 = "Jayson Tatum"
        c2i4 = "Josh Jackson"

        c3_name = "Total Steals Leaders"
        c3i1 = "Shai Gilgeous-Alexander"
        c3i2 = "De'Aaron Fox"
        c3i3 = "Matisse Thybulle"
        c3i4 = "Kawhi Leonard"

        c4_name = "Players with the most points in any NBA game"
        c4i1 = "Wilt Chamberlain"
        c4i2 = "Kobe Bryant"
        c4i3 = "Luka Doncic"
        c4i4 = "David Thompson"

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

