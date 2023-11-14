# Функция для расчета количества дней в месяце
def days_in_month(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month - 1]


# Ввод данных
year1, month1, day1, hour1, minute1, second1 = map(int, input().split())
year2, month2, day2, hour2, minute2, second2 = map(int, input().split())

# Расчет времени в секундах с начала эры
epoch_start = 0  # Начало эры, можно установить по желанию
seconds_per_day = 24 * 60 * 60
epoch1 = (
        (year1 - epoch_start) * 365 * seconds_per_day +
        sum(days_in_month(year1, m) for m in range(1, month1)) * seconds_per_day +
        (day1 - 1) * seconds_per_day +
        hour1 * 3600 + minute1 * 60 + second1
)
epoch2 = (
        (year2 - epoch_start) * 365 * seconds_per_day +
        sum(days_in_month(year2, m) for m in range(1, month2)) * seconds_per_day +
        (day2 - 1) * seconds_per_day +
        hour2 * 3600 + minute2 * 60 + second2
)

# Разница в секундах между датами
difference_seconds = abs(epoch2 - epoch1)

# Расчет количества дней и секунд в неполном дне
days = difference_seconds // seconds_per_day
seconds_in_incomplete_day = difference_seconds % seconds_per_day

# Вывод результата
print(days, seconds_in_incomplete_day)
