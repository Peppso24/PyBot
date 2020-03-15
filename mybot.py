import telepot
from config import TOKEN
from pprint import pprint
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import sys, time


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    print(content_type, chat_type, chat_id)
    pprint(msg)    
    keyboard= InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Ho fame", callback_data='press')],
        [InlineKeyboardButton(text="Ho sete", callback_data='press')],
    ])

    bot.sendMessage(chat_id, "Usa i pulsanti!", reply_markup=keyboard) #oppure bot.sendMessage(chat_id, msg['text'])



def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print("CallbackQuery: ", query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text="YATHAAA")

bot= telepot.Bot(TOKEN)
def send_welcome(message):
    bot.reply_to(message, 'Welcome!')
bot.message_loop({'chat': on_chat_message, 'callback_query':on_callback_query})


