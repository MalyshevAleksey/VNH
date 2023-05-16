import asyncio
import vk_api
import websocket
from random import randint
from vk_api.longpoll import VkLongPoll, VkEventType


# Отправка сообщения на сервер
async def send_message(message):
    # Отправка сообщения серверу
    ws.send(message)
    print(f"Sent message: {message}")


# Отправка пользователю <user_id> сообщения <message>
def write_msg(user_id, message, vk):
    print(f'Отправка сообщения: "{message}"')
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": randint(1241241, 324823592373247)})
    print('Сообщение отправлено')


# Получение имени и фамилии пользователя
def getUsername(user_id, vk):
    user = vk.method("users.get", {"user_ids": user_id})
    fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
    return fullname


# Получение сообщение ботом от пользователя
async def handle_event(event, vk):
    # Если оно имеет метку для меня (то есть бота)
    if event.to_me:
        print('Получено для бота')
        # Сообщение от пользователя
        request = event.text
        request = request.lower()
        print(f'Полученное сообщение от {getUsername(event.user_id, vk)} [{event.user_id}]: "{request}"')
        await send_message(f"vk {event.user_id} {request}")
        write_msg(event.user_id, "Хай", vk)


# Функция ожидания ответа от сервера
async def wait_server_message():
    while True:
        new_message = await ws.recv()
        print(new_message)


async def long_pool_func():
    for event in longpoll.listen():
        # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW:
            print('Получено сообщение')
            await handle_event(event, vk)


async def main():
    while True:
        await long_pool_func()
        await wait_server_message()



# API-ключ
token = "vk1.a.5sbN9G_n0PFGTDoHBRRBAC0knipzqKwjdS0zJysTKZzcyquQ" \
        "z5DZ38zFbE6nadRTtmcUTUkmmyF9cS7mmaIz4zOuzDWN0VgAAZGsGxl" \
        "pz_Y_LwTgBy2Bf0iA07wBbv-eQXogbg-eMHvqMfjv_81nN19vLjwY8EO" \
        "fr70ZAdEyn-XRsACbV_IV2dIhxrPDYRVEiLeq0pf_7M16rEDgqf64tg"
print('Токен получен')

# Создание соединения клиент-сервер
ws = websocket.WebSocket()
ws.connect('ws://localhost:8765')

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)
print('Авторизован как сообщество')

# Работа с сообщениями
longpoll = VkLongPoll(vk)
print('longpoll готов')

asyncio.run(main())
