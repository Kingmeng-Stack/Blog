import os
import re
import binascii
import traceback
rule = [0] * 256
flag = [False] * 256
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            filename = os.path.join(root, f)
            yield filename

def to(datfile):
    in_file = datfile
    out_file =re.sub(r'.dat$', '-1.jpg', datfile)
    binfile = open(in_file, 'rb')
    a = binfile.read()
    binfile.close()
    hex_in = binascii.b2a_hex(a)
    out_ret = ''
    for i in range(len(hex_in) // 2):
        hex_t = hex_in[2 * i:2 * (i + 1)]
        int_t = int(hex_t, 16)
        int_ret = rule[int_t]
        if int_ret > 15:
            hex_ret = hex(int_ret)[2:]
        else:
            hex_ret = '0' + hex(int_ret)[2:]
        out_ret += hex_ret
    hex_file = bytes.fromhex(out_ret)
    binfile = open(out_file, 'wb')
    binfile.write(hex_file)
    binfile.close()

def main():
    trans = input("输入已知的dat文件路径:")
    sheet = input("输入已知的照片文件路径:")
    trans = "E:\\00\\A.dat"
    binfile = open(trans, 'rb')
    a = binfile.read()
    hex_trans = binascii.b2a_hex(a)
    binfile = open(sheet, 'rb')
    a = binfile.read()
    hex_sheet = binascii.b2a_hex(a)
    for i in range(len(hex_trans) // 2):
        hex_t = hex_trans[2 * i:2 * (i + 1)]
        hex_s = hex_sheet[2 * i:2 * (i + 1)]
        int_t = int(hex_t, 16)
        int_s = int(hex_s, 16)
        if flag[int_t] == False:
            rule[int_t] = int_s
            flag[int_t] = True
        if flag.count(True) == 256:
            break
    base = input("规则更新完毕输入需要转换的dat文件目录:")
    for i in findAllFile(base):
        to(i)
    print("Ok")
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print('Exception Info')
        print('-' * 10)
        print('traceback.format_exc():')
        print(traceback.format_exc())
        print('-' * 10)
        
