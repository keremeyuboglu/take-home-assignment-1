from app import create_app
import os
import json

test_restaurant_id = 7
insert_menu_item = {
    "type": "INSERT",
    "name": "Test Item Name",
    "description": "Test Description",
    "stock_status": "IN_STOCK",
    "restaurant_id": test_restaurant_id,
    "image": "temp/xx.jpeg",
}

def test_create_menu_item():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.post(rf'/menu/{test_restaurant_id}',
                                    data=json.dumps(insert_menu_item),
                                    content_type='application/json')
        print(response.data)
        assert response.status_code == 200