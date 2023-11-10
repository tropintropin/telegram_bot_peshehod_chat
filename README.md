# Бот-помощник в Telegram для компании «Пешеход Тур»

[![wakatime](https://wakatime.com/badge/github/tropintropin/telegram_bot_peshehod_chat.svg)](https://wakatime.com/badge/github/tropintropin/telegram_bot_peshehod_chat)
[![version badge](https://img.shields.io/badge/Python-3.10_|_3.11-blue.svg)](https://www.python.org/)
[![version badge](https://img.shields.io/badge/aiogram-3.2.0-blue.svg)](https://docs.aiogram.dev/en/dev-3.x/)
[![Telegram Bot API](https://img.shields.io/badge/dynamic/json?color=blue&logo=telegram&label=Telegram%20Bot%20API&query=%24.api.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Faiogram%2Faiogram%2Fdev-3.x%2F.butcher%2Fschema%2Fschema.json&style=flat-square)](https://core.telegram.org/bots/api)

[![version badge](https://img.shields.io/badge/Peshehod_Help_Bot-v0.0.1b-blue.svg)](https://t.me/peshehod_help_bot)
[![copyright](https://img.shields.io/badge/©_Peshehod_Tour-2023-blue.svg)](https://peshehodtour.ru)
[![developer](https://img.shields.io/badge/Developer-Valery_Tropin-blue.svg)](https://tropin.one)

Бот написан по заказу компании [«Пешеход Тур»](https://peshehodtour.ru) в 2023 году.

Разработчик Валерий Тропин — [tropin.one](https://tropin.one).

<!-- vim-markdown-toc GFM -->

* [Стек](#Стек)
* [План по запуску разделов бота](#План-по-запуску-разделов-бота)
* [Рабочая схема разделов бота](#Рабочая-схема-разделов-бота)

<!-- vim-markdown-toc -->

## Стек

Бот написан на **Python 3.11** с использованием фреймворка **aiogram 3.2.0**.

Информация о пользователях и данные для FSM хранятся и обрабатываются с помощью **Redis**.

Зависимости указаны в файле [`requirements.txt`](requirements.txt).

Документация (docstrings) для классов, функций и методов написана при неоценимой поддержке [GPT-3.5](https://chat.openai.com).

Токен бота хранится в файле `.env`. В корне репозитория есть файл [`.env.example`](.env.example). Переименуйте его в `.env`
и вставьте внутрь токен от своего бота, полученный от [`@BotFather`](https://t.me/botfather).


## План по запуску разделов бота

- [x] Вводное слово 2023.06.14
- [x] Список всех туров (код написан к 2023.08.04)
- [x] ЧАВо (код написан к 2023.08.04)
- [ ] База данных пользователей (для статистики и последующего слияния с ORM)
- [x] Контакты 2023.08.13
- [ ] Оставить отзыв
- [ ] Анкета выбора тура (в процессе)
- [ ] Викторина

```mermaid
gantt
title       График работы
dateFormat  YYYY.MM.DD
axisFormat  %Y.%m.%d
excludes    
section     Development
Начало работы над ботом         :mileston,      2023.04.03, 
JSON-словари для бота           :done,      a0, 2023.04.05, 2023.05.18
Вводное слово                   :done,      a1, 2023.05.19, 2023.06.14
Список всех туров               :done,    a2, 2023.06.15, 60d
ЧАВо                            :done,    a3, 2023.06.15, 60d
Переработать гл. меню           :done,      a5, 2023.08.05, 2d
Контакты и Справка              :done,      a6, 2023.08.13, 1d
Анкета выбора тура              :active,    a7, 2023.11.03, 7d
section     Production
Тестовый запуск бота (v0.0.1b)  :mileston,      2023.06.14,
Бот-заглушка                    :active,    b0, 2023.06.14, 60d
```

## Рабочая схема разделов бота

```mermaid
graph LR
    id0{<strong>Точка входа<br><code>/start</code></strong>}
    id0 ==> id1{{Вводое слово}}
    id0 ==> id9{{<i>Главное меню<br>с командами</i>}}
    id0 ==> id10{{<i>Справка<i/><br><code>/help</code>}}
    id1 --> id8[(База данных<br>пользователей)]
    id1 --> id2{{ЧАВо<br><code>/faq</code>}}
        id2 -.-> id20>Оплата и бронирование]
        id2 -.-> id21>Места встреч]
        id2 -.-> id22>Как проходит экскурсия]
        id2 -.-> id23>Ваши экскурсии<br>и отзывы]
            id23 -.->|Реализация после<br>интеграции с ORM| id232><i>График экскурсий<br>на неделю</i>]
            id23 -.->|Реализация после<br>запуска основных разделов| id230><i>Прогноз погоды<br>в день экскурсии</i>]
            id23 -..->|<i>Переход в раздел экскурсий</i>| id7
            id23 -..->|<i>Переход в раздел отзывов</i>| id4
    id1 --> id7{{Список всех экскурсий<br><code>/tours</code>}}
        id7 -.-> id71>Групповые]
        id7 -.-> id72>Индивидуальные]
    id1 --> id3>Контакты<br><code>/contacts</code>]
    id1 --> id4>Оставить отзыв]
    id1 --> id5(Анкета:<br>подбери себе тур)
        id5 -..->|<i>Переход в раздел экскурсий</i>| id7
    id1 --> id6{{Викторина}}
```
