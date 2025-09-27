# Telegram To-Do Bot 📝

[English](#english) | [Русский](#русский)

---

## English

### Description
A simple and efficient Telegram bot for managing your tasks and to-do lists. Built with Python using the aiogram library and SQLite database for data persistence.

### Features
- ✅ Add new tasks
- 📋 View active tasks
- ✅ Mark tasks as completed
- ❌ Delete unwanted tasks
- 📊 View completed tasks history
- 🔄 Cancel operations at any time
- 💾 Persistent data storage with SQLite

### Requirements
- Python 3.8+
- aiogram 3.x
- aiosqlite

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd telegram-todo-bot
   ```

2. **Install dependencies:**
   ```bash
   pip install aiogram aiosqlite
   ```

3. **Set up your bot token:**
   - Create a new bot via [@BotFather](https://t.me/botfather) on Telegram
   - Get your bot token
   - Set the environment variable:
     ```bash
     export BOT_TOKEN="your_bot_token_here"
     ```
   - Or modify the `TOKEN` variable in `config.py`

4. **Run the bot:**
   ```bash
   python bot.py
   ```

### Usage

Start a conversation with your bot and use the following commands:

- **📝 Add Task** - Create a new task
- **📋 Task List** - View all active tasks
- **✅ Completed** - View completed tasks
- **❌ Delete Task** - Remove a task from your list

### File Structure

```
telegram-todo-bot/
├── bot.py          # Main bot logic and handlers
├── config.py       # Configuration settings
├── database.py     # Database operations
├── keyboards.py    # Telegram keyboard layouts
├── states.py       # FSM states for user interactions
└── README.md       # This file
```

### Database 

The bot uses SQLite database with the following table structure:

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    text TEXT,
    completed BOOLEAN DEFAULT FALSE
);
```

---

## Русский

### Описание
Простой и эффективный Telegram-бот для управления задачами и списками дел. Создан на Python с использованием библиотеки aiogram и базы данных SQLite для хранения данных.

### Возможности
- ✅ Добавление новых задач
- 📋 Просмотр активных задач
- ✅ Отметка задач как выполненных
- ❌ Удаление ненужных задач
- 📊 Просмотр истории выполненных задач
- 🔄 Отмена операций в любое время
- 💾 Постоянное хранение данных с SQLite

### Требования
- Python 3.8+
- aiogram 3.x
- aiosqlite

### Установка

1. **Клонирование репозитория:**
   ```bash
   git clone <url-вашего-репозитория>
   cd telegram-todo-bot
   ```

2. **Установка зависимостей:**
   ```bash
   pip install aiogram aiosqlite
   ```

3. **Настройка токена бота:**
   - Создайте нового бота через [@BotFather](https://t.me/botfather) в Telegram
   - Получите токен вашего бота
   - Установите переменную окружения:
     ```bash
     export BOT_TOKEN="ваш_токен_бота"
     ```
   - Или измените переменную `TOKEN` в файле `config.py`

4. **Запуск бота:**
   ```bash
   python bot.py
   ```

### Использование

Начните разговор с вашим ботом и используйте следующие команды:

- **📝 Добавить задачу** - Создать новую задачу
- **📋 Список задач** - Просмотр всех активных задач
- **✅ Выполненные** - Просмотр выполненных задач
- **❌ Удалить задачу** - Удалить задачу из списка

### Структура файлов

```
telegram-todo-bot/
├── bot.py          # Основная логика бота и обработчики
├── config.py       # Настройки конфигурации
├── database.py     # Операции с базой данных
├── keyboards.py    # Раскладки клавиатур Telegram
├── states.py       # Состояния FSM для взаимодействия с пользователем
└── README.md       # Этот файл
```

### Схема базы данных

Бот использует базу данных SQLite со следующей структурой таблицы:

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    text TEXT,
    completed BOOLEAN DEFAULT FALSE
);
```