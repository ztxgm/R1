import asyncio
import random
import json
import aiohttp
from datetime import datetime
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, URLInputFile

BOT_TOKEN = "6628638875:AAHWKt84Qu7wrPEEBcauEIh425jODdsUND8-Ws"
YANDEX_GEO_API = "d162c674-78aa-4664-9a19-9bd743c08fa1"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

# №6: /time и /date
@router.message(Command("time"))
async def cmd_time(message: Message):
    await message.answer(f"Текущее время: {datetime.now().strftime('%H:%M:%S')}")

@router.message(Command("date"))
async def cmd_date(message: Message):
    await message.answer(f"Текущая дата: {datetime.now().strftime('%Y-%m-%d')}")

# №7: Настольные игры (Кубики и Таймер)
main_board_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="/dice"), KeyboardButton(text="/timer")]
], resize_keyboard=True)

dice_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="1d6"), KeyboardButton(text="2d6")],
    [KeyboardButton(text="1d20"), KeyboardButton(text="Назад")]
], resize_keyboard=True)

timer_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="30 секунд"), KeyboardButton(text="1 минута")],
    [KeyboardButton(text="5 минут"), KeyboardButton(text="Назад")]
], resize_keyboard=True)

close_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/close")]], resize_keyboard=True)

active_timers = {}

@router.message(Command("start_board"))
async def cmd_start_board(message: Message):
    await message.answer("Выбери инструмент:", reply_markup=main_board_kb)

@router.message(Command("dice"))
async def cmd_dice(message: Message):
    await message.answer("Выбери кубик:", reply_markup=dice_kb)

@router.message(F.text.in_({"1d6", "2d6", "1d20"}))
async def roll_dice(message: Message):
    if message.text == "1d6":
        await message.answer(str(random.randint(1, 6)))
    elif message.text == "2d6":
        await message.answer(f"{random.randint(1, 6)}, {random.randint(1, 6)}")
    elif message.text == "1d20":
        await message.answer(str(random.randint(1, 20)))

@router.message(Command("timer"))
async def cmd_timer(message: Message):
    await message.answer("Выбери время:", reply_markup=timer_kb)

async def run_timer(user_id: int, chat_id: int, wait_time: int, text: str):
    try:
        await asyncio.sleep(wait_time)
        await bot.send_message(chat_id, f"{text} истекло", reply_markup=main_board_kb)
    except asyncio.CancelledError:
        pass # Таймер был отменен
    finally:
        active_timers.pop(user_id, None)

@router.message(F.text.in_({"30 секунд", "1 минута", "5 минут"}))
async def set_timer(message: Message):
    times = {"30 секунд": 30, "1 минута": 60, "5 минут": 300}
    t = times[message.text]
    
    if message.from_user.id in active_timers:
        active_timers[message.from_user.id].cancel()
        
    await message.answer(f"засек {message.text}", reply_markup=close_kb)
    task = asyncio.create_task(run_timer(message.from_user.id, message.chat.id, t, message.text))
    active_timers[message.from_user.id] = task

@router.message(Command("close"))
async def cmd_close(message: Message):
    if message.from_user.id in active_timers:
        active_timers[message.from_user.id].cancel()
        await message.answer("Таймер сброшен.", reply_markup=main_board_kb)

@router.message(F.text == "Назад")
async def back_to_main(message: Message):
    await message.answer("Главное меню:", reply_markup=main_board_kb)

# №8: Музей (Диаграмма состояний)
class Museum(StatesGroup):
    ENTRANCE = State()
    HALL_1 = State()
    HALL_2 = State()
    HALL_3 = State()
    HALL_4 = State()
    EXIT = State()

def make_room_kb(*rooms):
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=r)] for r in rooms], resize_keyboard=True)

@router.message(Command("museum"))
async def enter_museum(message: Message, state: FSMContext):
    await state.set_state(Museum.ENTRANCE)
    await message.answer("Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!", 
                         reply_markup=make_room_kb("Зал 1 (Античность)"))

@router.message(Museum.ENTRANCE, F.text.startswith("Зал 1"))
async def go_hall1(message: Message, state: FSMContext):
    await state.set_state(Museum.HALL_1)
    await message.answer("В данном зале представлено: Античное искусство.\nКуда пойдем дальше?", 
                         reply_markup=make_room_kb("Зал 2 (Средневековье)", "Зал 3 (Возрождение)", "Выход"))

