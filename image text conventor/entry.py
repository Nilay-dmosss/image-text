import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import pytesseract

def get_image_title(image_url):
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        return f"Error: {e}"

def main(excel_path, output_path):
    # Excel dosyasını oku
    df = pd.read_excel(excel_path)
    
    # Yeni bir DataFrame oluştur
    results = pd.DataFrame(columns=['URL', 'Title'])
    
    for index, row in df.iterrows():
        url = row['URL']
        title = get_image_title(url)
        results = results.append({'URL': url, 'Title': title}, ignore_index=True)
    
    # Sonuçları yeni bir Excel dosyasına yaz
    results.to_excel(output_path, index=False)

if __name__ == "__main__":
    excel_path = 'input.xlsx'  # Girdi Excel dosyasının yolu
    output_path = 'output.xlsx'  # Çıktı Excel dosyasının yolu
    main(excel_path, output_path)
