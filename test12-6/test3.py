'''
画水滴图
'''
from pyecharts import Liquid

lq = Liquid("水滴图","", title_color="blue", title_pos="center")
lq.add("饭量", [0.3, 0.5, 0.2], is_liquid_outline_show=True, is_liquid_animation=True,
         shape="diamond")  #形状

lq .render('水滴.html')