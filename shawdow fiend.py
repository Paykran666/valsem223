import asyncio


async def producer(producer_id, data_queue, num_data):
    """Производитель данных."""
    for i in range(1, num_data + 1):
        await asyncio.sleep(1)
        data = i
        await data_queue.put((producer_id, data))
        print(f"Производитель {producer_id}: сгенерировал {data}")


async def worker(data_queue, results_queue):
    """Работник, обрабатывающий данные."""
    while True:
        producer_id, data = await data_queue.get()
        await asyncio.sleep(1.5)  # Имитация обработки
        result = data * 2
        await results_queue.put(result)
        print(f"Работник: обработал {data} -> {result}")
        data_queue.task_done()
        if data_queue.empty():
            break


async def storage(results_queue):
    """Хранилище результатов."""
    saved_data = []
    while True:
        await asyncio.sleep(2)
        while not results_queue.empty():
            result = await results_queue.get()
            saved_data.append(result)
            results_queue.task_done()
        print(f"Сохранено: {saved_data}")
        if results_queue.empty() and all(q.empty() for q in [results_queue]):  # проверка всех очередей
            break


async def main():
    """Основная функция."""
    data_queue = asyncio.Queue()
    results_queue = asyncio.Queue()
    num_data = 10

    producers = [producer(i, data_queue, num_data) for i in range(1, 4)]
    workers = [worker(data_queue, results_queue) for _ in range(2)]

    await asyncio.gather(*producers, *workers, storage(results_queue))
    await data_queue.join()
    await results_queue.join()
    print("Система завершила работу.")


if __name__ == "__main__":
    asyncio.run(main())

