#! /usr/bin/python3
# -*- coding: utf-8 -*-

import random


def gen_card_num(start_with, total_num):
    result = start_with

    # 随机生成前N-1位
    while len(result) < total_num - 1:
        result += str(random.randint(0, 9))

    # 计算前N-1位的校验和
    s = 0
    card_num_length = len(result)
    for _ in range(2, card_num_length + 2):
        t = int(result[card_num_length - _ + 1])
        if _ % 2 == 0:
            t *= 2
            s += t if t < 10 else t % 10 + t // 10
        else:
            s += t

    # 最后一位当做是校验位，用来补齐到能够整除10
    t = 10 - s % 10
    result += str(0 if t == 10 else t)
    return result


def luhn(card_num):
    s = 0
    card_num_length = len(card_num)
    for _ in range(1, card_num_length + 1):
        t = int(card_num[card_num_length - _])
        if _ % 2 == 0:
            t *= 2
            s += t if t < 10 else t % 10 + t // 10
        else:
            s += t
    return s % 10 == 0


def random_vin():
    # 内容的权值
    content_map = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 0, 'J': 1, 'K': 2, 'L': 3,
        'M': 4, 'N': 5, 'O': 0, 'P': 7, 'Q': 8, 'R': 9, 'S': 2, 'T': 3,
        'U': 4, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, 'Z': 9, "0": 0, "1": 1,
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
    }
    # 位置的全值
    location_map = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    vin = ''.join(random.sample('0123456789ABCDEFGHJKLMPRSTUVWXYZ', 12))
    vin = vin + ''.join(random.sample('0123456789', 5))
    num = 0
    for i in range(len(vin)):
        num = num + content_map[vin[i]] * location_map[i]
    vin9 = num % 11
    if vin9 == 10:
        vin9 = "X"
    list1 = list(vin)
    list1[8] = str(vin9)
    vin = ''.join(list1)
    return vin


if __name__ == '__main__':
    for _ in range(50):
        random_card_num = gen_card_num('622848', 16)
        valid_result = luhn(random_card_num)
        print('%s %s' % (random_card_num, valid_result))
        print('%s' % (random_vin()))
