# telegram-ask-bot
Простой бот обратной связи в Telegram

## Шаги для развертывания на сервре:
### Необходимо:
 - сервер (ubuntu 20.04, а лучше сразу с Docker)
 - домен (в любой зоне и за любую цену)
## Шаги:
 - Купить домен
 - Арендовать сервер
    - Можно взять уже с предуствновленным докером
 - Установить Docker на сервер (если нужно) 
    - https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
 - Подключиться к серверу 
 - Устанавливаем Nginx 
    - `sudo apt-get update`
    - `sudo apt-get install -y nginx`
 - Настраиваем Nginx:
    - Открываем `bot.conf`, заменяя MY_URL на ваш в формате bot.site.com 
    - Копируем конфигурационный файл в директории Nginx
      - `sudo cp -f bot.conf /etc/nginx/sites-enabled`
      - `sudo cp -f bot.conf /etc/nginx/sites-available`
    - Перезапускаем Nginx
      - `sudo service nginx restart`
    - Если ошибки не выдало, значит конфиги верны
 - Настраиваем SSL и HTTPS 
    - Переходим на сайт certbot https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal
    - Исполняем команды с 1 по 7-ю.
## Запускаем проект:
 - Склонировать репозиторий
    - `git clone <link>`  
 - Переходим в папку с проектом
    - `cd telegram-ask-bot`
 - Собираем образ docker
 `docker build -t tgbotimg .` 
 - Запускаем контейнер, заменив значение ADMIN_CHAT_ID, BOT_API_KEY и URL на свои.
 ```docker run --name tgbot -d --restart=always \
    -p 8005:8000 \
    -e ADMIN_CHAT_ID=112233 \
    -e BOT_API_KEY=112233:AAQQWW \
    -e URL=bot.site.com \
    tgbotimg
