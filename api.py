import requests
import allure
import data


@allure.step('Отправляем запрос на создание пользователя')
def create_user(payload):
    return requests.post(data.CREATE_USER_URL, json=payload)


@allure.step('Отправляем запрос на удаление пользователя')
def delete_user(token):
    return requests.delete(data.REMOVE_USER_URL, headers={"Authorization": token})


@allure.step('Создание нового пользователя')
def new_user(credentials):
    response = create_user(credentials)
    response_payload = response.json()
    credentials['accessToken'] = response_payload['accessToken']

    return credentials

@allure.step('Удаление пользователя')
def remove_user(credentials):
    delete_user(credentials['accessToken'])