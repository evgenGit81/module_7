# -*- coding: utf-8 -*-
stihi = 'stih.txt'
file_read = open(stihi, "r", encoding='utf8')
file_count = file_read.read()
file_read.close()
print(file_count)

