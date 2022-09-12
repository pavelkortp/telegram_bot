import asyncio
from utils.db_api.db_gino import db
from data import config
from utils.db_api import quick_commands as commands
# from utils.db_api import quick_commands as commands


async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(1, 'Pavlo')
    await commands.add_user(2, 'gee', 'someone')
    await commands.add_user(31, 'Pss')
    await commands.add_user(442, 'rrr')
    await commands.add_user(522, 'aaa')

    users = await commands.select_all_users()
    print(users)

    count = await commands.count_users()
    print(count)

    user = await commands.select_user(1)
    print(user)

    await commands.update_user_name(1, 'new name')

    user = await commands.select_user(1)
    print(user)

loop = asyncio.get_event_loop()
loop.run_until_complete(db_test)
