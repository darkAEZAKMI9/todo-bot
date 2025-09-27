import aiosqlite

DB_NAME = "todo.db"

async def create_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                text TEXT,
                completed BOOLEAN DEFAULT FALSE
            )
        """)
        await db.commit()

async def add_task(user_id: int, text: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO tasks (user_id, text) VALUES (?, ?)",
            (user_id, text)
        )
        await db.commit()

async def get_tasks(user_id: int, completed: bool = False):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT id, text FROM tasks WHERE user_id = ? AND completed = ?",
            (user_id, completed)
        )
        return await cursor.fetchall()

async def delete_task(task_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        await db.commit()

async def complete_task(task_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE tasks SET completed = TRUE WHERE id = ?",
            (task_id,)
        )
        await db.commit()