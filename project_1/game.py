import numpy as np


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    # Попытка реализации алгоритма бинарного поиска
    # Счетчик количества попыток
    count = 1
    # Низ, центр, верх интервала
    bot, mid, top = 1, 50, 100
    # Если число = 50 - угадываем с первой попытки и не заходим в цикл
    while number != mid and bot <= top:
      count += 1
      # Если число больше центра текущего интервала
      if number > mid:
        # Делим интервал пополам, переходим в его верхнюю часть
        bot = mid + 1
      else:
        # Иначе, переходим в его нижнюю часть
        top = mid - 1
      # Вычисляем центр нового интервала
      mid = (bot + top) // 2
    
    # Ваш код заканчивается здесь

    return count

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)