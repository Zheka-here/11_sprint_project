#Иванов Евгений, 18-я когорта - Финальный проект. Инженер по тестированю плюс

import data
import sender_stand_request

#Функция получения трека заказа
def get_order_track():
    order_body = data.order_body.copy()
    response_create_order = sender_stand_request.create_new_order(order_body)
    order_track = response_create_order.json()["track"]
    return order_track

def get_order_assert():
    track = get_order_track()
    response_get_order = sender_stand_request.get_order(track)
    assert response_get_order.status_code == 200

# Тест 1. Проверка получения данных о заказе
def test_get_order_success_response():
    get_order_assert()
