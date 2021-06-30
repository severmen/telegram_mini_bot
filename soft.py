import requests
import copy
import random

def main():
    url = "https://api.telegram.org/<token>/"
    count = 0
    last_date = None

    def get_updates_json(request, ):  
        response = requests.get(request + 'getUpdates?')
        return response.json()

    def send_mess(chat, text):  
        params = {'chat_id': chat, 'text': text}
        response = requests.post(url + 'sendMessage', data=params)
        return response
        
    while True:
        b = None
        result_updates = get_updates_json(url)
        for a in result_updates.get('result'):
            b = a
        try:
            last_message_info = b.get('message')
        except:
            last_message_info = b.get('my_chat_member')
        try:
            user_info = copy.copy(last_message_info.get('from'))
        except:
            last_message_info = b.get('my_chat_member')
            user_info = copy.copy(last_message_info.get('from'))

        if str(last_message_info.get('date')) != str(last_date):
            if last_message_info.get('text') == "Хочу пожелание!":
                suggestions = ["Успехов в работе! Благополучия во всем!"
                ,"Самые искренние пожелания хорошего дня и отличного настроения только для тебя.",
                "Желаю тебе желания идти вперёд! Душевного спокойствия!",
                "Не трать время на дрему, торопись навстречу своей удаче в новом дне!",
                "Пускай этот прекрасный день принесет удачу, а также счастье и тепло, и ещё я пожелаю, чтобы тебе сегодня волшебно повезло!",
                "Душевного спокойствия! Хорошего настроения!",
                "Пусть начиная с этого утра, весь мир принадлежит только тебе!",
                "Настало прекрасное утро, оно так и манит выйти в этот мир и достигать!"
                'Желаю тебе желания идти вперёд! Уверенности в себе!',
                'Красивых чувств! Фейерверка эмоций!' ]
                randInt = random.randint(0, (len(suggestions)-1))
                send_mess(str(user_info.get('id')), str(suggestions[randInt]))
            else:
                send_mess(str(user_info.get('id')), "Привет "+(user_info.get('first_name'))+
                    " " + str(user_info.get('last_name'))+ " я принял твоё сообщение "+
                    last_message_info.get('text')+" ну не знаю как с ним быть :( "+
                    "но я могу пожелать тебе кое-что. Хочешь? Ну тогда напиши"
                    +" \"Хочу пожелание!\"")
            count += 1
            print("Всего было обращений " + str(count))
            last_date = str(last_message_info.get('date'))
    
if __name__ == "__main__":
    main()
