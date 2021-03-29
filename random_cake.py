import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

def noise_sp(image,taxa_ruido):
    row,col,ch = image.shape
    s_vs_p = 0.5
    taxa_ruido = 0.1
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(taxa_ruido * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in [image.shape[0],image.shape[1]]]
    out[tuple(coords)] = (255,255,255)
    # Pepper mode
    num_pepper = np.ceil(taxa_ruido* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in [image.shape[0],image.shape[1]]]
    out[tuple(coords)] = (0,0,0) 
    return out
def cake(altura,largura):
	cake=np.zeros((altura,largura,3), np.uint8)
	for i in range (0,altura):
		for j in range (0,largura):
			cake[i,j]=(0,200,200)
	return cake
def random_cake(min_altura,max_altura,min_largura,max_largura):
	altura=np.random.randint(min_altura,max_altura+1)
	largura=np.random.randint(min_largura,max_largura+1)
	imagem=cake(altura,largura)
	taxa_ruido=np.random.random()
	imagem_cobertura=noise_sp(imagem,taxa_ruido)
	return taxa_ruido,imagem_cobertura

taxa_ruido,imagem_saida=random_cake(300,400,400,600)
print('taxa de ruído=',taxa_ruido)
cv2.imshow('Saida teste',imagem_saida)
cv2.waitKey(0)




'''
img_array = []
n=1000
for i in range (0,n):
    img = np.zeros((n,n),dtype=(float,3))
    for a in range (0,i):
    	for b in range (300,700):
    		img[a,b]=(150,100,40)
    img_array.append(img)


out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (n,n),0)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()'''