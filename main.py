import vk_api
import os
import re
from vk_api.longpoll import VkLongPoll, VkEventType
from user_base import *
from random import getrandbits

# init api and connection
TOKEN = os.environ["VKKEY"]
api = vk_api.VkApi(token=TOKEN)
lp = VkLongPoll(api)


def msg(userid, message):
    api.method('messages.send', {'user_id': userid, 'message': message, 'random_id': getrandbits(64)})


print("connected to vk.com\n///////////////////")
for event in lp.listen():
    # print(event.type)
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            user_text = event.text
            user_id = event.user_id
            if user_text == "!r":
                add_user(user_id, 0)
                msg(user_id, """You are registered!""")
                msg(user_id, "You can save only one data container\nSend me !put <string>\nThe default data is "
                             "0\n2400 chars is the max length\nBot won't work if you send very long message.\n"
                             "If you don't want to use bot anymore - you can clear your data by !d, it helps us.")
                continue
            if get_user(user_id).fetchone() is None:
                msg(user_id, """You are not registered\nSend !r for registration.""")

            if re.search(r'^!put .+$', user_text):
                data = re.search(r'\S+$', user_text).group()
                if len(data) <= 2400:
                    update_user(user_id, data)
                else:
                    msg(user_id, "Too long message (max is 2400 char)")
                    continue
                msg(user_id, """Your data container were changed.\nSend me !get to get this.""")
            if re.search(r'^!get$', user_text):
                result = get_user(user_id).fetchone().data
                msg(user_id, "Your data:")
                msg(user_id, result)
            if re.search(r'!d', user_text):
                delete_user()
                msg("You were deleted. !r for start again.")
