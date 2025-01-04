import yfinance as yf


# Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными.
def fetch_stock_data(ticker, period='1mo'):
    """Получает исторические данные об акциях для указанного тикера и временного периода.
    Возвращает DataFrame с данными."""
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


# Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
def add_moving_average(data, window_size=5):
    """Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия."""
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


# Вычисляет и выводит среднюю цену закрытия акций за заданный период.
def calculate_and_display_average_price(data):
    """Функция принимает DataFrame, вычисляет и выводит в консоль среднюю цену закрытия акций за заданный период"""
    df = data['Close'].values
    average_closing_price = sum(df) / len(df)
    print(f"Средняя цена закрытия акций за заданный период: {average_closing_price:.{5}f}")


def notify_if_strong_fluctuations(data, threshold):
    """Функция вычисляет максимальное и минимальное значения цены закрытия и сравнивает разницу с заданным порогом.
    Если разница превышает порог, пользователь получает уведомление."""
    df = data['Close'].values
    price_fluctuation = (max(df) - min(df)) / max(df) * 100
    if price_fluctuation > threshold:
        print(f"Цена акций колебалась более чем на {threshold}% за период: {price_fluctuation:.{5}f}%")
