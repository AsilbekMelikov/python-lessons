# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 14:08:05 2023

@author: User
"""
#t_shaxslar= [ " Imom Buxoriy", " Amir Temur", " Imom Termiziy"]
#z_shaxslar = [ " Bill Gates", " Stive Jobs", " Mark Zuckerberg"]
#print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
#zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
#suhbat qilishni istar edim\n")
friends = []
friends.append("Asilbek")
friends.append("Yashnarbek")
friends.append("Zarnigor")
friends.append("Nilufar")
friends.append("Madina")

del friends[-1]
friends.insert(0,"Zokir")
friends.insert(2, "John")
print(friends)
yangi_mehmonlar= []
yangi_mehmonlar.append(friends.pop(0))
print(yangi_mehmonlar)