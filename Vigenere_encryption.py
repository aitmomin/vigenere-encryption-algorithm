def Chiffrement_vigenere(msg, clef):
	d={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j' :9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
	t=tuple(d)
	msg=msg.lower()
	clef=clef.lower()
	taille1=len(msg)
	taille2=len(clef)
	new_msg=""
	i=0	#message counter
	j=0	#key counter
	z=0	#dictionary key value
	
	while i < taille1:
		#test if the counter reaches the end of the key
		if j==taille2:
			j=0	
		#test if the character is not an alphabet
		if not msg[i].isalpha() or not clef[j].isalpha():
			new_msg=new_msg+msg[i]
			j+=1
			i+=1
			continue		
		#put the key value returned by the dictionary in x and y
		x=d[msg[i]]
		y=d[clef[j]]
		#test if the value exceeds the interval [0.25]		
		if x+y > 26:
			z=(x+y)%26	#z=x+y-26
		else:
			z=x+y
		#put the character returned by the tuple in the new string, whose z is the value of this character
		new_msg=new_msg+t[z]
		j+=1
		i+=1
		
	return new_msg