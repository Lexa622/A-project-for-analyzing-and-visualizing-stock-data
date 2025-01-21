import yfinance as yf


# Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными.
def fetch_stock_data(ticker, period='1mo', start='1970-01-01', end='2070-12-31'):     #
    """Получает исторические данные об акциях для указанного тикера и временного периода.
    Возвращает DataFrame с данными."""
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, start=start, end=end)     #
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
    return average_closing_price


def notify_if_strong_fluctuations(data, threshold):
    """Функция вычисляет максимальное и минимальное значения цены закрытия и сравнивает разницу с заданным порогом.
    Если разница превышает порог, пользователь получает уведомление."""
    df = data['Close'].values
    price_fluctuation = (max(df) - min(df)) / max(df) * 100
    if price_fluctuation > threshold:
        print(f"Цена акций колебалась более чем на {threshold}% за период: {price_fluctuation:.{5}f}%")


def add_rsi(data, rsi_period=14):
    """Рассчитывает RSI."""
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=rsi_period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=rsi_period).mean()

    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data


def add_macd(data, fast_ema=12, slow_ema=26, signal_sma=9):
    """Рассчитывает MACD."""
    data['EMA_fast'] = data['Close'].ewm(span=fast_ema, adjust=False).mean()
    data['EMA_slow'] = data['Close'].ewm(span=slow_ema, adjust=False).mean()
    data['MACD'] = data['EMA_fast'] - data['EMA_slow']
    data['Signal'] = data['MACD'].ewm(span=signal_sma, adjust=False).mean()
    return data


def st_dev(data):
    """Стандартное отклонение цены закрытия"""
    data['STDev'] = data['Close'].rolling(20, closed='left').std()
    return data
