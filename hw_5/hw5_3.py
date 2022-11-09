# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абвабвабвабв". Функции FIND и COUNT юзать нельзя.

from string import punctuation
import re


def remove_pattern_ver_1(pattern_string):
    re_pattern_string = "\\"+"\\".join(list(pattern_string))
    re_pattern = f"(\\w*{re_pattern_string}\\w*)"
    with open("in.txt", "r", encoding="utf-8") as file:
        data = str(file.read())
    new_data = re.sub(re_pattern, "", data)
    with open("out.txt", "w+", encoding="utf-8") as output_file:
        output_file.write(new_data)


def remove_pattern_ver_2(pattern_string):
    with open("in.txt", "r", encoding="utf-8") as file:
        data = str(file.read())
        with open("out2.txt", "w+", encoding="utf-8") as output_file:
            cp = 0  # текущая позиция в тексте
            sp = -1  # позиция последнего пробела или знака препинания
            wp = -1
            for w in data:
                if w.isspace() or any(p in w for p in punctuation):
                    if cp - sp > 1:  # накопилось слово?
                        word = data[sp + 1: cp]
                        output_word(output_file, word, pattern_string)
                    sp = cp
                else:
                    if cp - wp > 1:  # накопились промежутки?
                        output_file.write(data[wp + 1: cp])
                    wp = cp

                cp += 1

            if cp - sp > 1:  # накопилось слово?
                word = data[sp + 1: cp]
                output_word(output_file, word, pattern_string)
            if cp - wp > 1:  # накопились промежутки?
                output_file.write(data[wp + 1: cp])


def output_word(output_file, text, pattern_string):
    # skip = text.find(pattern_string) >= 0
    skip = re.search(pattern_string, text) is not None
    if not skip:
        output_file.write(text)


def task5_3():
    remove_pattern_ver_1("абв")
    # remove_pattern_ver_2("абв")


task5_3()
