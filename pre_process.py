import re

# cur_ch：現在対象としている文字
# pre_ch：一文字前に処理した文字
# src_filename：前処理をする文章
# new_filename_1：空白、改行をなくした文章
# new_filename_2：出力ファイル

src_filename = 'script/2.txt'
new_filename_1 = 'a.txt'
new_filename_2 = 'b.txt'

""" Reads a text file char by char. """
def iter_chars(filename):
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    for ch in content:
        yield ch

with open(src_filename) as f:
    for line in f.readlines():
        if len(line) >= 2:
            table = str.maketrans({
                v: '' for v in '\u3000 \x0c\x0b\t'
            })
            text = line.translate(table)
            with open(new_filename_1, mode = "a") as f:
                for s in text.splitlines():
                    f.write(s)

with open(new_filename_2, mode = "a") as f1:
    for ch in iter_chars(new_filename_1):
        f1.write(ch)
        if ch == "。" :
            print("改行")
            f1.write("\n")

         
