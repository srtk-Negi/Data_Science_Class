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
    content_table = soup.find_all(
        "table", class_="wikitable sortable plainrowheaders")[0]
    content_rows = content_table.find("tbody").find_all("tr")

    states = []
    population = []
    for row in content_rows[2:]:
        states.append(row.find("th", scope="row").find("a").text)
        population.append(row.find("div", style="float:right;").text)

    state_population_map = {}
    for i in range(len(states)):
        state_population_map[states[i]] = population[i]

    df = pd.DataFrame(list(state_population_map.items()),
                      columns=['State', 'Population'])

    print(df)
    df.to_csv("us_info.csv")


if __name__ == '__main__':
    main()
