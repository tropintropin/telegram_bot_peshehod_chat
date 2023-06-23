# Бот-помощник в Telegram для компании «Пешеход Тур»

[![wakatime](https://wakatime.com/badge/github/tropintropin/telegram_bot_peshehod_chat.svg)](https://wakatime.com/badge/github/tropintropin/telegram_bot_peshehod_chat)

©2023 [Пешеход Тур](https://peshehodtour.ru)

Разработчик: Валерий Тропин, [tropin.one](https://tropin.one)

## Стек

Бот написан на *Python* с использованием фреймворка *aiogram*.

*Python* 3.11  
*aiogram* v3 (beta)

Токен бота хранится в файле `.env`.

В корне репозитория есть файл [`.env.example`](.env.example). Переименуйте его в `.env`
и вставьте внутрь токен от своего бота, полученный от [`@botfather`](https://t.me/botfather).


## План по запуску разделов бота

- [x] Вводное слово 2023.06.14
- [ ] ЧАВо
- [ ] Контакты
- [ ] Оставить отзыв
- [ ] Анкета (подбери себе тур)
- [ ] Викторина

## Рабочая схема разделов бота

```mermaid
graph LR
    id0(/start)
    id0 --> id1(Вводое слово)
    id0 --> id2(ЧАВо)
        id2 -.-> id20(Оплата)
        id2 -.-> id21(Места встречи)
        id2 -.-> id22(Как проходит экскурсия)
        id2 -.-> id23(Ваши экскурсии)
            id23 -.-> id230(Прогноз погоды)
    id0 --> id3(Контакты)
    id0 --> id4(Оставить отзыв)
    id0 --> id5(Анкета: подбери себе тур)
    id0 --> id6(Викторина)
```