# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:40:04 2019

@author: Tsvetomir Gotsov
J1939 PGN Calculator
"""
print("Hex ID Mesage:")
CAN_Mesage = int(input(),16)
BIN_CAN = bin(CAN_Mesage)
Priority = CAN_Mesage >> 26
print("Priority:",Priority)
PGN = (CAN_Mesage & 0b00000011111111111111111100000000) >> 8
print("PGN:",PGN)
SourceAdress = (CAN_Mesage & 0b00000000000000000000000011111111)
print("Source Adress:",SourceAdress)

# 18FF72E0