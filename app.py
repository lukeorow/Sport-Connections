from flask import Flask, render_template
from PythonCode.Game import *
from PythonCode.DB import *
from PythonCode.AdminStuff import *
import datetime
import random
import json

app = Flask(__name__, static_url_path='/static')
#app.debug = False

todays_date = "2024-04-07"#datetime.datetime.now().date()

@app.route('/')
def index():
    #game_data = DB.get_game("daily_games.db", "2024-03-29")

    # this is for adding new games. only uncomment when adding new game
    #AdminStuff.add_new_daily_game()

    return render_template('index.html')

@app.route('/football')
def football():
    game_data = DB.get_game("data/football_games.db", todays_date)
    all_items = [(item.title, category.name) for category in game_data for item in category.items]
    random.shuffle(all_items)

    return render_template('football.html', all_items=all_items)

@app.route('/basketball')
def basketball():
    game_data = DB.get_game("data/basketball_games.db", todays_date)
    all_items = [(item.title, category.name) for category in game_data for item in category.items]
    random.shuffle(all_items)

    return render_template('basketball.html', all_items=all_items)

@app.route('/hockey')
def hockey():
    game_data = DB.get_game("data/hockey_games.db", todays_date)
    all_items = [(item.title, category.name) for category in game_data for item in category.items]
    random.shuffle(all_items)

    return render_template('hockey.html', all_items=all_items)

@app.route('/baseball')
def baseball():
    game_data = DB.get_game("data/baseball_games.db", todays_date)
    all_items = [(item.title, category.name) for category in game_data for item in category.items]
    random.shuffle(all_items)

    return render_template('baseball.html', all_items=all_items)

    

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

