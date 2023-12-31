
def Encrypt(text:str,keyLength:int, mode:bool):
    alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphLength = len(alph)
    k = -1
    if mode:
        k = 1
    encrypted = []
    for sign in text.lower():
        if (sign not in alph):
            encrypted.append(sign)
            continue
        encrypted.append( alph[ ( alph.find(sign) + k*keyLength )%alphLength ] )
    return "".join(encrypted)

text = """Информационные технологии призваны, основываясь и рационально используя современные достижения в области компьютерной техники и иных высоких технологий, новейших средств коммуникации, программного обеспечения и практического опыта, решать задачи по эффективной организации информационного процесса для снижения затрат времени, труда, энергии и материальных ресурсов во всех сферах человеческой жизни
и современного общества. Информационные технологии взаимодействуют и часто составляющей частью входят в сферы услуг, области управления, промышленного производства, социальных процессов"""
res = Encrypt(text,1,True,end = "\n\n")
print( res )
print( Encrypt(res,1,False) )