@router.message(Museum.HALL_1, F.text == "Выход")
async def go_exit(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Всего доброго, не забудьте забрать верхнюю одежду в гардеробе!")

# №9: Квиз из JSON
class Quiz(StatesGroup):
    ACTIVE = State()

@router.message(Command("quiz"))
async def start_quiz(message: Message, state: FSMContext):
    try:
        with open("questions.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return await message.answer("Файл с вопросами не найден!")
        
    selected = random.sample(data, min(10, len(data)))
    await state.set_state(Quiz.ACTIVE)
    await state.update_data(questions=selected, current=0, score=0)
    
    await message.answer(f"Вопрос 1: {selected[0]['question']}\n(Для отмены введите /stop_quiz)")

@router.message(Command("stop_quiz"), StateFilter(Quiz.ACTIVE))
async def stop_quiz(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Тест прерван.")

@router.message(StateFilter(Quiz.ACTIVE))
async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    q_list = data["questions"]
    curr_idx = data["current"]
    score = data["score"]
    
    # Проверка ответа
    correct_ans = q_list[curr_idx]["answer"].strip().lower()
    if message.text.strip().lower() == correct_ans:
        score += 1
        
    curr_idx += 1
    
    if curr_idx < len(q_list):
        await state.update_data(current=curr_idx, score=score)
        await message.answer(f"Вопрос {curr_idx + 1}: {q_list[curr_idx]['question']}")
    else:
        await state.clear()
        await message.answer(f"Опрос завершен! Правильных ответов: {score} из {len(q_list)}.\nЧтобы пройти снова: /quiz")

# №10: Геокодер с картой
@router.message(Command("geo"))
async def cmd_geo(message: Message):
    await message.answer("Введите адрес для поиска (например: /map Москва, Красная площадь):")

@router.message(Command("map"))
async def get_map(message: Message):
    query = message.text.replace("/map", "").strip()
    if not query:
        return await message.answer("Укажите адрес.")
        
    geocode_url = f"https://geocode-maps.yandex.ru/1.x/?apikey={YANDEX_GEO_API}&geocode={query}&format=json"
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(geocode_url) as resp:
                if resp.status != 200:
                    return await message.answer(f"Ошибка HTTP: {resp.status}")
                
                data = await resp.json()
                features = data.get("response", {}).get("GeoObjectCollection", {}).get("featureMember", [])
                
                if not features:
                    return await message.answer("Ничего не найдено по этому запросу.")
                    
                coords = features[0]["GeoObject"]["Point"]["pos"]
                lon, lat = coords.split(" ")
                
                static_url = f"https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&z=14&l=map&pt={lon},{lat},pm2rdm"
                
                image = URLInputFile(static_url)
                await message.answer_photo(photo=image, caption=f"Вот ваш объект: {query}")
                
        except Exception as e:
            await message.answer(f"Произошла ошибка сети: {e}")

# №11: Бот-переводчик
from deep_translator import GoogleTranslator

class TranslatorState(StatesGroup):
    active = State()

def get_trans_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="RU -> EN", callback_data="dir_ru_en")],
        [InlineKeyboardButton(text="EN -> RU", callback_data="dir_en_ru")]
    ])

@router.message(Command("translate"))
async def cmd_translate(message: Message, state: FSMContext):
    await state.set_state(TranslatorState.active)
    await state.update_data(direction="ru-en")
    await message.answer("Режим перевода включен. Выберите направление:", reply_markup=get_trans_kb())

@router.callback_query(F.data.startswith("dir_"), StateFilter(TranslatorState.active))
async def change_trans_direction(call: aiogram.types.CallbackQuery, state: FSMContext):
    dir_code = call.data.replace("dir_", "")
    await state.update_data(direction=dir_code.replace("_", "-"))
    await call.message.edit_text(f"Направление изменено на {dir_code.upper()}", reply_markup=get_trans_kb())

@router.message(StateFilter(TranslatorState.active))
async def do_translation(message: Message, state: FSMContext):
    data = await state.get_data()
    src, dest = data["direction"].split("-")
    
    try:
        translated = GoogleTranslator(source=src, target=dest).translate(message.text)
        await message.answer(f"🔤 Перевод:\n{translated}")
    except Exception as e:
        await message.answer("Произошла ошибка при переводе.")

# №5: ЭХО-БОТ (Ставится в самом конце)
@router.message()
async def echo_bot(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(f"Я получил сообщение {message.text}")


# --- ЗАПУСК БОТА ---
async def main_bot():
    dp.include_router(router)
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main_bot())