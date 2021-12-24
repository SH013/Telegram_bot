import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified
from aiogram.utils.callback_data import CallbackData
from random import randint
from contextlib import suppress
from main import bot, dp
from config import admin_id
from aiogram import types
import logging
import datetime 
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar
import psycopg2
from config import host, user, password, db_name

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name    
)
connection.autocommit = True

logging.basicConfig(level=logging.INFO)

user_data = {}
async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")

callback_numbers = CallbackData("fabnum", "action")

def get_keyboard_fab():
    buttons = [
        types.InlineKeyboardButton(text="-1", callback_data=callback_numbers.new(action="decr")),
        types.InlineKeyboardButton(text="+1", callback_data=callback_numbers.new(action="incr")),
        types.InlineKeyboardButton(text="Подтвердить", callback_data=callback_numbers.new(action="finish"))
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


    
start_kb = ReplyKeyboardMarkup(resize_keyboard=True,)
start_kb.row('Navigation Calendar', 'Dialog Calendar')


@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    await message.reply('Pick a calendar', reply_markup=start_kb)
    


@dp.message_handler(Text(equals=['Navigation Calendar'], ignore_case=True))
async def nav_cal_handler(message: Message):
    await message.answer("Please select a date: ", reply_markup=await SimpleCalendar().start_calendar())  

@dp.callback_query_handler(simple_cal_callback.filter())
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data )
    if selected:
        await callback_query.message.answer(
            f'You selected {date.strftime("%d/%m")}',
            reply_markup=start_kb
        )
        format = '%d/%m'
        a = datetime.datetime.strptime(date.strftime("%d/%m"), format)
        b = str(a)
        month_int = int(b[5:7])
        date_int = int(b[8:10]) 

        username = callback_query.from_user.username

        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO user1 (user_name, date_of_birth) VALUES
                (  %s, %s );""", (  f'{username}' , f'{a}', )
            )    
            
       
        if 20<=date_int and month_int ==1 or date_int<=19 and month_int==2:
            await callback_query.message.answer(f'Aquaris',
            reply_markup=start_kb)
        elif 20<=date_int and month_int ==2 or date_int<=20 and month_int==3:
            await callback_query.message.answer(f'Pisces',
            reply_markup=start_kb)
        elif 21<=date_int and month_int ==3 or date_int<=19 and month_int==4:
            await callback_query.message.answer(f'Aries',
            reply_markup=start_kb)
        elif 20<=date_int and month_int ==4 or date_int<=20 and month_int==5:
            await callback_query.message.answer(f'"Taurus"',
            reply_markup=start_kb)
        elif 21<=date_int and month_int ==5 or date_int<=20 and month_int==6:
            await callback_query.message.answer(f"Gemini",
            reply_markup=start_kb)
        elif 21<=date_int and month_int ==6 or date_int<=22 and month_int==7:
            await callback_query.message.answer(f"Cancer",
            reply_markup=start_kb)
        elif 21<=date_int and month_int ==7 or date_int<=20 and month_int==8:
            await callback_query.message.answer(f"Gemini",
            reply_markup=start_kb)
        elif 21<=date_int and month_int ==8 or date_int<=22 and month_int==9:
            await callback_query.message.answer(f"Leo",
            reply_markup=start_kb)
        elif 23<=date_int and month_int ==9 or date_int<=23 and month_int==10:
            await callback_query.message.answer(f"Virgo",
            reply_markup=start_kb)
        elif 24<=date_int and month_int ==10 or date_int<=22 and month_int==11:
            await callback_query.message.answer(f"Scorpio",
            reply_markup=start_kb)
        elif 23<=date_int and month_int ==11 or date_int<=20 and month_int==12:
            await callback_query.message.answer(f"Sagittarius",
            reply_markup=start_kb)
        elif 21<=date_int and month_int ==12 or date_int<=19 and month_int==1:
            await callback_query.message.answer(f"Capricorn",
            reply_markup=start_kb)
            

        

@dp.message_handler(Text(equals=['Dialog Calendar'], ignore_case=True))
async def simple_cal_handler(message: Message):
    await message.answer("Please select a date: ", reply_markup=await DialogCalendar().start_calendar())


@dp.callback_query_handler(dialog_cal_callback.filter())
async def process_dialog_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, date = await DialogCalendar().process_selection(callback_query, callback_data)
    if selected :
        await callback_query.message.answer(
            f'You selected {date.strftime("%d/%m")}',
            reply_markup=start_kb
        )
        format = '%d/%m'
        a = datetime.datetime.strptime(date.strftime("%d/%m"), format)
        b = str(a)
        month_int = int(b[5:7])
        date_int = int(b[8:10])
        username = callback_query.from_user.full_name

        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO user1 (user_name, date_of_birth) VALUES
                (  %s, %s );""", (  f'{username}' , f'{a}', )
            )    

        if 20<=date_int and month_int ==1 or date_int<=19 and month_int==2:
            await callback_query.message.answer(f'Aquaris',
            reply_markup=start_kb)
        elif 20<=date_int and month_int ==2 or date_int<=20 and month_int==3:
            await callback_query.message.answer(f'Pisces',
            reply_markup=start_kb)
        elif 21<=date_int and month_int ==3 or date_int<=19 and month_int==4:
            await callback_query.message.answer(f'Aries',
            reply_markup=start_kb)
        elif 20<=date_int and month_int ==4 or date_int<=20 and month_int==5:
            await callback_query.message.answer(f'"Taurus"',
            reply_markup=start_kb)
        elif 21<=date_int and month_int ==5 or date_int<=20 and month_int==6:
            await callback_query.message.answer(f"Gemini",
            reply_markup=start_kb)
        elif 21<=date_int and month_int ==6 or date_int<=22 and month_int==7:
            await callback_query.message.answer(f"Cancer",
            reply_markup=start_kb)
        elif 21<=date_int and month_int ==7 or date_int<=20 and month_int==8:
            await callback_query.message.answer(f"Gemini",
            reply_markup=start_kb)
        elif 21<=date_int and month_int ==8 or date_int<=22 and month_int==9:
            await callback_query.message.answer(f"Leo",
            reply_markup=start_kb)
        elif 23<=date_int and month_int ==9 or date_int<=23 and month_int==10:
            await callback_query.message.answer(f"Virgo",
            reply_markup=start_kb)
        elif 24<=date_int and month_int ==10 or date_int<=22 and month_int==11:
            await callback_query.message.answer(f"Scorpio",
            reply_markup=start_kb)
        elif 23<=date_int and month_int ==11 or date_int<=20 and month_int==12:
            await callback_query.message.answer(f"Sagittarius",
            reply_markup=start_kb)
        elif 21<=date_int and month_int ==12 or date_int<=19 and month_int==1:
            await callback_query.message.answer(f"Capricorn",
            reply_markup=start_kb)
            