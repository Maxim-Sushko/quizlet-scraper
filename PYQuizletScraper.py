import requests
from bs4 import BeautifulSoup

# URL of the Quizlet page to scrape
url = "https://quizlet.com/565984174/abeka-11th-grade-us-history-test-9-nine-weeks-exam-flash-cards/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all flashcard terms and definitions
    flashcards = soup.find_all('div', class_='SetPageTerm-content')
    
    # Loop through each flashcard and extract the term and definition
    for flashcard in flashcards:
        term = flashcard.find('div', class_='SetPageTerm-wordText').text.strip()
        definition = flashcard.find('div', class_='SetPageTerm-definitionText').text.strip()
        print(f"Term: {term}\nDefinition: {definition}\n")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")