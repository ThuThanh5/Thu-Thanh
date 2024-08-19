# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:57:43 2024

@author: Student
"""
from datetime import datetime
Nam_sinh = int(input("Nhap nam sinh:"))
Nam_hien_tai = datetime.now().year
Tuoi = Nam_hien_tai - Nam_sinh
print("Ban sinh nam",Nam_sinh,"vay ban",Tuoi,"tuoi")
