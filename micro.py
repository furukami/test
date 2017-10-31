import cv2
import numpy as np
import pyocr
import pyocr.builders
try:
	import Image
except ImportError:
	from PIL import Image
import printarray

def ins():
	tools = pyocr.get_available_tools()
	if len(tools) == 0:
		print("No OCR tool found")
		sys.exit(1)
	return tools[0]
	
def resize_bilinear(src, h, w):
	# 出力画像用の配列生成（要素は全て空）
    dst = np.empty((h,w))

    # 元画像のサイズを取得
    hi, wi = src.shape[0], src.shape[1]

    # 拡大率を計算
    ax = w / float(wi)
    ay = h / float(hi)
    
    # バイリニア補間法
    for y in range(0, h):
        for x in range(0, w):
            xi, yi = x/ax, y/ay
            x0, y0 = int(xi), int(yi)

             # 存在しない座標の処理
            if x0 > wi - 2: x0 = wi - 2
            if y0 > hi - 2: y0 = hi - 2
            
            # 重みの計算
            dx = xi - x0
            dy = yi - y0
            
            dst[y][x] = (1 - dx) * (1-dy) * src[y0][x0] + dx * (1-dy) * src[y0][x0+1] + (1-dx) * dy * src[y0][x0+1] + dx * dy * src[y0+1][x0+1]
            
    return dst

def micro(tool):
	m = 7
	b = 0
	data = [ [0 for p in range(9)] for k in range(9)]
	image = cv2.imread("test.png",0)
	height , width = image.shape
	h = int(height/9)
	vh = int(height/9)
	for i in range(9):
		n = 7
		w = int(width/9)
		vw = int(width/9)
		for j in range(9):
			cle = image[m:h,n:w]
			cle = resize_bilinear(cle, 1000, 1000)
			cv2.imwrite("stract{}.png".format(b),cle)
			data[i][j] = tool.image_to_string(	Image.open("stract{}.png".format(b)) ,builder = pyocr.builders.TextBuilder(tesseract_layout=6))
			#print(data[i][j])
			n += vw
			w += vw-1
			b += 1
		m += vh
		h += vh
	#printarray.arrayprint(data)
	return data
	
	
if __name__ == '__main__':
	tool=ins()
	datas=micro(tool)
	printarray.arrayprint(datas)
