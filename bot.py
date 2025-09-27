import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config import TOKEN, create_bot
from database import *
from keyboards import *
from states import AddTask

bot = Bot(token=TOKEN, default=create_bot())
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🚀 Добро пожаловать в To-Do бот!\n"
        "Используйте кнопки ниже для управления задачами.",
        reply_markup=main_kb
    )

@dp.message(lambda message: message.text == "📝 Добавить задачу")
async def add_task_handler(message: types.Message, state: FSMContext):
    await message.answer(
        "Введите текст задачи:",
        reply_markup=cancel_kb
    )
    await state.set_state(AddTask.waiting_for_text)

@dp.message(AddTask.waiting_for_text)
async def process_task_text(message: types.Message, state: FSMContext):
    if message.text == "❌ Отменить":
        await message.answer("Действие отменено", reply_markup=main_kb)
        await state.clear()
        return
    
    await add_task(message.from_user.id, message.text)
    await message.answer("✅ Задача добавлена!", reply_markup=main_kb)
    await state.clear()

@dp.message(lambda message: message.text == "📋 Список задач")
async def show_tasks(message: types.Message):
    tasks = await get_tasks(message.from_user.id, completed=False)
    if not tasks:
        await message.answer("📭 Нет активных задач")
        return
    
    kb = tasks_kb(tasks, "complete")
    await message.answer("Активные задачи:", reply_markup=kb)

@dp.message(lambda message: message.text == "✅ Выполненные")
async def show_completed_tasks(message: types.Message):
    tasks = await get_tasks(message.from_user.id, completed=True)
    if not tasks:
        await message.answer("📭 Нет выполненных задач")
        return
    
    text = "✅ Выполненные задачи:\n\n"
    for task_id, task_text in tasks:
        text += f"• {task_text}\n"
    
    await message.answer(text)

@dp.callback_query(lambda call: call.data.startswith("complete_"))
async def complete_task_handler(callback: types.CallbackQuery):
    task_id = int(callback.data.split("_")[1])
    await complete_task(task_id)
    await callback.message.edit_text("✅ Задача выполнена!")
    await callback.answer()

@dp.message(lambda message: message.text == "❌ Удалить задачу")
async def delete_task_handler(message: types.Message):
    tasks = await get_tasks(message.from_user.id, completed=False)
    if not tasks:
        await message.answer("📭 Нет задач для удаления")
        return
    
    kb = tasks_kb(tasks, "delete")
    await message.answer("Выберите задачу для удаления:", reply_markup=kb)

@dp.callback_query(lambda call: call.data.startswith("delete_"))
async def delete_task_callback(callback: types.CallbackQuery):
    task_id = int(callback.data.split("_")[1])
    await delete_task(task_id)
    await callback.message.edit_text("❌ Задача удалена!")
    await callback.answer()

@dp.callback_query(lambda call: call.data == "cancel")
async def cancel_callback_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Действие отменено")
    await state.clear()
    await callback.answer()

async def main():
    await create_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())