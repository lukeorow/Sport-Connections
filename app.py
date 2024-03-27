from flask import Flask, render_template
from PythonCode.Game import *
from PythonCode.DB import *
from PythonCode.AdminStuff import *
import datetime
import random
import json

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    todays_date = datetime.datetime.now().date()

    game_data= DB.get_game(todays_date)
    #game_data = DB.get_game("2024-03-21")
    #game_data = DB.get_game("2024-03-21")


    # this is for adding new games. only uncomment when adding new game
    #AdminStuff.add_new_daily_game()

    all_items = [(item.title, category.name) for category in game_data for item in category.items]
    random.shuffle(all_items)

    return render_template('index.html', all_items=all_items)

@app.route('/get_selected_game')
def get_selected_game(date):
    game_data = DB.get_game(date)
    return game_data


@app.route('/get_previous_dates')
def previous_game_dates():
    dates = DB.get_all_dates() 
    return dates


if __name__ == '__main__':
    app.run(debug=True)

