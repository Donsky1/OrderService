# OrderService
Задание. Нужно сделать сервис, в котором пользователи смогут заказывать товары из-за рубежа.
<h2>Service on Django</h2>

<p id='#overview'>В проекте реализовано 2 приложения: userapp - пользователи, orderapp - основное приложение. При запуске сервиса откроется страница входа, если пользователя нет, можно его зарегистрировать (ссылка прилагается ниже на странице входа). Чтобы пользователь смог зайти на сайт, его необходимо сделать в админке "персоналом" (is_staff) и выдать соотв. права для работы с таблицей заказов и товарами. </p>
<p>Логика работы реализована в соотв. с техническим заданием.</p>

<br>
<h2 id='installation'>Установка (с использованием docker)</h2>
<p>1. Клонируем проект<p>

```
git clone https://github.com/Donsky1/OrderService.git
```
<p>2. Переходим в папку с проектом, выполнив команду cd <p>

```
cd order_project
```
<p>3. Запускаем контейнер, используя docker compose up<p>
  
```
docker compose up -d
```
<p>4. (option) В некоторых случаях может потребоваться перезапустить контейнеры, выполнив<p>

  ```
docker compose down
docker compose up -d
```
<p>5. Узнаем имя web контейнера, чтобы выполнить команды django: makemigrations и migrate, createsuperuser<p>

  ```
docker ps
docker exec -ti order_project-web-1 bash
python manage.py makemigrations
python manage.py makemigrations userapp
python manage.py makemigrations orderapp
python manage.py migrate
python manage.py createsuperuser
```
<p>Выполнив все необходимые настройки и создав пользователя теперь можно зайти на сайт, используя созданного на предыдущем шаге администратора.<p>
