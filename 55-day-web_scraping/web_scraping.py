import requests
from bs4 import BeautifulSoup

def scrape_website(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        books = soup.find_all('article', class_='product_pod')

        with open(output_file, 'w', encoding='utf-8') as file:
            for book in books:
                title_tag = book.find('h3').find('a')
                title = title_tag['title']  
                link = url + title_tag['href']  

                file.write(f'Title: {title}\nLink: {link}\n\n')

        print(f"Scraped data has been saved to {output_file}")

    except requests.exceptions.HTTPError as e:
        print(f'HTTP error occurred: {e}')
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data: {e}')

if __name__ == '__main__':
    base_url = 'http://books.toscrape.com/'  
    output_file = 'books.txt'
    scrape_website(base_url, output_file)
