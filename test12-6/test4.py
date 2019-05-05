'''
画地图
pip install echarts-countries-pypkg 世界地图
pip install echarts-china-provinces-pypkg 中国省份地图
pip install echarts-china-cities-pypkg  中国城市地图
Geo城市库，没有导入
'''
from pyecharts import Map

chinagbp=[0.3608, 4.6, 13.1735]
japanegdp=[3.13,5.04, 4.3421]
americagdp=[5.98, 14.72, 19.5558]
indiagdp=[0.3166, 1.19, 2.6074]
brazilgdp=[0.4619, 1.7, 1.7592]

value=[0.3608, 0.4619, 5.98, 3.13]

cou=['China', 'Brazil', 'United States', 'Japan']
map = Map("gdp","", title_color="red", title_pos="left", width=1200, height=600)
map.add("地图", cou, value, maptype="world", is_visualmap=True, visual_text_color="#000")

map.render("MapWorld.html")