import asyncio
import aiohttp

# №2 Асинхронный поиск IP
async def fetch_ip(session, name, url):
    try:
        async with session.get(url, timeout=5) as response:
            if response.status == 200:
                ip = await response.text()
                return name, ip.strip()
    except Exception:
        pass
    await asyncio.sleep(999) 

async def get_my_ip():
    services = {
        "ipify": "https://api.ipify.org",
        "ip-api": "http://ip-api.com/line/?fields=query",
        "seeip": "https://api.seeip.org"
    }
    
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_ip(session, name, url)) for name, url in services.items()]
        
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        
        for p in pending:
            p.cancel()
            
        if done:
            name, ip = done.pop().result()
            print(f"IP: {ip} (Ответил первым: {name})")

# №3 Эмуляция собеседований
async def interview_process(name, t1_prep, t1_def, t2_prep, t2_def):
    print(f"{name} started the 1 task.")
    await asyncio.sleep(t1_prep / 100)
    
    print(f"{name} moved on to the defense of the 1 task.")
    await asyncio.sleep(t1_def / 100)
    print(f"{name} completed the 1 task.")
    
    print(f"{name} is resting.")
    await asyncio.sleep(5 / 100)
    
    print(f"{name} started the 2 task.")
    await asyncio.sleep(t2_prep / 100)
    
    print(f"{name} moved on to the defense of the 2 task.")
    await asyncio.sleep(t2_def / 100)
    print(f"{name} completed the 2 task.")

async def interviews(*candidates):
    tasks = [interview_process(*c) for c in candidates]
    await asyncio.gather(*tasks)

# №4 Памятка агронома
async def apply_fertilizers(plant):
    print(f"7 Application of fertilizers for {plant}")
    await asyncio.sleep(3 / 1000)
    print(f"7 Fertilizers for the {plant} have been introduced")

async def treat_pests(plant):
    print(f"8 Treatment of {plant} from pests")
    await asyncio.sleep(5 / 1000)
    print(f"8 The {plant} is treated from pests")

async def process_plant(plant, t_soak, t_sprout, t_root):
    print(f"0 Beginning of sowing the {plant} plant")
    
    bg_tasks = asyncio.gather(apply_fertilizers(plant), treat_pests(plant))
    
    print(f"1 Soaking of the {plant} started")
    await asyncio.sleep(t_soak / 1000)
    print(f"2 Soaking of the {plant} is finished")
    
    print(f"3 Shelter of the {plant} is supplied")
    await asyncio.sleep(t_sprout / 1000)
    print(f"4 Shelter of the {plant} is removed")
    
    print(f"5 The {plant} has been transplanted")
    await asyncio.sleep(t_root / 1000)
    print(f"6 The {plant} has taken root")
    
    await bg_tasks
    print(f"9 The seedlings of the {plant} are ready")

async def sowing(*plants):
    tasks = [process_plant(*p) for p in plants]
    await asyncio.gather(*tasks)

async def main_block_1():
    print("--- Запуск Задачи 2 ---")
    await get_my_ip()
    
    print("\n--- Запуск Задачи 3 ---")
    await interviews(
        ("Alice", 10, 5, 12, 6),
        ("Bob", 8, 4, 15, 8)
    )
    
    print("\n--- Запуск Задачи 4 ---")
    await sowing(
        ("Tomato", 10, 20, 15),
        ("Cucumber", 8, 15, 10)
    )

if __name__ == "__main__":
    asyncio.run(main_block_1())