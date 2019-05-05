'''
画出中、日、美、印、巴的在1960、1990、2008、2018年的GDP比较柱状图
'''
from pyecharts import Bar               #画柱状图

chinagbp=[0.3608, 4.6, 13.1735]
japanegdp=[3.13,5.04, 4.3421]
americagdp=[5.98, 14.72, 19.5558]
indiagdp=[0.3166, 1.19, 2.6074]
brazilgdp=[0.4619, 1.7, 1.7592]

bar = Bar("GDP", "Countries", title_color="red", title_pos="right", width=1000, height=500, background_color="blue")

# japanegdp, americagdp, indiagdp, brazilgdp,
years=['1990', '2008', '2018']
bar.add("china", years, chinagbp,
        mark_point=['max', 'min'],  mark_line=["average"],
        legend_text_color="red", is_label_show=True, is_datazoom_show=True, legend_pos="left",
        is_convert=True, label_pos="inside")

bar.add("america", years, americagdp,
        mark_point=['max', 'min'],  mark_line=["average"],
        legend_text_color="red", is_label_show=True, is_datazoom_show=True, legend_pos="left",
        is_convert=True, label_pos="inside")

bar.add("india", years, indiagdp,
        mark_point=['max', 'min'],  mark_line=["average"],
        legend_text_color="red", is_label_show=True, is_datazoom_show=True, legend_pos="left",
        is_convert=True, label_pos="inside")

bar.add("brazil", years, brazilgdp,
        mark_point=['max', 'min'],  mark_line=["average"],
        legend_text_color="red", is_label_show=True, is_datazoom_show=True, legend_pos="left",
        is_convert=True, label_pos="inside")
bar.render("comparegdp.html")