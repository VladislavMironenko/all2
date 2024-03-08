import asyncio
import json
from aiogram import Bot , Dispatcher , executor , types
from parcer import check_new_update
from parcer_2 import check_new_update_1


token = '6167770624:AAFsFS4fHZS6JsWYsa4Q86NGP2RSgJfsmXE'
channel_id = '@ukrinfo1'
bot = Bot(token=token , parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# @dp.message_handler(commands='start')
# async def start(message:  types.Message):
#     start_buttons = ['Последние 5 новостей']
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(*start_buttons)
#     await message.answer('Лента новостей' , reply_markup=keyboard)


# @dp.message_handler(Text(equals='Последние 5 новостей'))
# async def get_last_five(message: types.Message):
#     with open('new_dict.json' ) as file:
#         new_dict = json.load(file)
#         last_five = list(new_dict.items())[0:5]
#
#     for k , v in last_five:
#         news = f'{v["novost_title"]}\n{v["novost_url"]}'
#         await  message.answer(news)


async def get_new_novosti():
    while True:
        fresh_new = check_new_update()

        if len(fresh_new) >=1:
            for k, v in sorted(fresh_new.items()):
                news = f'<b>{v["novost_title"]}</b>\n{v["novost_url"]}'
                # await  bot.send_message(chat_id='612914425' , text=news , disable_notification=True)
                await bot.send_message(chat_id=channel_id , text=news , disable_notification=True)
                with open('new_dict.json' , 'r') as f:
                    new_dict = json.load(f)
                    new_dict[k] = v
                with open('new_dict.json' , 'w') as f:
                    json.dump(new_dict , f , indent=4 , ensure_ascii=False)

        await asyncio.sleep(90)

async def get_new_novosti_1():
    while True:
        fresh_new = check_new_update_1()

        if len(fresh_new) >=1:
            for k, v in sorted(fresh_new.items()):
                news = f'<b>{v["novost_title"]}</b>\n{v["novost_url"]}'
                # await  bot.send_message(chat_id='612914425' , text=news , disable_notification=True)
                await bot.send_message(chat_id=channel_id , text=news , disable_notification=True)
                with open('new_dict_1.json' , 'r') as f:
                    new_dict = json.load(f)
                    new_dict[k] = v
                with open('new_dict_1.json' , 'w') as f:
                    json.dump(new_dict , f , indent=4 , ensure_ascii=False)

        await asyncio.sleep(30)

def main():
    loop = asyncio.get_event_loop()
    loop.create_task(get_new_novosti())
    loop.create_task(get_new_novosti_1())
    executor.start_polling(dp , skip_updates=True)
        # executor.start_polling(dp)
        # executor.start_polling(dp , skip_updates=True)
if __name__=='__main__':
    asyncio.run(main())


