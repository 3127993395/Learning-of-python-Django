
import pygame, sys, math
from datetime import datetime


def print_text(font, x, y, text, angle, color=(255, 255, 255)):
    """定义一个用于输出指定位置和角度文本的函数"""
    img_text = font.render(text, True, color)
    img_text = pygame.transform.rotate(img_text, angle)
    screen.blit(img_text, (x, y))

def cycle_text(cirText, bins, today_xx, cirRadius, font):
    """
    定义一个输出循环文本的函数
    cirText: 环形循环文本，如日期和时间的中文
    bins: 圆需要分为多少等分，如秒需要分成60等分
    today_xx: 接收当前时间(月日周时分秒)的具体数值
    cirRadius: 指定环形文本的半径
    font: 指定使用的字体
    """
    for i in range(1, len(cirText) + 1):
        # c_angle: 旋转一次的角度
        c_angle = math.radians(360 / bins)*(today_xx - i)
        # t_angle: 环上每个独立文本的角度
        t_angle = 0 - (360 / bins) * (today_xx - i)
        # add_x: 环上每个独立文本的横坐标距离pos_x的距离
        add_x = math.cos(c_angle)*cirRadius
        # add_x: 环上每个独立文本的横坐标距离pos_x的距离
        add_y = math.sin(c_angle)*cirRadius
        # print_text(): 调用上面定义的函数，输出换上每个文本
        print_text(font, pos_x + add_x, pos_y + add_y, str(cirText[i - 1]), angle=t_angle)


# 初始化一个界面
pygame.init()
# 屏幕大小
screen = pygame.display.set_mode((800, 700))
# 标题
pygame.display.set_caption("Python Clock")

# 月，日，周，时，分，秒字体
font1 = pygame.font.Font("C:/Windows/Fonts/msyh.ttc", 11)
# 年字体
font2 = pygame.font.Font("C:/Windows/Fonts/msyh.ttc", 15)
# 时钟中心
pos_x = 400
pos_y = 330
# 年月日周时分秒对应中文字符
secondsText = ["零一秒","零二秒","零三秒","零四秒","零五秒","零六秒","零七秒","零八秒","零九秒","零十秒","十一秒","十二秒","十三秒",
               "十四秒","十五秒","十六秒","十七秒","十八秒","十九秒","二十秒","二十一秒","二十二秒","二十三秒","二十四秒","二十五秒",
               "二十六秒","二十七秒","二十八秒","二十九秒","三十秒","三十一秒","三十二秒","三十三秒","三十四秒","三十五秒","三十六秒",
               "三十七秒","三十八秒","三十九秒","四十秒","四十一秒","四十二秒","四十三秒","四十四秒","四十五秒","四十六秒","四十七秒",
               "四十八秒","四十九秒","五十秒","五十一秒","五十二秒","五十三秒","五十四秒","五十五秒","五十六秒","五十七秒","五十八秒",
               "五十九秒","零   秒"]
minuteText = ["零一分","零二分","零三分","零四分","零五分","零六分","零七分","零八分","零九分","零十分","十一分","十二分","十三分",
              "十四分","十五分","十六分","十七分","十八分","十九分","二十分","二十一分","二十二分","二十三分","二十四分","二十五分",
              "二十六分","二十七分","二十八分","二十九分","三十分","三十一分","三十二分","三十三分","三十四分","三十五分","三十六分",
              "三十七分","三十八分","三十九分","四十分","四十一分","四十二分","四十三分","四十四分","四十五分","四十六分","四十七分",
              "四十八分","四十九分","五十分","五十一分","五十二分","五十三分","五十四分","五十五分","五十六分","五十七分","五十八分",
              "五十九分","零   分"]
hourText = ["零一点","零两点","零三点","零四点","零五点","零六点","零七点","零八点","零九点","零十点","十一点","十二点",
            "十三点","十四点","十五点","十六点","十七点","十八点","十九点","二十点","二十一点","二十二点","二十三点","零   点"]
weekText = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
dayText = ["零一号","零二号","零三号","零四号","零五号","零六号","零七号","零八号","零九号","十  号","十一号","十二号",
           "十三号","十四号","十五号","十六号","十七号","十八号","十九号","二十号","二十一号","二十二号","二十三号",
           "二十四号","二十五号","二十六号","二十七号","二十八号","二十九号","三十号","三十一号"]
monthText = ["零一月","零二月","零三月","零四月","零五月","零六月","零七月","零八月","零九月","十  月","十一月","十二月"]
# 为了更方便的提取年对应的中文字符，先自动生成一个数字列表，将第2020-2050个元素更换为2020年-2050年对应的中分字符
yearText = list(range(1, 3000))
yearText[2020:2051] = ["二零二零年","二零二一年","二零二二年","二零二三年","二零二四年","二零二五年","二零二六年","二零二七年"
                       ,"二零二八年","二零二九年","二零三零年","二零三一年","二零三二年","二零三三年","二零三四年","二零三五年"
                      ,"二零三六年","二零三七年","二零三八年","二零三九年","二零四零年","二零四一年","二零四二年"
                       ,"二零四三年","二零四四年","二零四五年","二零四六年","二零四七年","二零四八年","二零四九年","二零五零年"]
while True:
    # 鼠标点击x或按下键盘esc键时退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit()
    # 填充背景颜色
    screen.fill("grey11")
    # 绘制一条表明当前日期时间的红线
    pygame.draw.line(screen, color="red", start_pos=(380, pos_y+18), end_pos=(770, pos_y+18),)
    # 获取当前年份
    year = datetime.today().year
    # 输出当前年份
    print_text(font2, pos_x - 20, pos_y, text=yearText[year], angle=0, color="red")
    # 获取当前月份
    months = datetime.today().month
    # 输出月环(会根据月份的变化，顺时针方向旋转，红线处为当前月份)
    cycle_text(cirText=monthText, bins=12, today_xx=months, cirRadius=65, font=font1)
    # 天数这里需要考虑闰年和非闰年以及每月天数不一致的情况
    days = datetime.today().day
    if months in [1,3,5,7,8,10,12]:
        cycle_text(cirText=dayText, bins=31, today_xx=days, cirRadius=118, font=font1)
    elif months in [4,6,9,11]:
        cycle_text(cirText=dayText[0:-1], bins=30, today_xx=days, cirRadius=118, font=font1)
    elif months == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            cycle_text(cirText=dayText[0:-2], bins=29, today_xx=days, cirRadius=118, font=font1)
        else:
            cycle_text(cirText=dayText[0:-3], bins=28, today_xx=days, cirRadius=118, font=font1)
    # 以下周，时，分，秒与月环相似
    weeks = datetime.today().isoweekday()
    cycle_text(cirText=weekText, bins=7, today_xx=weeks, cirRadius=165, font=font1)
    hours = datetime.today().hour % 24
    cycle_text(cirText=hourText, bins=24, today_xx=hours, cirRadius=215, font=font1)
    minutes = datetime.today().minute
    cycle_text(cirText=minuteText, bins=60, today_xx=minutes, cirRadius=270, font=font1)
    seconds = datetime.today().second
    cycle_text(cirText=secondsText, bins=60, today_xx=seconds, cirRadius=325, font=font1)
    # 最后别忘记刷新一下界面
    pygame.display.update()

