"""Ploty Express 系统自带渐变颜色"""
import plotly.express as px

for key in px.colors.named_colorscales():
    print(key)