import sys
from ioconverter import IOConverter


def put_help(mode: int):                  # put help
    if mode == 1: print('команда может передаваться в командной строке')
    print(IOConverter.get_help())
    if mode == 1: print('/exit - выход')


def conversion(line: str):              # convert line
    try:
        print(IOConverter.convert(line))
    except Exception as e:
        print(e)


def comm_line(mode: int, line: str):    # command line
    if line == '/exit':
        sys.exit(0)
    elif line == '/list':
        print(IOConverter.get_list())
    elif line == '/help':
        put_help(mode)
    else: conversion(line)


if len(sys.argv) > 1:                   # command line parameters?
    line = ''
    for i in range(1,len(sys.argv)):
        if i != 1: line += ' '
        line += sys.argv[i]
    comm_line(0, line)
    sys.exit(0)

print('Привет! Перевожу из одной валюты в другую')
put_help(1)
while(1):
    line = input('ввод : ')
    comm_line(1, line)
