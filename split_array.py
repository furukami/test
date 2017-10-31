import sys
def sp(string):
	n = string.split('\n') #改行文字の分割
	i = 0
	while(i < len(n)):
		n[i] = n[i].split('\t') #\tが存在するので各行でsplitを実行し分割、数字のみを取り出す
		n[i][0] = n[i][0].split(' ')
		i += 1
	return n
	
def divison(n):
	array = [[0 for i in range(9)]for j in range(9)]
	i = 0
	#print(n)
	if('SATISFIABLE' in n[0][0]):
		print("satisfiable!")
		i += 1
		j = 0
		while(i < len(n)-2):
			for k in range(9):
				array[j][k]=int(n[i][1])
				i += 1
			j += 1
		return array
	elif ('UNSATISFIABLE' in n[0][0]):
		print("un satisfiable")
		sys.exit(0)
		
	