from aiogram.types import ReplyKeyboardMarkup , InlineKeyboardMarkup , InlineKeyboardButton , KeyboardButton , ReplyKeyboardRemove

#Проверка все ли верно в вашем профиле!
vseverno = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Нет, Отредактировать",callback_data="net"),
            InlineKeyboardButton(text="Да, Все ок",callback_data="yes")
        ]
    ],
    resize_keyboard=True
)

#Изменения своих данных в профиле!
options = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Имя",callback_data="name")
        ],
        [
            InlineKeyboardButton(text="Фамилия",callback_data="surname")
                                
        ],
        [
            InlineKeyboardButton(text="Номер телефона",callback_data="number")
        ]
    ],
    resize_keyboard=True
)


#Обычные кнопки которые видны всегда 
mainkb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Инструкция 🧾"),
            KeyboardButton(text="Профиль 👤")
        ],
        [
            KeyboardButton(text="Поддержка ☎️"),
            KeyboardButton(text="Адреса 📬")
        ],
        [
            KeyboardButton(text="Калькулятор 📐")
        ]
    ],
    resize_keyboard=True
)

marketplaces = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Pindduoduo",callback_data="pd")
        ],
        [
            InlineKeyboardButton(text="Taobao",callback_data="to")
        ],
        [
            InlineKeyboardButton(text="1688",callback_data="18")
        ],
        [
            InlineKeyboardButton(text="Poizon",callback_data="pn")
        ]
    ],
    resize_keyboard=True
)


notkb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отмена 🙅‍♂️")
        ]
    ],
    resize_keyboard=True
)



photoyesorno = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да",callback_data="yesphoto")
        ],
        [
            InlineKeyboardButton(text="Нет",callback_data="nophoto")
                                
        ]
    ],
    resize_keyboard=True
)

buttonyesorno = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да",callback_data="yesbutton")
        ],
        [
            InlineKeyboardButton(text="Нет",callback_data="nobutton")
                                
        ]
    ],
    resize_keyboard=True
)

confirmationyesorno = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да",callback_data="yesconfirm")
        ],
        [
            InlineKeyboardButton(text="Нет",callback_data="noconfirm")
                                
        ]
    ],
    resize_keyboard=True
)