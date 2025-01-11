import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc),"
          "GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л,"
          "с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):» ")
    period = input("Введите период для данных (например, '1mo' для одного месяца)"
                   "['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']: ")
    threshold = float(input("Введите допустимый % колебания цены акции за заданный период: "))
    csv_export = input("Введите 'y' если сохранить данные в csv файл или 'n' если не сохранять: ")

    # Fetch stock data Получение данных о ценных бумагах
    stock_data = dd.fetch_stock_data(ticker, period)

    # Вычисляет и выводит среднюю цену закрытия акций за заданный период.
    dd.calculate_and_display_average_price(stock_data)

    # Анализирует данные и уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период.
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Позволяет сохранять загруженные данные об акциях в CSV файл
    if csv_export == 'y':
        dplt.export_data_to_csv(stock_data, f"{ticker}_{period}_stock_price_chart.csv")

    # Add moving average to the data Добавьте скользящее среднее значение, RSI и MACD к данным
    stock_data = dd.add_moving_average(stock_data)
    stock_data = dd.add_rsi(stock_data)  # Добавляем расчет RSI
    stock_data = dd.add_macd(stock_data)  # Добавляем расчет MACD

    # Plot the data Построим график данных
    dplt.create_and_save_plot(stock_data, ticker, period)


if __name__ == "__main__":
    main()
