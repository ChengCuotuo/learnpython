'''
结巴分词
'''
import jieba
s = u'曾经有一份真诚的爱情放在我面前，我没有珍惜，等我失去的时候我才后悔莫及，' \
    u'人世间最痛苦的事莫过于此。如果上天能够给我一个再来一次的机会，' \
    u'我会对那个女孩子说三个字：我爱你。如果非要在这份爱上加上一个期限，' \
    u'我希望是……一万年！'
cut_list = jieba.cut(s)
print('/'.join(cut_list))
'''
曾经/有/一份/真诚/的/爱情/放在/我/面前/，
/我/没有/珍惜/，/等/我/失去/的/时候/我/才/后悔莫及/，
/人世间/最/痛苦/的/事/莫过于此/。
/如果/上天/能够/给/我/一个/再/来/一次/的/机会/，
/我会/对/那个/女孩子/说/三个/字/：/我爱你/。
/如果/非要/在/这份/爱上/加上/一个/期限/，
/我/希望/是/…/…/一万年/！

'''
cut_list = jieba.cut(s, cut_all=True)
print('/'.join(cut_list))
'''
曾经/有/一份/真诚/的/爱情/放在/我/面前///我/没有/珍惜///
等/我/失去/的/时候/我/才/后悔/后悔莫及/莫及///人世/人世间/
世间/最/痛苦/的/事/莫过/莫过于/莫过于此/过于/于此///如果/
上天/能够/给/我/一个/再来/一次/的/机会///我会/对/那个/女孩/
女孩子/孩子/说/三个/字///我爱你///如果/非要/在/这份/爱/上/
加上/一个/期限///我/希望/是////一万/一万年/万年//
'''