
with open('8x.dic', 'r') as f:
    res = f.read()


with open('8x777.dic', 'w') as fw:
    for i in res.splitlines():
        fw.writelines('777' + i + '\n')
