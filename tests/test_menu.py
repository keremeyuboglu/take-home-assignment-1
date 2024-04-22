from test_base import * # Need those as they're fixtures
import json

test_restaurant_id = 1
insert_menu_item = {
    "type": "INSERT",
    "menu_item_id": 148142
}
delete_menu_item = {
    "type": "DELETE",
    "menu_item_id": 148142
}

def test_get_latest_menu(client):
    response = client.get(rf'/menu/{test_restaurant_id}')
    assert response.status_code == 200

def test_insert_menu_item_to_menu(client):
    response = client.post(rf'/menu/{test_restaurant_id}',
                                data=json.dumps(insert_menu_item),
                                content_type='application/json')
    assert response.status_code == 200
        

def test_delete_menu_item_from_menu(client):
    response = client.post(rf'/menu/{test_restaurant_id}',
                                data=json.dumps(delete_menu_item),
                                content_type='application/json')
    assert response.status_code == 200