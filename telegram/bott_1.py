import asyncio
import json
from aiogram import Bot , Dispatcher , executor , types
from parcer_2 import check_new_update_1


token = '6167770624:AAFsFS4fHZS6JsWYsa4Q86NGP2RSgJfsmXE'
# channel_id = '@ukrinfo123'
bot = Bot(token=token , parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def get_new_novosti_1():
    while True:
        fresh_new = check_new_update_1()

        if len(fresh_new) >=1:
            for k, v in sorted(fresh_new.items()):
                news = f'<b>{v["novost_title"]}</b>\n{v["novost_url"]}'
                await  bot.send_message(chat_id='612914425' , text=news , disable_notification=True)
                with open('new_dict_1.json' , 'r') as f:
                    new_dict = json.load(f)
                    new_dict[k] = v
                with open('new_dict_1.json' , 'w') as f:
                    json.dump(new_dict , f , indent=4 , ensure_ascii=False)

        await asyncio.sleep(30)
#
# async def schedule_task():
#     while True:
#         await get_new_novosti()
#         await asyncio.sleep(30)


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(get_new_novosti_1())
    executor.start_polling(dp , skip_updates=True)
        # executor.start_polling(dp)
        # executor.start_polling(dp , skip_updates=True)
if __name__=='__main__':
    main()