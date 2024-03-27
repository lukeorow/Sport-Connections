import datetime

class GameScheduler:

    def get_current_date():
        return datetime.datetime.now().date()

g = GameScheduler()
print(g.get_current_date)