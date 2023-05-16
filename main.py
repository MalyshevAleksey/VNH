import asyncio
import sqlite3
import websockets

all_clients = []


async def handle_message_from_vk(message: str):
    print('Отправка из бота на сайт')
    # Обработка полученного сообщения (отправка на сайт)
    print('Соединено с сайтом')
    await all_clients[0].send(message)
    print('Отправлено на сайт')


async def handle_message_from_site(message: str):
    print('Отправка с сайта в бота')
    # Обработка полученного сообщения (отправка в вк)
    print('Соединено с вк')
    await all_clients[1].send(message)
    print('Отправлено в вк')


async def add_in_DataBase(type_mess: str, user_id: int, text: str):
    # Сохранение сообщения в базу данных
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages(type, user_id, text) VALUES(?, ?, ?)", (type_mess, user_id, text))
    conn.commit()
    conn.close()


async def send_message(message: str):
    for client in all_clients:
        await client.send(message)


async def new_client_connected(client_socket: websockets.WebSocketClientProtocol, path: str):
    print("Соединение с новым клиентом")
    all_clients.append(client_socket)
    while True:
        try:
            new_message = await client_socket.recv()
            print(new_message)
            print("Новое сообщение от клиента: ", new_message)
            string = new_message.split(' ')
            type_mess = string[0]
            user_id = int(string[1])
            text = ' '.join(string[2:])
            await add_in_DataBase(type_mess=type_mess, user_id=user_id, text=text)
            await send_message(message=new_message)
            # if type_mess == 'vk': # Получение сообщения от клиента с вк
            #     await handle_message_from_vk(message=new_message)
            # if type_mess == 'site': # Получение сообщения от клиента с сайта
            #     await handle_message_from_site(message=new_message)
        except:
            pass


async def start_server():
    async with websockets.serve(new_client_connected, "localhost", 8765):
        await asyncio.Future()


asyncio.run(start_server())
