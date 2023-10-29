import urllib.request
import argparse
import concurrent.futures

def download_image(url):
    
    filename = url.split("/")[-1]
    
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Загружено изображение {filename}")
    except Exception as e:
        print(f"Ошибка при загрузке изображения {filename}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Загрузка изображений из списка URL-адресов")
    parser.add_argument("urls", nargs="+", help="URL-адреса изображений")
    
    args = parser.parse_args()
    urls = args.urls
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)
    
    print("Загрузка завершена")

if __name__ == "__main__":
    main()