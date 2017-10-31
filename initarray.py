import printarray
import micro as mi
			
def convert(data):
	array = [ [0 for p in range(len(data))] for k in range(len(data))]
	for i in range(len(data)):
		for j in range(len(data)):
			if data[i][j] == '1':
				array[i][j] = 1
			elif data[i][j] == '2':
				array[i][j] = 2
			elif data[i][j] == '3':
				array[i][j] = 3
			elif data[i][j] == '4':
				array[i][j] = 4
			elif data[i][j] == '5':
				array[i][j] = 5
			elif data[i][j] == '6':
				array[i][j] = 6
			elif data[i][j] == '7':
				array[i][j] = 7
			elif data[i][j] == '8':
				array[i][j] = 8
			elif data[i][j] == '9':
				array[i][j] = 9
			elif data[i][j] == ' ':
				array[i][j] = 0
	#printarray.arrayprint(array)
	return array

def filewrite(data):
	f = open('in.csp','w')
	for i in range(len(data)):
		for j in range(len(data)):
			if data[i][j] == 1:
				#f.write("(int x_"+i+"_"+j+" "+data[i][j]+" "+data[i][j]+")")
				f.write("(int x_{}_{} {} {})\n".format(i,j,data[i][j],data[i][j]))
			elif data[i][j] == 2:
				#f.write("(int x_"+i+"_"+j+" "+data[i][j]+" "+data[i][j]+")")
				f.write("(int x_{}_{} {} {})\n".format(i,j,data[i][j],data[i][j]))
			elif data[i][j] == 3:
				#f.write("(int x_"+i+"_"+j+" "+data[i][j]+" "+data[i][j]+")")
				f.write("(int x_{}_{} {} {})\n".format(i,j,data[i][j],data[i][j]))
			elif data[i][j] == 4:
				#f.write("(int x_"+i+"_"+j+" "+data[i][j]+" "+data[i][j]+")")
				f.write("(int x_{}_{} {} {})\n".format(i,j,data[i][j],data[i][j]))
			elif data[i][j] == 5:
				#f.write("(int x_"+i+"_"+j+" "+data[i][j]+" "+data[i][j]+")")
				f.write("(int x_{}_{} {} {})\n".format(i,j,data[i][j],data[i][j]))
			elif data[i][j] == 6:
				#f.write("(int x_"+i+"_"+j+" "+data[i][j]+" "+data[i][j]+")")
				f.write("(int x_{}_{} {} {})\n".format(i,j,data[i][j],data[i][j]))
			elif data[i][j] == 7:
				#f.write("(int x_"+i+"_"+j+" "+data[i][j]+" "+data[i][j]+")")
				f.write("(int x_{}_{} {} {})\n".format(i,j,data[i][j],data[i][j]))
			elif data[i][j] == 8:
				#f.write("(int x_"+i+"_"+j+" "+data[i][j]+" "+data[i][j]+")")
				f.write("(int x_{}_{} {} {})\n".format(i,j,data[i][j],data[i][j]))
			elif data[i][j] == 9:
				#f.write("(int x_"+i+"_"+j+" "+data[i][j]+" "+data[i][j]+")")
				f.write("(int x_{}_{} {} {})\n".format(i,j,data[i][j],data[i][j]))
			elif data[i][j] == 0:
				#f.write("(int x_"+i+"_"+j+"1 9)")
				f.write("(int x_{}_{} 1 9)\n".format(i,j))
				
	for i in range(len(data)):
		f.write("(alldifferent" )
		for j in range(len(data)):
			#f.write(" x_"+j+"_"+i)
			f.write(" x_{}_{}".format(j,i))
		f.write(")\n")
	for i in range(len(data)):
		f.write("(alldifferent" )
		for j in range(len(data)):
			#f.write(" x_"+i+"_"+j)
			f.write(" x_{}_{}".format(i,j))
		f.write(")\n")
	
	for i in range(0,len(data),3):
		for j in range(0,len(data),3):
			twoadder(i,j,f)
	f.close()
	
def twoadder(n,m,f):
	i = n
	f.write("(alldifferent")
	while(i < n+3):
		j = m
		while(j < m+3):
			#f.write(" x_"+i+"_"+j)
			f.write(" x_{}_{}".format(i,j))
			j+=1
		i+=1
	f.write(")\n")
	
if __name__ == '__main__':
	tool = mi.ins()
	before = mi.micro(tool)
	after = convert(before)
	printarray.arrayprint(after)