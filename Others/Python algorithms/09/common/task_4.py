# Created by Nikolay Pakhomov 25.03.2025
# Алгоритм SHA-1 (Secure Hash Algorithm 1)
# Алгоритм получает на входе сообщение максимальной длины 2^64 - 1 бит и создает в качестве выхода хэш-строку длиной
# 160 бит.

def sha1(data):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    length = len(data)  # целое число 64 бита
    data = data << 1 + 1

    if len(data) % 512 > 448:
        data = data << 64

    data = data << (448 - len(data) % 512)
    data = data << 64 + length

    for part_512 in data:
        w = []
        for i in range(16):
            w[i] = part_512[:32]  # помещаем 32 бита
            part_512 = part_512[32:]

        for i in range(16, 80):
            w[i] = (w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]) << 1

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        # хеширование
        for i in range(80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999

            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1

            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC

            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (a << 5) + f + e + k + w[i]
            e = d
            d = c
            c = b << 30
            b = a
            a = temp

        h0 = h0 + a
        h1 = h1 + b
        h2 = h2 + c
        h3 = h3 + d
        h4 = h4 + e

    # конкатенация
    hash = h0 + h1 + h2 + h3 + h4

    return hash
