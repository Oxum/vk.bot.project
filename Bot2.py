import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(
    token='0fee6d3eea0e4f7ea1950c5d930230fcce3f19eeb6cb68f7f1f04bf482b63db3014f3276326a186668f8d')  # токен вашей группы
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '180495402')  # цифровой id вашей группы


def main():
    keyboard1 = VkKeyboard(one_time=False)  # создаем клавиатуру. False - клавиатура после нажатия не будет закрываться. True - будет.
    keyboard1.add_button('Помощь', color=VkKeyboardColor.POSITIVE)  # цвета. POSITIVE - Зелёный. NEGATIVE - Красный. PRIMARY - Синий
    keyboard1.add_button('Привет', color=VkKeyboardColor.POSITIVE)  # цвета. POSITIVE - Зелёный. NEGATIVE - Красный. PRIMARY - Синий
    keyboard1.add_line()  # добавляем ещё одну строку для клавиатуры
    keyboard1.add_button('Закрыть клавиатуру', color=VkKeyboardColor.NEGATIVE)

    helpmsg = ''' Помощь ответ! '''
    hellomsg = ''' Привет! '''
    Menusmg = ''' Вы бери из списка, что тебе нужно: '''

    while True:  # бесконечная проверка на получение событий в группе (если поймаем ошибку)
        try:  # ловим ошибку
            for event in longpoll.listen():

                if event.type == VkBotEventType.MESSAGE_NEW and event.object.text.lower() == 'помощь':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=helpmsg,
                                     random_id=0)
                # отправляем пользователю пзаготовленное сообщение hellomsg

                if event.type == VkBotEventType.MESSAGE_NEW and event.object.text.lower() == 'привет':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=hellomsg,
                                     random_id=0)
                # отправляем пользователю заготовленное сообщение hellomsg.

                if event.type == VkBotEventType.MESSAGE_NEW and event.object.text.lower() == 'начать':
                    vk.messages.send(peer_id=event.object.peer_id,
                                     message=Menusmg,
                                     keyboard=keyboard1.get_keyboard(),
                                     random_id=0)
                # По команде начать (вызываем клавиатуру)

                if event.type == VkBotEventType.MESSAGE_NEW and event.object.text.lower() == 'закрыть клавиатуру':
                    vk.messages.send(peer_id=event.obj.peer_id,
                                     message='Клавиатура закрыта, чтобы заново вызвать введите: начать',
                                     random_id=0,
                                     keyboard=keyboard1.get_empty_keyboard())
                # отправляем пользователю пустую клавиатуру и сообщение о успешном закрытии

                if event.type == VkBotEventType.MESSAGE_NEW and event.object.text.lower() == 'тро':
                    vk.messages.send(user_id=460193519,
                                     message='Вызвали')
                # отправляем пользователю заготовленное сообщение hellomsg.

        except Exception as e:
            print('')  # выводим сообщение о том что получили ошибку


if __name__ == '__main__':
    main()