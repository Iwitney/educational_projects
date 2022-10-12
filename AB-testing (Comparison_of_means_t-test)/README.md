В очень крупной компании по доставке пиццы ведется работа над приложением для курьеров.

Есть несколько ресторанов в разных частях города и целый штат курьеров. Но есть одна проблема — к вечеру скорость доставки падает из-за того, что курьеры уходят домой после рабочего дня, а количество заказов лишь растет. Это приводит к тому, что в момент пересмены доставка очень сильно проседает в эффективности. 

Data scientist-ы придумали новый алгоритм, который позволяет курьерам запланировать свои последние заказы перед окончанием рабочего дня так, чтобы их маршрут доставки совпадал с маршрутом до дома. То есть, чтобы курьеры доставляли последние свои заказы за день как бы "по пути" домой. 

Было решено раскатить A/B тест на две равные группы курьеров. Часть курьеров использует старый алгоритм без опции "по пути", другие видят в своем приложении эту опцию и могут ее выбрать. Исходные данные включают разбивку на тестовую и контрольные выборки.  
<b>Задача</b> – проанализировать данные эксперимента и помочь бизнесу принять решение о раскатке новой фичи на всех курьеров.


#### Описание данных
- <b>order_id</b> - id заказа
- <b>delivery_time</b> - время доставки в минутах
- <b>district</b> - район доставки
- <b>experiment_group</b> - экспериментальная группа