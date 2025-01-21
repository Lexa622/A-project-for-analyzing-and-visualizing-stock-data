import matplotlib.pyplot as plt
import pandas as pd
from bokeh.io import output_file
from bokeh.plotting import figure, show


def create_and_save_bokeh(data, ticker):
    # Рисунок будет отображен в статическом HTML-файле
    output_file(f'Интерактивный_график_{ticker}.html',
                title=f'График цен закрытия {ticker}')
    # Настройка объекта.
    fig = figure(height=500,
                 width=900,
                 x_axis_label='Дата',
                 y_axis_label='Цена закрытия',
                 x_range=(data.index[0], data.index[-1]),
                 title=f'Интерактивный график {ticker}')
    # Координаты в линии.
    fig.line(x=data.index, y=data['Close'], color='blue', line_width=1)
    # Вывод в браузер.
    show(fig)
    average_close = data['Close'].mean()
    print(f'Среднее значение колонки "Close": {average_close}')


def create_and_save_plot(data, ticker, period, chart_design_style, filename=None):
    plt.figure(figsize=(11, 7))
    plt.subplot(4, 1, 1)
    plt.style.use(chart_design_style)
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.ylabel("Цена")
    plt.legend(loc='upper left')

    # График RSI
    plt.subplot(4, 1, 2)
    plt.plot(data.index, data['RSI'], label='RSI', color='blue')
    plt.axhline(70, linestyle='--', alpha=0.5, color='black')
    plt.axhline(30, linestyle='--', alpha=0.5, color='black')
    plt.ylabel("RSI")
    plt.legend(loc='upper left')

    # График MACD
    plt.subplot(4, 1, 3)
    plt.bar(data.index, data['MACD'], label='MACD', color='blue')
    plt.plot(data.index, data['Signal'], label='Signal Line', color='red')
    plt.ylabel("MACD")
    plt.legend(loc='upper left')

    # График стандартного отклонения цены закрытия
    plt.subplot(4, 1, 4)
    plt.plot(data.index, data['STDev'], label='STDev', color='red')
    plt.xlabel("Дата")
    plt.ylabel("STDev")
    plt.legend(loc='upper left')

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def export_data_to_csv(data, filename):
    """Сохраняет загруженные данные об акциях в CSV файл"""
    data.to_csv(filename)
    print(f"Файл сохранен как {filename}")
