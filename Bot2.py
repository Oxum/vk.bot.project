import vk_api
import random
import time

#Наш токен полученный с группы вк
token = "0fee6d3eea0e4f7ea1950c5d930230fcce3f19eeb6cb68f7f1f04bf482b63db3014f3276326a186668f8d"


vk = vk_api.VkApi(token=token)

vk._auth_token()

#У кнопок может быть один из 4 цветов:
#1. primary — синяя кнопка, обозначает основное действие. #5181B8
#2. default — обычная белая кнопка. #FFFFFF
#3. negative — опасное действие, или отрицательное действие (отклонить, удалить и тд). #E64646
#4. positive — согласиться, подтвердить. #4BB34B

while True:
    try:
    #Присоединяемся к серверу
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
    #Задаем сообщение, которое должен ввести пользователь!(С маленькой буквы!)
            if body.lower() == "привет":
    #Что мы будем отвечать на это слово!
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "кто я?":
                vk.method("messages.send", {"peer_id": id, "message": "Ты хороший человек", "random_id": random.randint(1, 2147483647)})

    except Exception as E:
        time.sleep(1)
#Доделать клавиатуру и научить отправлять аудио
