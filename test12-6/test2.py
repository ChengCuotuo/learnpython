'''
画折线图
'''
from pyecharts import Line

xuexi=['第一学期', '第二学期','第三学期', '第四学期']
wclpaiming=[8, 6, 7, 9]
lspaiming=[5, 5, 2, 1]
line = Line("学习情况", "排名", title_color="red", title_pos="left", width=1200, height=600)
line.add("王春雷", xuexi, wclpaiming,
        mark_point=['max', 'min'],  mark_line=["average"],
        legend_text_color="red", is_label_show=True, is_datazoom_show=True, legend_pos="right",
        is_convert=False, label_pos="inside", is_smooth=True)

line.add("李盛", xuexi, lspaiming,
        mark_point=['max', 'min'],  mark_line=["average"],
        legend_text_color="red", is_label_show=True, is_datazoom_show=True, legend_pos="right",
        is_convert=False, label_pos="inside", is_smooth=True)

line.render('成绩排名比较.html')