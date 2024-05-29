import json
import allure
import pytest
import requests
from data import Urls, Order


class TestOrderCreate:

    @allure.title('Проверка поля «Цвет самоката»')
    @pytest.mark.parametrize('choose_color', [[], ['GREY'], ['BLACK'], ['BLACK', 'GREY']])
    def test_make_order(self, choose_color):
        payload = Order.data_order
        payload['color'] = choose_color
        payload = json.dumps(payload)
        response = requests.post(Urls.ORDER_CREATE, payload)
        assert response.status_code == 201 and 'track' in response.text


class TestOrderList:

    @allure.title('Проверка списка успешных заказов')
    def test_check_status_order_list(self):
        response = requests.get(Urls.ORDER_CREATE)
        assert response.status_code == 200 and 'orders' in response.text
