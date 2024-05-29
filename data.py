class Urls:
    CREATE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    LOGIN_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    ORDER_CREATE = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'


class Message:
    LOGIN_ALREADY_USE = 'Этот логин уже используется. Попробуйте другой.'
    INSUFFICIENT_DATA_CREATE = 'Недостаточно данных для создания учетной записи'
    INSUFFICIENT_DATA_ENTER = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'


class Order:
    data_order = {
        "firstName": "Artem",
        "lastName": "Besfamilnyi",
        "address": "test address",
        "metroStation": 5,
        "phone": "+7 444 555 66 77",
        "rentTime": 8,
        "deliveryDate": "2024-05-20",
        "comment": "test comment",
        "color": []
    }
