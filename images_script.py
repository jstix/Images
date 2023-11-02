import os
import requests
from bs4 import BeautifulSoup
import urllib.request

# Define your search terms
search_terms = ['Barbers', 'Accountancy', 'Florist', 'Removals', 'Dentist', 'Supermarket', 'Window cleaners', 'Day nursery', 'Furniture shop', 'Driving school', 'Hospitality', 'Garden Services', 'Beauty salon']  # Add all your 29 search terms here

# Define the path to your Images folder on Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Images")

for term in search_terms:
    # Create a new folder for each search term in your Images folder on Desktop
    folder_path = os.path.join(desktop_path, term)
    os.mkdir(folder_path)

    # Send a GET request to Unsplash
    response = requests.get(f"https://unsplash.com/s/photos/{term}")

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all img tags on the page
    img_tags = soup.find_all('img')

    # Download the first 20 images
    for i, img_tag in enumerate(img_tags[:20]):
        img_url = img_tag.get('src')
        urllib.request.urlretrieve(img_url, f'{folder_path}/{term} {i+1}.jpg')
