for i in range(1,5):
    k = ['cp866','cp1251','UTF-16LE','UTF-16BE']
    for t in range(len(k)):
        f=open('text-'+str(i)+'.txt', 'r', encoding = k[t])
        text = f.read()
        f.close()
        if text.find('Привет') != -1:
            print(text + k[t])
