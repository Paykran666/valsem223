import asyncio

async def async_timer(seconds_list):
    """
    Асинхронно выводит сообщение "Прошло X секунд!" для каждого элемента списка
    с соответствующей задержкой.
    """
    for seconds in seconds_list:
        await asyncio.sleep(seconds) # Задержка на указанное количество секунд
        print(f"Прошло {seconds} секунд!")

async def main():
    await async_timer([1, 3, 2])

if __name__ == "__main__":
    asyncio.run(main())

