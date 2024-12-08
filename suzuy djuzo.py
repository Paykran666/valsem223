import asyncio

async def add_customers(queue):
    """Добавляет покупателей в очередь."""
    for i in range(1, 11):
        customer = f"Покупатель {i}"
        await queue.put(customer)
        print(f"Добавлен в очередь: {customer}")
        await asyncio.sleep(1)

async def serve_customers(queue):
    """Обслуживает покупателей из очереди."""
    while True:
        customer = await queue.get()
        print(f"Обслуживаю: {customer}")
        await asyncio.sleep(2)
        queue.task_done()
        if queue.empty():
            break

async def main():
    """Основная функция, запускающая добавление и обслуживание покупателей."""
    queue = asyncio.Queue()
    await asyncio.gather(
        add_customers(queue),
        serve_customers(queue)
    )
    await queue.join() # Дождаться завершения всех задач
    print("Все покупатели обслужены.")


if __name__ == "__main__":
    asyncio.run(main())
