import requests
import bs4


def main():
    # print the header
    print_header()
    # get zip code from user
    zip_code = input('What is your zip code (96001)? ')

    # get html from web
    html = get_html_from_web(zip_code)
    # parse the html
    get_weather_from_html(html)
    # display for the forecast


def print_header():
    print('--------------------------')
    print('       WEATHER APP')
    print('--------------------------')
    print()


def get_html_from_web(zip_code):
    url = 'https://www.wunderground.com/weather/us/or/portland/{}'.format(zip_code)
    response = requests.get(url)
    return response.text
    # print(response.text[0:250])


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip().replace("\n", "")
    return text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    loc = soup.find('h1').get_text()
    loc = cleanup_text(loc)
    temp = soup.find(class_='current-temp').get_text()
    temp = cleanup_text(temp)
    # todo: continue lesson 50
    print(loc, temp)


if __name__ == '__main__':
    main()

