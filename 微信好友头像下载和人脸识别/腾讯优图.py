import TencentYoutuyun
import os   #文件路径
import re

appid = '10174324'
secret_id = 'AKIDhkpmyrD8g3HLG47zQii7QdhZGAysKmsv'
secret_key = 'y1UwLZN2gAQcDpiaL1eAgCpcID02wwrB'
userid = '924271966'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT #优图的开方平台
youtu=TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

use_face = 0;
base_path="headimage"
print("照片的名称，性别，年龄，颜值")
pattern = re.compile(r'[a-zA-Z]{3,}');
find = []
for file_name in os.listdir(base_path):
    result = youtu.DetectFace(os.path.join(base_path, file_name))
    find += pattern.findall(str(result))
    find = list(set(find))
    print(find)
    '''
    if result['errorcode'] == 0: #是 0 表示是人脸
        use_face += 1
        gender='男' if result['face'][0]['gender'] >= 50 else '女'
        age = result['face'][0]['age']   #年龄
        beauty = result['face'][0]['beauty'] #颜值
        print(file_name[:-4], gender, age, beauty, sep=',') #用 , 间隔
    '''

#print(find)
'''
['glasses', 'nose', 'shape', 'mouth', 'profile', 'eye', 'gender', 'errorcode', 
'pitch', 'eyebrow', 'session', 'age', 'left', 'pupil', 'roll', 'width', 'height', 
'image', 'FAILED', 'glass', 'right', 'mask', 'IMAGE', 'SDK', 'hat', 'errormsg', 
'face', 'True', 'expression', 'yaw', 'beauty', 'False', 'FACEDETECT']
'''