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
    start = input("Введите конкретную дату начала анализа(например, '1970-01-30'): ")
    end = input("Введите конкретную дату окончания анализа(например, '2025-01-14'): ")
    chart_design_style = input("Введите стиль оформления графиков ('Solarize_Light2', '_classic_test_patch',"
                               "'_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background',\n"
                               "'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10', 'seaborn-v0_8',"
                               "'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark',\n"
                               "'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep',"
                               "'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper',\n"
                               "'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk',"
                               "'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid',"
                               "'tableau-colorblind10'): ")
    threshold = float(input("Введите допустимый % колебания цены акции за заданный период: "))
    csv_export = input("Введите 'y' если сохранить данные в csv файл или 'n' если не сохранять: ")

    # Fetch stock data Получение данных о ценных бумагах.
    stock_data = dd.fetch_stock_data(ticker, period, start, end)
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
    stock_data = dd.st_dev(stock_data)  # Добавляем расчет стандартного отклонения цены закрытия

    # Plot the data Построим график данных
    dplt.create_and_save_plot(stock_data, ticker, period, chart_design_style)

    dplt.create_and_save_bokeh(stock_data, ticker)


if __name__ == "__main__":
    main()
