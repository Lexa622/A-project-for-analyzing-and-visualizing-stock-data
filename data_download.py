import yfinance as yf


# Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными.
def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


# Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


# Вычисляет и выводит среднюю цену закрытия акций за заданный период.
def calculate_and_display_average_price(data):
    df = data['Close'].values
    average_closing_price = sum(df) / len(df)
    print(f"Средняя цена закрытия акций за заданный период: {average_closing_price}")
