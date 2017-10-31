import sys
import cv
import micro as mi
import initarray as ini
import sub
import split_array as SA
import printarray

if  __name__ == '__main__':
	image = sys.argv
	tool = mi.ins()
	cv.cv(image)
	before = mi.micro(tool)
	after = ini.convert(before)
	ini.filewrite(after)
	txt=sub.running()
	array = SA.sp(txt)
	finisharray = SA.divison(array)
	printarray.arrayprint(finisharray)
	#print(finisharray)