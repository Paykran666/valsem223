import asyncio
import random

async def process_task(queue):
    """Обрабатывает задачи из очереди."""
    while True:
        task = await queue.get()
        print(f"Обрабатываю: {task}")
        await asyncio.sleep(random.uniform(1, 2)) # Имитация выполнения задачи
        queue.task_done() # Сигнализирует о завершении задачи
        if queue.empty():
            break

async def main():
    """Создает очередь задач и запускает обработчики."""
    queue = asyncio.Queue()
    tasks = ["Задача 1", "Задача 2", "Задача 3", "Задача 4", "Задача 5"]
    for task in tasks:
        await queue.put(task)

    await asyncio.gather(process_task(queue), process_task(queue))
    await queue.join() # Ждет завершения всех задач в очереди
    print("Все задачи обработаны.")


if __name__ == "__main__":
    asyncio.run(main())
