from pyecharts import Bar

bar = Bar('pername', 'pernamecounter')
bar.add('',['王春雷', '张宇', '张卓琦'], [86, 25, 99],lenged_txt_color='blue')
bar.render("per.html")

