v = float( input("V(м/мин):") )
l = float( input("L(км):") )
l = l*1000 # метров
t = l/v # minutes
hours = t//60
minutes = int(t%60)
seconds = int((t%60 - minutes)*60)
print(f"hours:{hours}, minutes:{minutes}, seconds:{seconds}")

