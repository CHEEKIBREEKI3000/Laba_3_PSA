import os
for i in range(1,8):
    f=open('BinaryFiles/file00'+str(i), 'rb')
    a=f.read(8)
    wer=''
    if a.hex()=='89504e470d0a1a0a':
        wer='.png'
    if a.hex()=='255044462d312e33':
        wer='.pdf'
    if a.hex()=='4f54544f000b0080':
        wer='.otf'
    if a.hex()=='ffd8ffe000104a46':
        wer='.jpg'
    if a.hex()=='526172211a070100':
        wer='.rar'
    if a.hex()=='377abcaf271c0004':
        wer='.7z'
    if a.hex()=='504b030414030000':
        wer='.zip'
    f.close()
    os.rename('BinaryFiles/file00'+str(i),'BinaryFiles/file00'+str(i)+wer)
