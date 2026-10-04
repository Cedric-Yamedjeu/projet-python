from datetime import date, timedelta


import requests


def get_rates(currencies, nb_days=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=nb_days)

    symbols = ','.join(currencies)
    r = requests.get(
        f"https://www.docstring.fr/api/rates/history/?start_at={start_date}&end_at={end_date}&symbols={symbols}",
        timeout=10,
    )

    #print("URL appelée :", r.url)
    #print("Statut HTTP :", r.status_code)

    if not r.ok or not r.json():
        return False, False

    api_rates = r.json().get("rates")
    if not api_rates:
        return False, False

    #pprint(api_rates)
    all_days = sorted(api_rates.keys())
    #all_rates = [api_rates[day] for day in all_days]
    all_rates = {
        currency: [api_rates[day][currency] for day in all_days]
        for currency in currencies
    }
    #pprint(all_rates)
    return all_days, all_rates


if __name__ == '__main__':
    days, rates = get_rates(currencies=["USD", "EUR"], nb_days=30)
    #print(days)
    #print(rates)