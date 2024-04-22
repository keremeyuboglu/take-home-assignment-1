from test_base import * # Need those as they're fixtures
import json

test_restaurant_id = 1
insert_menu_item = {
    "name": "Test Item Name",
    "description": "Test Description",
    "stock_status": "IN_STOCK",
    "image": "temp/xx.jpeg",
}

def test_create_menu_item(client):
    response = client.post(rf'/menu-item/{test_restaurant_id}',
                                data=json.dumps(insert_menu_item),
                                content_type='application/json')
    assert response.status_code == 200