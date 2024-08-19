# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:07:43 2024

@author: PHAM THU THANH
"""
lua_chon = int(input("Nhap so thu tu tuong ung voi mon an:"))
print("==========MENU==========")
print("1.Hu tieu")
print("2.Chao long")
print("3.Banh canh")
print("4.Bun rieu")
print("5.Pho bo")
print("========================")
print("Moi nhap lua chon:",lua_chon)
if lua_chon == 1:
    print("Ban da chon Hu tieu ")
elif lua_chon == 2:
    print("Ban da chon chao long")
elif lua_chon == 3:
    print("Ban da chon banh canh")
elif lua_chon == 4:
    print("Ban da chon Bun rieu")
elif lua_chon == 5:
    print("Ban da chon Pho bo")
else:
    print("Lua chon khong hop le")
print("========================")