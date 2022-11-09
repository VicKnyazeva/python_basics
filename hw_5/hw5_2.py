# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def rle_encode(input_file_name, output_file_name):
    count = 0
    prev_ch = '.'

    with open(input_file_name, "r", encoding="utf-8") as file:
        text = str(file.read())

    with open(output_file_name, "w+", encoding="utf-8") as file:
        for curr_ch in text:
            if curr_ch == prev_ch:
                count += 1
                if count == 9:
                    file.write(str(count) + prev_ch)
                    count = 0
            else:
                if count > 0:
                    file.write(str(count) + prev_ch)
                prev_ch = curr_ch
                count = 1

        if count > 0:
            file.write(str(count) + prev_ch)


def rle_decode(input_file_name, output_file_name):
    with open(input_file_name, "r", encoding="utf-8") as file:
        encoded = str(file.read())

    with open(output_file_name, "w+", encoding="utf-8") as file:
        count = 0
        for ch in encoded:
            if count == 0:
                count = int(ch)
            else:
                file.write(ch * count)
                count = 0


def test():
    rle_encode("input.txt", "output1.txt")
    rle_decode("output1.txt", "output2.txt")


test()