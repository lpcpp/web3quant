from api.currency import Currency


if __name__ == '__main__':
    c = Currency()
    # output: ["console", "csv"], default="console"
    c.get_currency_with_marketcap(start=300000000, end=500000000, output="console")
