# project_online_shop
проект интернет-магазина, который будете дорабатываться на каждом уроке в течение всего курса Django

21.1 fbv и cbv (homework)

+Задание 1
Продолжаем работать с проектом из предыдущего домашнего задания. Переведите имеющиеся контроллеры с FBV на CBV.

Задание 2
+2.1 Создайте новую модель блоговой записи со следующими полями:

заголовок,
slug (реализовать через CharField),
содержимое,
превью (изображение),
дата создания,
признак публикации,
количество просмотров.
+2.2 Для работы с блогом реализуйте CRUD для новой модели.

Задание 3
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:

при открытии отдельной статьи увеличивать счетчик просмотров;
выводить в список статей только те, которые имеют положительный признак публикации;
при создании динамически формировать slug name для заголовка;
после успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.
* 
* Дополнительное задание ( не реализовано)
Когда статья достигает 100 просмотров, отправлять себе на почту поздравление с достижением.

Примечание: для отправки писем рекомендуем использовать почтовый сервис Яндекс.

Дополнительное задание, помеченное звездочкой, выполнять желательно, но не обязательно.