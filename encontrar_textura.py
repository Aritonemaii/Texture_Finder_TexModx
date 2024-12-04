import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from PIL import Image
import numpy as np
from skimage.metrics import structural_similarity as ssim
import imagehash

VALID_EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp", ".tiff"}

def compare_images_ssim(img1, img2):
    """Calcula a similaridade estrutural (SSIM) entre duas imagens."""
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    # Adapta para o menor tamanho sem redimensionar
    min_height = min(arr1.shape[0], arr2.shape[0])
    min_width = min(arr1.shape[1], arr2.shape[1])

    arr1_cropped = arr1[:min_height, :min_width]
    arr2_cropped = arr2[:min_height, :min_width]

    return ssim(arr1_cropped, arr2_cropped, multichannel=True, channel_axis=-1)

def compare_images_hash(img1, img2):
    """Compara imagens usando hash perceptual."""
    hash1 = imagehash.phash(img1)
    hash2 = imagehash.phash(img2)
    return abs(hash1 - hash2)

def find_matching_image(random_image_path, original_folder_path):
    """Procura a imagem mais semelhante à imagem fornecida na pasta original."""
    random_image = Image.open(random_image_path).convert('RGB')
    best_match = None
    highest_ssim = -1
    smallest_hash_diff = float('inf')

    for root, _, files in os.walk(original_folder_path):
        for file in files:
            original_image_path = os.path.join(root, file)

            # Ignorar arquivos com extensões inválidas
            if not any(file.lower().endswith(ext) for ext in VALID_EXTENSIONS):
                continue

            try:
                original_image = Image.open(original_image_path).convert('RGB')

                # Calcula SSIM
                ssim_value = compare_images_ssim(random_image, original_image)

                # Calcula diferença de hash
                hash_diff = compare_images_hash(random_image, original_image)

                # Verifica a melhor combinação (SSIM alto + hash diff baixo)
                if ssim_value > highest_ssim or (ssim_value == highest_ssim and hash_diff < smallest_hash_diff):
                    highest_ssim = ssim_value
                    smallest_hash_diff = hash_diff
                    best_match = original_image_path
            except Exception as e:
                print(f"Erro ao processar {original_image_path}: {e}")
                continue

    return best_match

# Interface gráfica para selecionar arquivos e pastas
def select_file_or_folder():
    Tk().withdraw()  # Oculta a janela principal do Tkinter

    # Seleciona a textura com nome aleatório
    print("Selecione a textura com nome aleatório.")
    random_image_path = askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if not random_image_path:
        print("Nenhuma textura foi selecionada.")
        return None, None

    # Seleciona a pasta com as texturas originais
    print("Selecione a pasta com as texturas originais.")
    original_folder_path = askdirectory()
    if not original_folder_path:
        print("Nenhuma pasta foi selecionada.")
        return None, None

    return random_image_path, original_folder_path

# Principal
random_image_path, original_folder_path = select_file_or_folder()

if random_image_path and original_folder_path:
    result = find_matching_image(random_image_path, original_folder_path)
    if result:
        # Copiar a imagem encontrada para o mesmo diretório da imagem aleatória
        destination_dir = os.path.dirname(random_image_path)
        shutil.copy(result, destination_dir)
        print(f"A textura correspondente foi copiada para: {destination_dir}")
    else:
        print("Nenhuma textura correspondente foi encontrada.")
else:
    print("Operação cancelada.")
