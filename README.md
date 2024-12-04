IMPORTANTE:
Algumas texturas, o script pode ter dificuldade de diferenciar, então se for alguma textura muito escura, pode haver alguma captura-falsa, valide a textura obtida pelo script, antes de fazer as alterações.
-------------------------------

1 - extraia as imagens dos arquivos do jogo (stream5ra.bun, stream5rb.bun) em formato JPG, pois se extrair em formato PNG, as texturas vão ficar muito escuras, e sujar o resultado. Demais texturas, como da pasta Global, Frontend, podem ser extraidas como PNG, caso contrário, logos de marcas por exemplo, a imagem ficará toda branca.
2 - extraia as texturas no jogo, pelo Texmod.exe
3 - Abra o script pelo VSCode, para rodar o python a partir dele (Não é um executável)
4 - Rode o script, selecione a textura extraída pelo Texmod.exe e selecione a pasta com as texturas extraídas no passo 1
5 - Espere o script concluir o procedimento, a velocidade de finalização vai depender da quantidade de imagens na pasta geral (passo 1)
6 - Assim que o script finalizar o processo, vai constar a mensagem no terminal do VSCode, então vá até o diretório onde estão as texturas do TexMod.exe, e verifique se obteve êxito na captura.
---------------------

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

-----------
Abra o cmd, copie essa linha acima, cole e dê enter.
