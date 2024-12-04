Bibliotecas necessárias para o script funcionar corretamente:

Bibliotecas Padrão do Python (não requerem instalação):
* os: Para manipulação de diretórios e caminhos de arquivos.
* shutil: Para copiar arquivos de um lugar para outro.
* tkinter: Para criar interfaces gráficas simples e selecionar arquivos/pastas.

Bibliotecas adicionais (Requerem instalação):
* Pillow (instalada como Pillow): Para manipulação de imagens. O módulo usado é Image.
* numpy: Para trabalhar com arrays numéricos, essencial para a comparação pixel a pixel.
* scikit-image (instalada como scikit-image): Para calcular a SSIM (Structural Similarity Index).
* imagehash: Para gerar hashes perceptuais de imagens, usados na comparação de similaridade.

Comando para instalar:
pip install pillow numpy scikit-image imagehash
----------- Abra o cmd, copie essa linha acima, cole e dê enter.
