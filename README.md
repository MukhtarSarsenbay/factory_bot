# factory_bot
 Описание
С помощью Django и Django REST Framework написать API для приёма сообщений и отправки их в Telegram бот.
Функционал готового задания должен выглядеть следующим образом: через API получаем сообщение, его потом отправляем в Telegram бот.
Схема работы:
1. Пользователь регистрируется в нашей системе. При регистрации указывает логин, пароль и имя
2. Пользователь находит бота в Telegram и подписывается на него. На этом этапе требуется создать Telegram бота.
3. В личном кабинете генерирует токен и привязывает этот токен к своему чату. Простой способ реализации: любое входящее сообщение от пользователя бот запоминает как токен пользователя
4. Пользователь отправляет на API своё сообщение. В этот момент бот сразу дублирует его в Telegram. Пользователь должен получать только свои сообщения.
Формат сообщения:
{Имя пользователя}, я получил от тебя сообщение: {Сообщение}
Сообщение должно идти с новой строки.
Функционал:
1. Авторизация
2. Регистрация
3. Генерация токена для телеграм бота. (Только после авторизации)
4. Отправка сообщений своему боту. На сервере фиксировать: дату и тело
сообщения. (Только после авторизации)
5. Получение списка всех сообщений: дата отправки, сообщение (Только после
авторизации)
Функционал выше должен работать через REST API.
Результат
1. Загрузить на сервер (запустить можно на https://try.digitalocean.com/freetrialoffer/ или другом альтернативном варианте)
2. Скинуть ссылку на бота
3. Залить исходный код на GitHub
Информацию отправляйте по ссылке:
https://docs.google.com/forms/d/e/1FAIpQLSdtx-nktEVsSm8yAaHCKE3NbJPwQ0jImxQFEJ u-_m1eIMJ5zg/viewform?usp=sf_link
Важно. Отправить результат тестового задания в гугл форму, потому что в hh.kz сообщение затеряется и мы можем не увидеть вовремя вашу работу.
   
