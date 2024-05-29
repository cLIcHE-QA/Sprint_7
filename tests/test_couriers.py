import allure
import pytest
import requests
from data import Urls, Message
from helpers import Delivery


class TestSignUpCourier:

    @allure.title('Проверка создания курьера с валидными данными')
    def test_signup_courier_correct_data(self):
        payload = Delivery.generation_data_for_signup()
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.json().get('ok') == True

    @allure.title('Проверка создания двух одинаковых курьеров')
    def test_signup_two_similar_couriers(self):
        payload = Delivery.generation_data_for_signup()
        requests.post(Urls.CREATE_COURIER, data=payload)
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 409 and response.json()['message'] == Message.LOGIN_ALREADY_USE

    @allure.title('Создаем курьера без поля логина/пароля.')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_signup_courier_without_one_field(self, field):
        payload = Delivery.signup_courier()
        del payload[field]
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 400 and response.json()['message'] == Message.INSUFFICIENT_DATA_CREATE


class TestSignInCourier:

    @allure.title('Проверка авторизации курьера')
    def test_signin_courier(self):
        payload = Delivery.signup_courier()
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @pytest.mark.parametrize('field', ['login', 'password'])
    @allure.title('Проверка авторизации с невалидным значением поля логина/пароля')
    def test_signin_with_wrong_one_values_field(self, field):
        payload = Delivery.signup_courier()
        payload[field] = ''
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 400 and response.json()['message'] == Message.INSUFFICIENT_DATA_ENTER

    @allure.title('Проверка авторизации без поля логина')
    def test_signin_without_one_field(self):
        payload = Delivery.signup_courier()
        del payload['login']
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 400 and response.json()['message'] == Message.INSUFFICIENT_DATA_ENTER

    @allure.title('Проверка авторизации несуществующего курьера')
    def test_signin_with_non_existent_courier(self):
        payload = Delivery.signup_courier()
        payload['login'] = payload['login'] + '1'
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 404 and response.json()['message'] == Message.ACCOUNT_NOT_FOUND
