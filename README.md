# OrderService
Задание. Нужно сделать сервис, в котором пользователи смогут заказывать товары из-за рубежа.
<h2>Service on Django</h2>

<p id='#overview'>В проекте реализовано 2 приложения: userapp - пользователи, orderapp - основное приложение.</p>
<br>
<h2 id='installation'>Установка (с использованием docker)</h2>
<p>1. Создаем директорию, клонируем проект в эту папку ... <p>

```
git clone https://github.com/Donsky1/OrderService.git
```
<p>2. Переходим в папку с проектом, выполнив команду cd <p>

```
cd order_project
```
<p>3. Запускаем контейнер  использую docker compose up<p>
  
```
docker compose up -d
```
<p>4. Создадим новые миграции<p>

  ```
manage.py makemigrations 
```
<p>5. Применим миграции <p>

  ```
manage.py migrate  
```
