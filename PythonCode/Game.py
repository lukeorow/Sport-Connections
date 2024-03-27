import json
import sqlite3
import datetime

class Item: 
    def __init__(self, title):
        self.title = title
        self.category = None # initalized to none until put in a category
        
class Category:
    def __init__(self, name):
        self.name = name
        self.items = [] # this is where the 4 items in the catgeory get put

    def add_items(self, item1, item2, item3, item4):
        if len(self.items) == 0:
            item1.category = self
            item2.category = self
            item3.category = self
            item4.category = self
            self.items = [item1, item2, item3, item4]
        else:
            print("Category already full")

    def to_dict(self):
        return {
            'name': self.name,
            'items': [item.title for item in self.items]
        }

# takes takes a category name and 4 item names and makes into a category with 4 items
    def make_category(category_name, item1_name, item2_name, item3_name, item4_name):
        category = Category(category_name)
        item1 = Item(item1_name)
        item2 = Item(item2_name)
        item3 = Item(item3_name)
        item4 = Item(item4_name)

        category.add_items(item1, item2, item3, item4)

        return category, item1, item2, item3, item4



