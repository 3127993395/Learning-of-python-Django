import csv
from datetime import datetime
import matplotlib.pyplot as plt

import matplotlib

matplotlib.rc("font", family='Microsoft YaHei')

filename = 'F:\pathon\LZY\data_study\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取日期，最高温度和最高温度。
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # 根据最高温度和最低温度绘制图形。
    plt.style.use('Solarize_Light2')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式。
    ax.set_title("2018年每日最高和最低温度", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("温度（F）", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()