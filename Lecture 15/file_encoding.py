import sys

print('Кодировка по умолчанию:', sys.getdefaultencoding())

print('----------- Стих в кодировке UTF-8 ---------------')
file_name_utf8 = 'F:\Python\Projects\Lectures\Lecture 15\стих utf8.txt'
f_utf8 = open(file_name_utf8, encoding='utf-8')
print(f_utf8.read())
f_utf8.close()

print('----------- Стих в кодировке ANSI ---------------')
file_name_cp1251 = 'F:\Python\Projects\Lectures\Lecture 15\стих ansi.txt'
f_cp1251 = open(file_name_cp1251, encoding='cp1251')
print(f_cp1251.read())
f_cp1251.close()