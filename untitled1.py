# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:27:48 2020

@author: Kyser
"""

#%%
i = int(input("Enter the sale amount"))

if i <= 5000:
    disc = i * 0.10
elif i <= 10000 :
    disc = i * 0.15
elif i <= 15000:
    disc = i * 0.20
elif i >= 15000:
    disc = i * 0.30
else:
    print("invalid amount")

print("disc amount:", disc)
print("Net pay:",i - disc)