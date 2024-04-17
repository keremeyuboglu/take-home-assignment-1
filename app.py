from flask import Flask, jsonify
from db_util import check_if_non_seeded_db, seed_db
import json
from util import get_seed_data, convert_keys_to_pascal_case
from db import db



database_credentials = {
    'dbname': 'Unplug',
    'user': 'postgres',
    'password': '123',
    'host': 'localhost',
    'port': '5432'
}

app = Flask(__name__)
connection_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(**database_credentials)
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string

db.init_app(app)

if check_if_non_seeded_db():
    seed_data = get_seed_data()
    seed_data = convert_keys_to_pascal_case(seed_data)
    seed_db(seed_data)


@app.get('/')
def hello():
    file_name = 'sample_data.json'
    menu_item = None

    # with open(file_name, 'r') as file:
    #     # Load the JSON data from the file
    #     data = json.load(file)
    #     menu_items = data["menu_item_map"]
    #     item_data = menu_items["148142"]
        
    # menu_item = MenuItem(
    #     id=item_data["id"],
    #     name=item_data["name"],
    #     description=item_data["description"],
    #     stock_status=item_data["stock_status"],
    #     restaurant_id=item_data["restaurant_id"],
    #     image=item_data["image"],
    #     ranking=item_data["ranking"],
    #     price=item_data["price"],
    #     calories=item_data["calorie"]
    # )
    # db.session.add(menu_item)
    # db.session.commit()
    return 'Hello, World!'

@app.get('/menu/<restaurant_id>')
def get_menu(restaurant_id: int):
    # db.get_or_404(MenuItem)
    # user = db.one_or_404(
    #     db.select(MenuItem).filter_by(id=restaurant_id)
    # )
    # return jsonify(user)
    return 5

@app.post('/menu/<restaurant_id>')
def create_menu(restaurant_id: int):
    return 5

@app.get('/menu-item/<menu_item_id>')
def get_menu_item(menu_item_id: int):
    return 5

# Menu
# Menu Item
# Restaurant

