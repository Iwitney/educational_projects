# Проект по сквозной аналитике для салона красоты. 
У салона красоты есть реклама в онлайне и сайт, через который можно оставить заявку на услугу.  
При помощи сквозной аналитики нужно проследить путь от клика по рекламному объявлению до покупки и, таким образом, оценить эффективность маркетинга.
Необходимо подготовить данные для отчета. Для решения использованы SQL и Python (Pandas). 

Данные были размещены в базе данных PostgreSQL. 

Были написаны функции по:
- выгрузке отчета из базы данных в датафрейм в Jupyter Notebook, 
- записи датафрейма в базу данных PostgreSQL,
- отправке отчета в Google Spreadsheets.

Также был проведен анализ качества данных, поиск логических несоответствий и дубликатов.
Кроме этого по сделанному отчету был разработан небольшой дашборд в Looker Studio. https://datastudio.google.com/reporting/0c01b1be-f9f3-45dd-8459-c07ad0d61f9e
