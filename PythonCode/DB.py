import sqlite3
from PythonCode.Game import *
import json
from flask import jsonify


# database functions for storing the
class DB:

    @staticmethod
    # this will create a new db if one doesn't already exists, needs to happen right when game starts
    def startup_db(db_name):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # table stores the category with its name and the 4 items as strings
        # will need a way to take the item objects and put them in the database, then be able to retrieve them 
        # and put them back into objects with their correct attributes
        create_table = """
        CREATE TABLE IF NOT EXISTS daily_games (
            game_number INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE,
            category1 TEXT,
            category2 TEXT,
            category3 TEXT,
            category4 TEXT
        )
        """
        cursor.execute(create_table)

        conn.commit()
        cursor.close()
        conn.close()

    def insert_game(db_name, date, cat1, cat2, cat3, cat4):
        DB.startup_db(db_name)
        # needs to insert a full game into the database
        # a full game includes 4 categories that each contain 4 items that belong to them. 
        # they need to be associated with the date primary key

        conn = sqlite3.connect(db_name) # adds to the specific DB
        cursor = conn.cursor()

        cursor.execute("INSERT INTO daily_games (date, category1, category2, category3, category4) VALUES (?, ?, ?, ?, ?)", (date, cat1, cat2, cat3, cat4))

        conn.commit()
        cursor.close()
        conn.close()

    def format_game_data(row):
        categories_data = row[2:]
        game = []
        game_number = row[0]
        print("Game number " + str(game_number))
        for category_data in categories_data:
            if category_data:
                category_items = category_data.split("!!")
                item1 = Item(category_items[1])
                item2 = Item(category_items[2])
                item3 = Item(category_items[3])
                item4 = Item(category_items[4])
                category = Category(category_items[0])
                category.add_items(item1, item2, item3, item4)
                category.name = category_items[0]
                game.append(category)
        return game

 
    # this gets the game data from the selected sport based on the inputted date
    def get_game(db_name, date):
        # i need to be able to pull a game (which includes 4 categories where each contains 4 items), by using the date
        # to grab the specific one. i need to be able to pull the category and items with their attributes
        
        conn = sqlite3.connect(db_name) # now it pulls from whichever sport's db is in parameter
        cursor = conn.cursor()
    
        cursor.execute("SELECT * FROM daily_games WHERE date=?", (date,))
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row:
            categories_data = row[2:]
            game = []
            game_number = row[0] # could be used to show what # game it is
            for category_data in categories_data:
                if category_data:
                    category_items = category_data.split("!!")
                    item1 = Item(category_items[1])
                    item2 = Item(category_items[2])
                    item3 = Item(category_items[3])
                    item4 = Item(category_items[4])
                    category = Category(category_items[0])
                    category.add_items(item1, item2, item3, item4)
                    category.name = category_items[0]
                    game.append(category)
            return game
        else:
            return "Nothing found"
    
    # collects all of the dates available in the db (for previous games button)
    def get_all_dates(db_name):
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT date FROM daily_games")
        dates = cursor.fetchall()
        dates_list = [date[0] for date in dates]
        connection.close()

        return jsonify(dates_list)


