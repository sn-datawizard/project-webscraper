from bs4 import BeautifulSoup
import pandas as pd
import main


url_costs = f"https://livingcost.org/cost"
url_income = f"https://www.worlddata.info/average-income.php"
url_happy = f"https://worldpopulationreview.com/country-rankings/happiest-countries-in-the-world"

soup = main.request(url_costs)
frame = soup.find("tbody")
containers = frame.find_all("tr")
container = containers[0]

country_list = []
costs_list = []

for container in containers:
	country = container.find("span", {"class": "align-middle"}).get_text()
	country_list.append(country)

	costs = container.find_all("span")[1].get_text().split("$")[1].strip()
	costs_list.append(costs)

output = pd.DataFrame({"Country": country_list, "Cost of Living in USD": costs_list})
output["Cost of Living in USD"] = output["Cost of Living in USD"].astype("int")
#print(output)
df_cost = output
#print(df_cost)

main.upload("costs", output)


soup = main.request(url_income)
frame = soup.find("table", {"id": "tabsort"})
containers = frame.find_all("tr")[1:]
container = containers[0]

country_list = []
income_list = []

for container in containers:
	country = container.find("a").get_text()
	country_list.append(country)

	income = container.find_all("td")[3].get_text().split(" ")[0].strip().replace(",", "").strip()
	income_list.append(income)

output = pd.DataFrame({"Country": country_list, "Avg. monthly Income in USD": income_list})
output["Avg. monthly Income in USD"] = output["Avg. monthly Income in USD"].astype("int")
#print(output)
print(output.dtypes)
df_income = output
#print(df_income)

main.upload("salary", output)


soup = main.request(url_happy)
frame = soup.find("tbody")
containers = frame.find_all("tr")
container = containers[0]

country_list =[]
happy_list = []

for container in containers:
	country = container.find("a").get_text()
	country_list.append(country)

	#happy = container.find_all("td")[2].get_text().replace(".", ",").strip()
	happy = container.find_all("td")[2].get_text().strip()
	happy_list.append(happy)

output = pd.DataFrame({"Country": country_list, "Happiness": happy_list})
output["Happiness"] = output["Happiness"].astype("float")
#print(output)
df_happy = output
#print(df_happy)

main.upload("happy", output)


df_1 = main.merge(df_cost, df_income)
df_2 = main.merge(df_1, df_happy)
print(df_2)
main.upload("data", df_2)