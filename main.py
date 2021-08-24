from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome("/Users/Kamiklza/PycharmProjects/chromedriver")

driver.get("https://www.empireonline.com/movies/features/best-movies-2")
soup = BeautifulSoup(driver.page_source, "html.parser")

movies = soup.find_all(name="div", class_="listicle-item")

for movie in reversed(movies):
    title = movie.find("h3").getText()
    with open("movie_list.txt", "a") as file:
        file.write(f"{title}\n")




# movie = movies[0]
# title = movie.find("h3").getText()
# print(title)