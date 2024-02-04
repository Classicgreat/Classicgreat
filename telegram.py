import telebot
from telebot import types
from password import give_item
#import requests

token=""

bot=telebot.TeleBot(token)

def generator_keyboards(ListNameBTN,NumberColumns=2):
    keyboards=telebot.types.ReplyKeyboardMarkup(row_width=NumberColumns,resize_keyboard=True)
    btn_names=[telebot.types.KeyboardButton(text=x) for x in ListNameBTN]
    keyboards.add(*btn_names)
    return keyboards

def gettext(message):
    print(message.text)
"""def getinfo(ip:str)->dict:
    url=f"https://ipinfo.io/{ip}/geo"
    r=requests.get(url).json()
    b=""
    for i in r:
        if i!="readme":b=b+str(i)+" "+str(r[i])+"\n"
    return b
def getip(message):
    ip=message.text
    info=getinfo(ip)
    bot.send_message(message.chat.id, info)"""

@bot.message_handler(commands=["start"])
def start(message):
    keyboard=types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("+ Play",callback_data="play"))
    bot.send_message(message.chat.id, f"hello, {message.from_user.first_name}",reply_markup=keyboard)
    #print(message)
    #msg=bot.send_message(message.chat.id,"hello",reply_markup=generator_keyboards(["meny","exit"]))
    #bot.reply_to(message,"Сверху лох")
    #bot.register_next_step_handler(msg, getip)

@bot.message_handler(func=lambda m:m.text)
def text(message):
    text=message.text
    if text=="meny":
        bot.send_message(message.chat.id, "ses")
    elif text=="exit":
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=GFq6wH5JR2A")
    elif text=="sas":
        bot.send_message(message.chat.id, "good")

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data=="play":
        markup=types.InlineKeyboardMarkup()
        btn1=types.InlineKeyboardButton("- Stop",callback_data="stop")
        btn2=types.InlineKeyboardButton("-___-",callback_data="smile")
        btn3=types.InlineKeyboardButton("Text",callback_data="text")
        btn4=types.InlineKeyboardButton("Email",callback_data="email")
        markup.add(btn1,btn2,btn3,btn4)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup)
    elif call.data=="stop":
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("+ Play",callback_data="play"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="CLASSIC",reply_markup=markup)
    elif call.data=="smile":
       bot.send_message(call.message.chat.id, ":)")
       #bot.send_message(call.message.chat.id, "https://catherineasquithgallery.com/uploads/posts/2021-03/1614612233_137-p-fon-dlya-fotoshopa-priroda-209.jpg")
    elif call.data=="text":
        msg=bot.send_message(call.message.chat.id,"Enter Text:")
        bot.register_next_step_handler(msg, gettext)
    elif call.data=="email":
        bot.send_message(call.message.chat.id, f"Your email generated: {give_item()}@your_mail.com")
if __name__=="__main__":
    bot.infinity_polling()