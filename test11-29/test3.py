from pyecharts import Pie
pie=Pie('pie')

pie.add('',['王春雷', '张宇', '张卓琦'], [86, 25, 99],Radius=[10,80])
pie.render('prepie.html')
