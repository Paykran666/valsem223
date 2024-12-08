import asyncio

async def progress_tracker(n):
    """
    Имитирует выполнение задачи и выводит прогресс каждые 0.5 секунды.
    """
    progress = 0
    increment = 100 // n # Размер шага прогресса

    while progress < 100:
        await asyncio.sleep(0.5)
        progress += increment
        if progress > 100: #корректировка, чтобы не превысить 100%
            progress = 100
        print(f"Выполнено {progress}%...")

    print("Выполнено 100%!")


async def main():
    await progress_tracker(10)

if __name__ == "__main__":
    asyncio.run(main())
