import requests
import pandas as pd
from bs4 import BeautifulSoup


def main():
    try:
        result = requests.get(
            "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
        )
    except Exception as e:
        print(e)
        return

    soup = BeautifulSoup(result.content, "html.parser")
    table_rows = soup.find_all(
        "table", class_="wikitable sortable plainrowheaders"
    )[0].find("tbody").find_all("tr")

    for row in table_rows[2:]:
        state = row.find_all("th", scope="row")
        print(state)
        break

    # with open("/Users/Sarthak/Desktop/School Projects/Data Science/project_4/states.html", "a") as f:
    #     f.write(table_body.prettify())


if __name__ == '__main__':
    main()
