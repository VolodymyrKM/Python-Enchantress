import pytest
from freezegun import freeze_time
from amazon_killer import amazon_killer as app
from users_info import t_create_user, t_response_create_user, t_full_response_from_create_user


@pytest.fixture
def store_app():
    app.config['TESTING'] = True
    with app.test_client() as client:
        return client


@pytest.fixture
def create_user():
    return t_create_user


@pytest.fixture
def response_from_create():
    return t_response_create_user


@pytest.fixture
def full_response_from_create_user():
    return t_full_response_from_create_user


@freeze_time('2021-02-08T14:16:41')
def test_create_user(store_app, create_user, response_from_create,
                     full_response_from_create_user):
    response = store_app.post('/users', json=create_user)

    assert response.status_code == 201
    assert response.json == response_from_create

    user_id = response.json['user_id']
    response = store_app.get(f'/users/{user_id}')
    full_response_from_create_user["user_id"] = user_id

    assert response.status_code == 200
    assert response.json == full_response_from_create_user


@pytest.mark.parametrize('value', range(2, 10))
def test_user_not_found(store_app, value):
    response = store_app.get(f'/users/{value}')
    
    assert response.status_code == 404
    assert response.json == {"error": f"no such user with id {value}"}


def test_put_user(store_app):
    response = store_app.put('/users/1', json={
        "name": "Illia",
        "email": "illia.sukonnik@example.com",
    }
                             )
    assert response.status_code == 200
    assert response.json == {
        "status": "success"
    }


@pytest.mark.parametrize('value', range(2, 100))
def test_put_invalid_user(store_app, value):
    response = store_app.put(f'/users/{value}')
    
    assert response.status_code == 404
    assert response.json == {"error": f"no such user with id {value}"}


def test_delete_user(store_app):
    response = store_app.delete('/users/1')
    
    assert response.json == {"status": "success"}
    assert response.status_code == 200


@pytest.mark.parametrize('value', range(2, 100))
def test_delete_user_invalid_input(store_app, value):
    response = store_app.delete(f'/users/{value}')
    
    assert response.status_code == 404
    assert response.json == {"error": f"no such user with id {value}"}


@freeze_time('2021-02-08T14:16:41')
def test_create_product_carts(store_app):
    response = store_app.post('/add_carts',
                              json=
                              {"user_id": 1,
                               "products": [
                                   {"product": 'Book: how to stop be boring',
                                    "price": 500, },
                                   {"product": 'fireworks',
                                    "price": 1500, }]})
    assert response.json == {"cart_id": 1, "creation_time": '2021-02-08T14:16:41'}
    assert response.status_code == 201

    cart_id = response.json['cart_id']
    response = store_app.get(f'/read_cart/{cart_id}')

    assert response.status_code == 200
    assert response.json == {
        "user_id": 1,
        "creation_time": '2021-02-08T14:16:41',
        "products": [
            {
                "product": 'Book: how to stop be boring',
                "price": 500,
            },
            {
                "product": 'fireworks',
                "price": 1500,
            }
        ]
    }


@pytest.mark.parametrize('value', range(2, 20))
def test_invalid_input_user(store_app, value):
    response = store_app.post('/add_carts',
                              json=
                              {"user_id": value, "products": [], })
    assert response.json == {"error": f"no such user with id {value}"}


def test_update_cart_user(store_app):
    response = store_app.put('/update_cart/1',
                             json={"user_id": 1,
                                   "products": [
                                       {
                                           "product": 'fireworks',
                                           "price": 1500,
                                       }
                                   ]
                                   })
    
    assert response.status_code == 200
    assert response.json == {"status": "success"}


@pytest.mark.parametrize('value', range(2, 20))
def test_update_invalid_cart_input(store_app, value):
    response = store_app.put(f'/update_cart/{value}')

    assert response.status_code == 404
    assert response.json == {"error": f"no such cart with id {value}"}


def test_delete_cart_valid(store_app):
    response = store_app.delete('/del_cart/1')

    assert response.json == {"status": "success"}
    assert response.status_code == 200


@pytest.mark.parametrize('value', range(4, 14))
def test_del_cart_user_invalid(store_app, value):
    response = store_app.delete(f'/del_cart/{value}')

    assert response.json == {"error": f"no such cart with id {value}"}
    assert response.status_code == 404
