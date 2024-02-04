from random import choice,randint
def generate(lenth,alf):
    pas=''
    for i in range(lenth):
        pas=pas+choice(alf)
    return pas
def choosing(p):
    chars=' '
    j=0
    for i in alf.keys():
        if p[j]==1:
            chars=chars+alf[i]
        j+=1
    return chars
def give_item():
    prilag=items['prilag'][randint(0,len(items['prilag'])-1)]
    suhestv=items['suhestv'][randint(0,len(items['suhestv'])-1)]
    prilag2=items['prilag'][randint(0,len(items['prilag'])-1)]
    nar=items['nar'][randint(0,len(items['nar'])-1)]
    if randint(0,1)==1:
        return f"{prilag}{'_' if prilag2!='' else ''}{suhestv}_of{'_' if prilag2!='' else ''}{prilag2}_{nar}"
    else:
        return f"{prilag.title()}{suhestv.title()}Of{prilag2.title()}{nar.title()}"
def mail():
    mails=["gmail.com","mail.ru","yandex.ru","rambler.ru","yahoo.com"]
    for i in range(len(mails)):
        print(f"{i}:{mails[i]}",end="; ")
    return mails[int(input("\n>>"))]
alf={
    "letters low":"abcdefghijklmnopqrstuvwxyz",
    "letters up":"abcdefghijklmnopqrstuvwxyz".upper(),
    "simbols":"!@#$%^&*()-_=+[]}{:;',./<>?~`*"+'"',
    "nums":"1234567890"
}
items={
    "prilag":["","unbelievable","cool","wonderful","sexy"],
    "suhestv":["sas",],
    "nar":["pooring",]
}
print(f'Your email: {give_item()}@{mail()}')
print(f'Your password:{generate(int(input("Enter lenth>>")),choosing([int(input(f"Add {i}?>>")) for i in alf.keys()]))}')