import requests

URL_SERVICE = "https://3e71a59e-ba1a-4aac-8016-bb658069c5ac.serverhub.praktikum-services.ru"
CREATE_ORDER = "/api/v1/orders"
GET_BY_TRACK = "/v1/orders/track?t="

order_body = {
    "firstName": "Соул",
    "lastName": "Гудман",
    "address": "Альбукерке, 12",
    "metroStation": "1",
    "phone": "01234567890",
    "rentTime": 5,
    "deliveryDate": "2023-03-23",
    "comment": "Комментарий",
    "color": [
        "BLACK"
    ]
}

order_by_tracker = {
    "order": {
        "id": "",
        "firstName": "Соул",
        "lastName": "Гудман",
        "address": "Альбукерке, 12",
        "metroStation": "1",
        "phone": "01234567890",
        "rentTime": 5,
        "deliveryDate": "2023-03-23",
        "track": "",
        "status": 2,
        "color": [
            "BLACK"
        ],
        "comment": "Комментарий",
        "cancelled": False,
        "finished": False,
        "inDelivery": False,
        "courierFirstName": "Курьер",
        "createdAt": '2023-03-23',
        "updatedAt": '2023-03-23'
    }
}


# Создание нового заказа
def post_new_order(body):
    return requests.post(URL_SERVICE + CREATE_ORDER,
                         json=body)


# Получения заказа по треку заказа
def get_order_by_track(track):
    return requests.get(URL_SERVICE + GET_BY_TRACK + f'{track}')


def test_create_new_order():
    # Выполнить запрос на создание заказа
    resp_order = post_new_order(order_body)
    # print(resp_order)

    assert resp_order.status_code == 201


def test_get_order_by_track():
    # Выполнить запрос на создание заказа
    resp_order = post_new_order(order_body)

    assert resp_order.status_code == 201

    # Сохранить номер трека заказа
    track = resp_order.json()['track']

    # Выполнить запрос на получения заказа по треку заказа
    resp = get_order_by_track(track)

    # Проверить, что код ответа равен 200
    assert resp.status_code == 200
