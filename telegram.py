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

"""def hello(func):
    print("hello")
    func()
    print("good")
@hello
def goodb():
    print("test")"""

if __name__=="__main__":
    bot.infinity_polling()