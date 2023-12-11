# Бот для отслеживания проверок выполненных работ на платформе Devman
Скрипт руководит работой бота, который отслеживает работы, проверенные преподавателем и публикует сообщения о статусе этих работ.

## Как установить
Для работы бота нужет персональный токен DEVMAN API, который можно получить на сайте [devman](https://dvmn.org/)  и токен телеграм бота.
Так же необходимо иметь id пользователя в телеграме.

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```
### Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл .env рядом остальными файлами кода и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Доступно 2 переменные:
* TELEGRAM_TOKEN - токен телеграм-бота полученный при создании бота.
* DEVMAN_TOKEN - персональный API токен ученика на платформе Devman.

#### Запуск скрипта
Для запуска скрипта нежно знать ID телеграм пользователя
```
python bot.py
```
Далее скрипт попросит ввести ID пользователя
```
Введите свой chat id:
```
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).