import requests
import allure
import data


@allure.step('Отправляем запрос на создание пользователя')
def create_user(payload):
    return requests.post(data.CREATE_USER_URL, json=payload)


@allure.step('Отправляем запрос на удаление пользователя')
def delete_user(token):
    return requests.delete(data.REMOVE_USER_URL, headers={"Authorization": token})