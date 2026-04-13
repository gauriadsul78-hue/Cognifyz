import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print("❌ Failed to fetch data")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    
    print("\n📜 Top Quotes:\n")
    
    for i in range(len(quotes)):
        print(f"{i+1}. {quotes[i].text}")
        print(f"   - {authors[i].text}\n")

def main():
    while True:
        print("\n==== WEB SCRAPER MENU ====")
        print("1. Show Quotes")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            scrape_quotes()
        elif choice == '2':
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
