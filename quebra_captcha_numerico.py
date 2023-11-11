from playwright.sync_api import sync_playwright
import cv2
import pytesseract
import os

# Declara url do site e caminho da pasta onde será salva a imagem do captcha
url = 'insert URL'
caminho_destino = 'insert destiny path'


def QuebraCaptchaNumerico(url, caminho_destino):
    with sync_playwright() as p:
        # Acessa site
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url),

        # Baixa imagem gerada do captcha informando o elemento path
        imagem_elemento = page.locator('insert path image')
        imagem_elemento.screenshot(path=caminho_destino)

        # Lê imagem e retorna o número do captcha
        pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
        texto = pytesseract.image_to_string(
            cv2.imread(caminho_destino), lang="por")

        print(f'O CAPTCHA É: {texto}')

        # Excluir a imagem após a leitura
        os.remove(caminho_destino)

        input('STOP')


QuebraCaptchaNumerico(url, caminho_destino)
