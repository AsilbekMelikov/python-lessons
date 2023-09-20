# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 14:33:42 2023

@author: User
"""

#ismlar=("asilbek","behruz","sardor","yashnarbek")
#for ism in ismlar:
    #if ism=="asilbek":
   #     print(ism.upper())
  #  else:
 #       print(ism.lower())
 
#ism = input("Ismingiz nima? \n>>> ")  
#if ism.lower()!= "ali":
 #   print(f"I am so sorry {ism.title()}. We are waiting for Ali")
#else:
    #print(f"Hello {ism.title()} How are you?")
    
    
#yosh = int(input("How old are you?\n>>> "))
#if yosh>=18:
#    print(" Welcome to our website!")
#else:
 #   print("Get the hell out of here, it is not your place,  ")
 
 
#login = input("Insert your new login code>>> ")
#if len(login)<=4:
 #   print("Please, choose a new login more than 4 letters or numbers")
#else:
#    print("Congratulations, your login has been successfully confirmed")
 


#login= input("What is your login?\n>>> ")
#if login.lower()=="admin":
 #   print(f"Welcome,{login}. Do you want to see a list of users? ")
#else:
 #   print(f"Welcome,{login.title()} ")
 
#son = float(input("Istalgan sonni kiriting? >>> "))
#print(son**(1/2)) if son>=0 else print("Musbat son kiriting ")


#kun =int( input("Hafta kunlarini tartib raqamini kiriting>>> "))
#if kun>=8 or kun==0:
#    print(("Buncha kun yo'q bir haftada\n Iltimos boshqatttadan kiriting>>> "))
#else:   
 #if kun==1:
 #   print("Dushanba")
 #elif kun==2:
 #   print("Seshanba")
# elif kun==3:
 #   print("Chorshanba")
 #elif kun==4:
 #   print("Payshanba")
 #elif kun==5:
 #   print("JUMA")
# elif kun==6:
 #   print("Shanba")
# else:
#    print("Yakshanba")
            
 
 
#narx = 15000
#choy=0
#salad=1
#non=1
#if choy:
#    narx=narx+5000
#if salad:
#    narx=narx+5000
#if non:
 #   narx=narx+3000
#else:
 #   narx=narx
#print(f"Jami {narx} so'm bo'ldi")

#menu = ["manti","osh","shashlik","somsa","besh barmoq"]
#ovqat=input("Nima ovqat yeysiz?>>> ")
#if ovqat.lower() in menu:
 #   print("Buyurtmangiz qabul qilindi!")
#else:
 #   print('Afsuski bunday ovqat yo\'q')
  
 
    
 
#menu=["osh","qozonkabob","shashlik","norin","somsa"]
#buyurtmalar=["manti"]
#if buyurtmalar:
 #for taom in buyurtmalar:
    #if taom in menu:
    #    print(f"menuda {taom} bor")
   # else:
  #      print(f"Kechirasiz {taom} yo'q")
#else:
 #   print("Ro'yxat bo'sh")
 
 
# print("Ikkita ixtiyoriy son kiriting>>> ")
#a=float(input("a="))
#b=float(input("b="))
#if a==b:
 #   print(f"{a}={b}")
#elif a>b:
#    print(f"{a}>{b}" )
#else:
#    print(f"{a}<{b}" )
 

#mahsulotlar=["tuxum","cola","pepsi","flash","non","tarvuz","qovun","pomidor",
#             "bodring","banan"]
#yangi_savat=[]
#for n in range(5):
 #   yangi_savat.append(input(f"{n+1}-mahsulotni kiriting>>> "))
#print(yangi_savat)
#if yangi_savat:
 #for mahsulot in yangi_savat:
  # if mahsulot in mahsulotlar:
   #   print(f"{mahsulot} do'konimizda bor")
   #else:
   #   print(f"{mahsulot} do'konimizda yo'q")
#else:
 #print("Iltimos savatingizni to'ldiring")    
    
    
   
#mahsulotlar=["tuxum","cola","pepsi","flash","non","tarvuz","qovun","pomidor",
                # "bodring","banan"]  
#savat=[]
#for n in range(5):
 #  savat.append(input(f"{n+1}-mahsulotni kiriting>>> "))

#bor_mahsulotlar= []
#mavjud_emas= []
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
 #       bor_mahsulotlar.append(mahsulot)
 #   else:
 #       mavjud_emas.append(mahsulot)
#print("Bor mahsulotlar", bor_mahsulotlar)
#print("Yo'q mahsulotlar", mavjud_emas)
#if bor_mahsulotlar:
#    print("Quyidagi mahsulotlar do'konimizda bor>>> ")
#    for mahsulot in bor_mahsulotlar:
#        print(mahsulot)
#else:
 #   print("Do'konimizda siz izlayotgan mahsulotlar afsuski qolmagan")
#if mavjud_emas:
 #  print("Quyidagi mahsulotlar do'konimizda yo'q:")
  # for mahsulot in mavjud_emas:
   #   print(mahsulot)
#else:
 #   print("Barcha mahsulotlarimiz do'konda bor")
    
    

#print("5 ta son kiriting")
#son=[]     
#for n in range(5):
 #   son.append(input(f"{n+1}-sonni kiriting>>> "))
#print(sum(son))
#print(len(son))


#foydalanuvchilar=["asilbek","behruz","laziz","asliddin","sardor"]
#login=input("Websitega kirish uchun login tanlang>>> ")
#if login.lower() in foydalanuvchilar:
 #   print("Yana bir marta urinib ko'ring chunki bu login band")
#else:
    #print(f"Xush kelibsiz websitega {login.title()}")
    
    
#son=int(input("Xohlagan bitta butun son kiriting>>> "))
#for n in range(2,100):
   # if not son%(n):
   #   print(f"shu son {n} ga qoldiqsiz bo'linadi")
   
   

    
import numpy as np   
print("a va b ga son kiriting")   
a=int(input("a="))
b=int(input("b="))
son=list(range(a,b+1))
print(son)
takrorlanish=list(np.repeat(son,a))
print(takrorlanish)














 