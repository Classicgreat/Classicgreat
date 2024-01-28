import telebot
import requests

token=""

bot=telebot.TeleBot(token)

def getinfo(ip:str)->dict:
    url=f"https://ipinfo.io/{ip}/geo"
    r=requests.get(url).json()
    b=""
    for i in r:
        if i!="readme":b=b+str(i)+" "+str(r[i])+"\n"
    return b

@bot.message_handler(commands=["start"])
def start(message):
    #print(message)
    msg=bot.send_message(message.chat.id,"hello")
    #bot.reply_to(message,"Сверху лох")
    bot.register_next_step_handler(msg, getip)

def getip(message):
    ip=message.text
    info=getinfo(ip)
    bot.send_message(message.chat.id, info)

def generator_keyboards(ListNameBTN,NumberColumns=2):
    keyboards=telebot.types.ReplyKeyboardMarkup(row_width=NumberColumns,resize_keyboard=True)
    btn_names=[telebot.types.KeyboardButton(text=x) for x in ListNameBTN]
    keyboards.add(*btn_names)
    return keyboards

if __name__=="__main__":
    bot.infinity_polling()