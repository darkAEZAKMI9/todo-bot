from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Добавить задачу"), KeyboardButton(text="📋 Список задач")],
        [KeyboardButton(text="✅ Выполненные"), KeyboardButton(text="❌ Удалить задачу")]
    ],
    resize_keyboard=True
)

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="❌ Отменить")]],
    resize_keyboard=True
)

def tasks_kb(tasks: list, prefix: str):
    buttons = []
    for task_id, text in tasks:
        buttons.append([InlineKeyboardButton(
            text=text[:50] + "..." if len(text) > 50 else text, 
            callback_data=f"{prefix}_{task_id}"
        )])

    buttons.append([InlineKeyboardButton(text="❌ Отменить", callback_data="cancel")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)