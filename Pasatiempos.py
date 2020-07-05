from bs4 import BeautifulSoup
import requests
import img2pdf
import shutil
import os


url = r'https://www.tuexperto.com/2020/03/30/100-pasatiempos-para-toda-la-familia-para-descargar-e-imprimir/#21_crucigramas_para_imprimir_y_resolver_online'
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
images = soup.find_all('img')
img_list = []
for img in images:
    img_list.append(img['data-src'])

del img_list[0:9]
del img_list[-12:]

pasatiempos = list(set(img_list))
#for img in pasatiempos:
    #filename = img.split("/")[-1]
    #file_path = os.path.join(r'C:\Users\ggalina\Pasatiempos\Imagenes', filename)
   # img_file = requests.get(img, stream = True) # Stream = True es to guarantee no interruptions
    #img_file.decode_content = True # Otherwise the downloaded image file's size will be zero
    #with open(file_path,'wb') as f:
        #shutil.copyfileobj(img_file.raw,f)

# convert all files ending in .jpg inside a directory
dirname = r'C:\Users\ggalina\Pasatiempos\Imagenes'

with open("Pasatiempos.pdf", "wb") as f:
    imgs = []
    for fname in os.listdir(dirname):
        path = os.path.join(dirname,fname)
        imgs.append(path)
    f.write(img2pdf.convert(imgs))

# Esto te tira el nombre de la imagen en el url
# filename = print(img.split("/")[-1])

# Con esto consigues el archivo de cada url en la lista
# url de la lista = requests.get(elemento de la lista (uurl), stream = True)
# https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c
