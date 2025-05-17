from PIL import Image

# Abre a imagem colorida
imagem_colorida = Image.open('lena_colorida.jpg')

# Converte para escala de cinza
imagem_cinza = imagem_colorida.convert('L')

# Binariza a imagem (preto e branco)
threshold = 127
imagem_binarizada = imagem_cinza.point(lambda p: 255 if p > threshold else 0)

# Salva as imagens no formato esperado
imagem_cinza.save('lena_cinza.jpg')
imagem_binarizada.save('lena_binarizada.jpg')