from bs4 import BeautifulSoup
import requests

HEADERS = {'user-agent': 'Mozilla/5.0'}

from bs4 import BeautifulSoup
import requests
SAMPLE_RECIPE_URL = 'https://www.nationaltrust.org.uk/discover/food/recipes/pies-savoury-treats/pizza'


def get_recipe_details(recipe_url):

    r = requests.get(recipe_url, headers=HEADERS)

    recipe_html = r.text
    
    soup = BeautifulSoup(recipe_html, 'html.parser')

    # Ingredients #1
    divs = soup.find_all("div", class_="Sectionstyle__Content-sc-1rnt8u1-3")
    ingredients_uls = divs[5].find_all("ul")
    ingredients1_lis = ingredients_uls[0].find_all("li")
    ingredients2_lis = ingredients_uls[1].find_all("li")


    ingredients1 = [li.text.replace("\xa0", " ") for li in ingredients1_lis]
    ingredients2 = [li.text.replace("\xa0", " ") for li in ingredients2_lis]

    # Steps (list of steps)
    step_ps = soup.find_all(attrs={"data-testid":"recipe-steps--description"})
    
    steps = [step_p.p.text for step_p in step_ps]

    return {
        'ingredients1': ingredients1,
        'ingredients2': ingredients2,
        'steps': steps
        }


    




