import TencentYoutuyun
import os   #文件路径
from pyecharts import Pie  #画饼状图
appid = '10174324'
secret_id = 'AKIDhkpmyrD8g3HLG47zQii7QdhZGAysKmsv'
secret_key = 'y1UwLZN2gAQcDpiaL1eAgCpcID02wwrB'
userid = '924271966'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT #优图的开方平台
youtu=TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

use_face = 0
not_use_face = 0
base_path="img"
for file_name in os.listdir(base_path):
    result = youtu.DetectFace(os.path.join(base_path, file_name))
    #print(str(result))
    if result['errorcode'] == 0: #是 0 表示是人脸
        use_face += 1
    else:
        not_use_face += 1

attr = ['是人脸', '不是人脸']
vale = [use_face, not_use_face]
pie = Pie("微信好友头像使用人脸比例", title_pos="left")
pie.add("", attr, vale, radius=[30, 60], is_random=False, label_text_size=20,
        is_label_show=True, is_lengend_show=True)
pie.show_config()
pie.render("好友头像人像比例.html")

