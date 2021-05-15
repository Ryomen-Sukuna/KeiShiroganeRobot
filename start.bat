@echo off
TITLE Kei bot
:: Enables virtual env mode and then starts kei
env\scripts\activate.bat && py -m tg_bot
