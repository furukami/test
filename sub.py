import subprocess

def running():
	txt = subprocess.run(["sugar","in.csp"],stdout = subprocess.PIPE)
	n = txt.stdout
	n = n.decode('UTF-8')
	return n
	
if __name__ == '__main__':
	txt = running()
	#print(txt)
	txt = txt.split('\n')
	i = 0
	while(i < len(txt)):
		n = txt[i].split('\t') #\tが存在するので各行でsplitを実行し分割、数字のみを取り出す
		print(n)
		i += 1
	#print(type(txt))
	#n = txt.decode('UTF-8')
	#new = n.split('\n')
	#print(n)
	#print(new)
	#print(n)
	#dst = txt.replace('\\na','\\na')
	
	