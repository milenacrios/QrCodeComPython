import qrcode
COLOR_RED = (255,0,0)
COLOR_SALMAO = (255,160,122)
dados = {
    'imagem': "https://i.pinimg.com/736x/01/d2/b6/01d2b61c02e9606b198f3f2c14b07543.jpg",
    'audio': "https://open.spotify.com/track/6hiKXxS7pgPKnKfCU7UJ6O?si=4a20f39b76744d72",
    'video': "https://www.youtube.com/watch?v=a9-eyE74llU"

}

if __name__ == '__main__':
    cores = [(COLOR_RED, 'white'), ('white', COLOR_RED), (COLOR_SALMAO, 'white')]
    for i, (chave, valor) in enumerate(dados.items()):
        qr = qrcode.QRCode(None, qrcode.ERROR_CORRECT_H)
        qr.add_data(valor)
        img = qr.make_image(fill_color = cores[i][0], back_color = cores[i][1])
        img.save(f'qrcode/{chave}.png')
    
