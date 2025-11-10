# Grafika_zad_1.py
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Adres obrazu (banan)
IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Cavendish_banana_from_Maracaibo.jpg/960px-Cavendish_banana_from_Maracaibo.jpg"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def main():
    # Pobranie obrazu z internetu
    req = urllib.request.Request(IMAGE_URL, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = resp.read()

    # Dekodowanie przez OpenCV (BGR) i konwersja do RGB
    arr = np.frombuffer(data, dtype=np.uint8)
    bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

    # Podgląd oryginału (matplotlib)
    plt.imshow(rgb)
    plt.axis('off')
    plt.title("Oryginalny obraz")
    plt.show()

    # Zmniejszenie, skala szarości, obrót 90° w prawo
    h, w = rgb.shape[:2]
    half = cv2.resize(rgb, (w // 2, h // 2), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(half, cv2.COLOR_RGB2GRAY)
    rotated = cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)

    # Podgląd wyniku (matplotlib) + zapis do pliku
    plt.imshow(rotated, cmap='gray')
    plt.axis('off')
    plt.title("Obraz po zmianach")
    plt.show()

    # Zapis wyniku do pliku PNG (możesz potem go podejrzeć/otworzyć)
    out_path = "obraz_po_zmianach.png"
    # UWAGA: cv2.imwrite oczekuje obrazu w BGR/1-kanał, tu jest 1-kanał (OK).
    cv2.imwrite(out_path, rotated)
    print(f"Zapisano wynik do: {out_path}")

    # Macierz pikseli
    print(rotated)

if __name__ == "__main__":
    main()
