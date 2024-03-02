from datetime import date
atual="{}".format(date.today())
atual=atual.replace("-", " ")
atual=atual.split()
for k in range(0, len(atual)):
	atual[k]=int(atual[k])
print(atual)
n=input("Digite sua data de nascimento: ")
n=n.replace("/", " ")
n=n.split()
n=n[::-1]
for k in range(0, len(n)):
	n[k]=int(n[k])
print(n)
def tempo(n):
	if atual[1]<n[1]:
		return True
	elif atual[1]==n[1]:
		if atual[2]<n[2]:
			return True
		elif atual[2]>n[2]:
		    return False
	elif atual[1]>n[1]:
		return False
if n[1]==atual[1] and n[2]==atual[2]:
	print("Feliz aniversário!")
i=atual[0]-n[0]-1
tempo(n)
if tempo(n)==True:
	i=i+1
print("Você tem {} anos".format(i))