import requests
from bs4 import BeautifulSoup

busqueda = input("Ingrese término de búsqueda para Mercado Libre: ")

url = f"https://listado.mercadolibre.com.ar/{busqueda}#D[A:{busqueda}]"
# se emula navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

items = soup.find_all("div", class_="poly-card__content")

if not items:
    print("No se encontraron productos.")
else:
    for item in items:
        title_tag = item.find("h3", class_="poly-component__title-wrapper").find("a")
        title = title_tag.text.strip() if title_tag else "Sin título"
        link = title_tag['href'] if title_tag else "Sin link"

        prev_price_tag = item.find("s", class_="andes-money-amount--previous")
        prev_price = prev_price_tag.text.strip() if prev_price_tag else None

        current_price_tag = item.find("div", class_="poly-price__current")
        current_price = current_price_tag.text.strip() if current_price_tag else "Sin precio"

        discount_tag = item.find("span", class_="andes-money-amount__discount")
        discount = discount_tag.text.strip() if discount_tag else None

        installments_tag = item.find("span", class_="poly-price__installments")
        installments = installments_tag.text.strip() if installments_tag else None

        shipping_tag = item.find("span", class_="poly-shipping--next_day")
        shipping = shipping_tag.text.strip() if shipping_tag else "Sin info de envío"

        promoted_tag = item.find("a", class_="poly-component__ads-promotions")
        promoted = "Sí" if promoted_tag else "No"

        print(f"Título: {title}")
        print(f"Link: {link}")
        print(f"Precio anterior: {prev_price}")
        print(f"Precio actual: {current_price}")
        print(f"Descuento: {discount}")
        print(f"Cuotas: {installments}")
        print(f"Envío: {shipping}")
        print(f"Promocionado: {promoted}")
        print("-" * 40)
