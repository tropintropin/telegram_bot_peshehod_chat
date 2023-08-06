# Бот-помощник в Telegram для компании «Пешеход Тур»

[![wakatime](https://wakatime.com/badge/github/tropintropin/telegram_bot_peshehod_chat.svg)](https://wakatime.com/badge/github/tropintropin/telegram_bot_peshehod_chat)
[![version badge](https://img.shields.io/badge/Python-3.10_|_3.11-blue.svg)](https://docs.aiogram.dev/en/dev-3.x/)
[![version badge](https://img.shields.io/badge/aiogram-3.0.0b9-blue.svg)](https://docs.aiogram.dev/en/dev-3.x/)
[![Telegram Bot API](https://img.shields.io/badge/dynamic/json?color=blue&logo=telegram&label=Telegram%20Bot%20API&query=%24.api.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Faiogram%2Faiogram%2Fdev-3.x%2F.butcher%2Fschema%2Fschema.json&style=flat-square)](https://core.telegram.org/bots/api)

[![copyright](https://img.shields.io/badge/©_Peshehod_Tour-2023-blue.svg)](https://peshehodtour.ru)
[![developer](https://img.shields.io/badge/Developer-Valery_Tropin-blue.svg)](https://tropin.one)

Бот написан по заказу компании [«Пешеход Тур»](https://peshehodtour.ru) в 2023 году.

Разработчик Валерий Тропин — [tropin.one](https://tropin.one).

## Стек

Бот написан на *Python* с использованием фреймворка *aiogram*.

*Python* 3.11  
*aiogram* v3 (beta)

Документация (docstrings) для классов, функций и методов написана при неоценимой поддержке *GPT 3.5*.

Токен бота хранится в файле `.env`.

В корне репозитория есть файл [`.env.example`](.env.example). Переименуйте его в `.env`
и вставьте внутрь токен от своего бота, полученный от [`@botfather`](https://t.me/botfather).


## План по запуску разделов бота

- [x] Вводное слово 2023.06.14
- [ ] Список всех туров (код написан к 2023.08.04)
- [ ] ЧАВо (код написан к 2023.08.04)
- [ ] База данных пользователей (для статистики и последующего слияния с ORM)
- [ ] Контакты
- [ ] Оставить отзыв
- [ ] Анкета (подбери себе тур)
- [ ] Викторина

```mermaid
gantt
title       График работы
dateFormat  YYYY.MM.DD
axisFormat  %Y.%m.%d
excludes    
section     Development
Начало работы над ботом :mileston,      2023.04.03, 
JSON-словари для бота   :done,      a0, 2023.04.05, 2023.05.18
Вводное слово           :done,      a1, 2023.05.19, 2023.06.14
Список всех туров       :active,    a2, 2023.06.15, 60d
ЧАВо                    :active,    a3, 2023.06.15, 60d
Переработать гл. меню   :done,      a5, 2023.08.05, 2023.08.06
section     Production
Тестовый запуск бота    :mileston,      2023.06.14,
Бот-заглушка            :active,    b0, 2023.06.14, 60d
```

## Рабочая схема разделов бота

```mermaid
graph LR
    id0{<strong>/start</strong>}
    id0 ==> id1{{Вводое слово}}
    id0 ==> id9{{Главное меню<br>с командами}}
    id1 --> id8[(База данных<br>пользователей)]
    id1 --> id2{{ЧАВо}}
        id2 -.-> id20>Оплата и бронирование]
        id2 -.-> id21>Места встреч]
        id2 -.-> id22>Как проходит экскурсия]
        id2 -.-> id23>Ваши экскурсии<br>и отзывы]
            id23 -.->|???| id232><i>График экскурсий<br>на неделю</i>]
            id23 -.->|???| id230><i>Прогноз погоды</i>]
            id23 -..->|<i>Переход в раздел экскурсий</i>| id7
            id23 -..->|<i>Переход в раздел отзывов</i>| id4
    id1 --> id7{{Список всех<br>экскурсий}}
        id7 -.-> id71>Групповые]
        id7 -.-> id72>Индивидуальные]
    id1 --> id3>Контакты]
    id1 --> id4>Оставить отзыв]
    id1 --> id5(Анкета:<br>подбери себе тур)
        id5 -..->|<i>Переход в раздел экскурсий</i>| id7
    id1 --> id6{{Викторина}}
```
