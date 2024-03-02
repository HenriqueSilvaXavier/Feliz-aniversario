from datetime import datetime, timedelta
hoje=datetime.now()
D=input("Data de nascimento: ")
D=D.split("/")
for n in range(0, len(D)):
	D[n]=int(D[n])
nascimento=datetime(year=D[2], month=D[1], day=D[0])
c=nascimento+timedelta(1)
a=c.year
ca=0
while (c-hoje).days<0:
	if c.month==D[1] and c.day==D[0]:
		ca=ca+1
	c=c+timedelta(1)
c=datetime(year=hoje.year, month=D[1], day=D[0])
if (hoje-c).days<0:
	c=datetime(year=hoje.year-1, month=D[1], day=D[0])
ani=c
m=c.month
cm=0
while ani<hoje:
	m2=ani.month
	if m2!=m:
		m=m2
		cm=cm+1
	ani=ani+timedelta(1)
if c.day>hoje.day:
	if D[0]!=31 and D[0]!=28:
		c2=datetime(year=hoje.year, month=(hoje.month-1), day=D[0])
	elif D[0]==31:
		c2=datetime(year=hoje.year, month=(hoje.month-1), day=D[0]-1)
		c2=c2+timedelta(1)
	elif D[0]==29:
		if hoje.year%4==0:
			c2=datetime(year=hoje.year, month=(hoje.month-1), day=D[0]-1)
			c2=c2+timedelta(1)
	d=(hoje-c2).days
	cm=cm-1
if c.day<=hoje.day:
	d=hoje.day-c.day
ani=datetime(year=hoje.year, month=D[1], day=D[0])
if (ani-hoje).days<0:
	ani=datetime(year=hoje.year+1, month=D[1], day=D[0])
if ani.day==hoje.day and ani.month==hoje.month:
	print("Feliz aniversário! 🥳")
else:
	print("Faltam {} dias para o seu aniversário".format((ani-hoje).days+1))
print("Você tem {} anos, {} meses e {} dias".format(ca, cm, d))