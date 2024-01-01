# Бот-помощник в Telegram для компании «Пешеход Тур»

[![wakatime](https://wakatime.com/badge/github/tropintropin/telegram_bot_peshehod_chat.svg)](https://wakatime.com/badge/github/tropintropin/telegram_bot_peshehod_chat)
[![version badge](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![version badge](https://img.shields.io/badge/aiogram-3.3.0-blue.svg)](https://docs.aiogram.dev/en/dev-3.x/)
[![Telegram Bot API](https://img.shields.io/badge/dynamic/json?color=blue&logo=telegram&label=Telegram%20Bot%20API&query=%24.api.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Faiogram%2Faiogram%2Fdev-3.x%2F.butcher%2Fschema%2Fschema.json&style=flat-square)](https://core.telegram.org/bots/api)

[![version badge](https://img.shields.io/badge/Peshehod_Help_Bot-v1.0.0-blue.svg)](https://t.me/peshehod_help_bot)
[![copyright](https://img.shields.io/badge/©_Peshehod_Tour-2023-blue.svg)](https://peshehodtour.ru)
[![developer](https://img.shields.io/badge/Developer-Valery_Tropin-blue.svg)](https://tropin.one)

Бот написан по заказу компании [«Пешеход Тур»](https://peshehodtour.ru) в 2023 году.

Разработчик Валерий Тропин — [tropin.one](https://tropin.one).

<!-- vim-markdown-toc GFM -->

* [Стек](#Стек)
* [Готовность разделов](#Готовность-разделов)
* [График работы](#График-работы)
* [Перспективная схема разделов бота](#Перспективная-схема-разделов-бота)

<!-- vim-markdown-toc -->

## Стек

Бот написан на **Python 3.12** с использованием фреймворка **aiogram 3.3.0**. Под **Python 3.10+** тоже работает.

Данные для FSM хранятся и обрабатываются с помощью **Redis** и **SQLite**.

> Необходимо отдельно установить Redis и SQLite в систему, запустить сервер Redis в фоновом режиме, чтобы бот заработал.

<details>
<summary><i>Подробнее про установку Redis и SQLite на Ubuntu и другие ОС</i></summary>

Установка [Redis](https://timeweb.cloud/tutorials/redis/ustanovka-i-nastrojka-redis-dlya-raznyh-os)
<br>
`sudo apt install redis`
<br>
`sudo service redis-server restart`
<br>
`redis-cli ping` → если вернул `PONG`, то сервер запущен.

Установка [SQLite](https://timeweb.cloud/tutorials/sqlite/rukovodstvo-po-nastrojke-sqlite)
<br>
`sudo apt install sqlite3`
<br>
`sqlite3 --version`
</details>

Зависимости указаны в файле [`requirements.txt`](requirements.txt).

Документация для модулей, классов, функций и методов, аннотации типов написаны при неоценимой поддержке [GPT-3.5](https://chat.openai.com) и [Phind Model](https://www.phind.com).

Токен бота хранится в файле `.env`. В корне репозитория есть файл [`.env.example`](.env.example). Переименуйте его в `.env`
и вставьте внутрь токен от своего бота, полученный от [`@BotFather`](https://t.me/botfather).

> Либо используйте секреты Docker для добавления токена бота и прочей чувствительной информации в контейнер на проде — библиотека `environs`, которая используется в проекте, в теории, сможет извлечь переменные окружения оттуда тоже.

## Готовность разделов

- [x] 2023.06.14 Вводное слово
- [x] 2023.08.04 Список всех туров
- [x] 2023.08.04 ЧАВо
- [x] 2023.08.13 Контакты
- [x] 2023.12.01 Анкета выбора тура
- [x] 2023.12.27 Раздел с лекциями «Винные хроники»
- [x] 2023.12.29 Бонус от Пешехода
- [x] 2023.12.30 Оставить отзыв
- [ ] Стикерпак от Пешехода

## График работы
```mermaid
gantt
title       График работы
dateFormat  YYYY.MM.DD
axisFormat  %Y.%m
excludes    
todayMarker on

section     DEVELOPMENT

Начало работы                       :milestone,             2023.04.03, 
JSON-словари для бота               :done,          A0,     2023.04.05,     2023.05.18
Вводное слово                       :done,          A1,     2023.05.19,     2023.06.14
Список всех туров                   :done,          A2,     2023.06.15,     60d
ЧАВо                                :done,          A3,     2023.06.15,     60d
Переработать гл. меню               :done,          A5,     2023.08.05,     2d
Контакты и Справка                  :done,          A6,     2023.08.13,     1d
Анкета выбора тура                  :done,          A7,     2023.11.03,     2023.12.01
Ревизия данных (с апреля)           :done, crit,    A8,     2023.12.02,     2023.12.27
Винные хроники                      :done,          A9,     2023.12.27,     2d
Оставить отзыв                      :done,          A10,    2023.12.27,     3d
Стикерпак от Пешехода               :active,        A11,    2023.12.30,     1w
Работа над ошибками                 :crit,          A12,    after A11,      1w
Ревизия документации                :               A13,    after A12,      1w

section     PRODUCTION

Тестовый запуск бота v0.0.1b        :milestone, done,       2023.06.14,
Бот-заглушка v0.0.1b                :done,          B0,     2023.06.14,     2023.12.31
Запуск бота в production v1.0.0     :milestone, crit,       2023.12.31,
Бот v1.0.0                          :active,        B1,     2023.12.31,     2w
```

## Перспективная схема разделов бота

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
