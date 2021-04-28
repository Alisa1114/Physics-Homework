from PIL import Image

import os

print("這是電容式感應的示意圖\n")

os.system('pause')

im1=Image.open('im1.jpg')

im1.show()

print("\n然後這是鋰離子聚合物電池的化學反應式\n")

print("負極：(Carbon-Lix) → C + xLi+ + xe−\n隔膜： Li+ 導電\n正極： Li1−xCoO2 + xLi+ + xe− → LiCoO2\n總反應：(碳-xLi+ + xe−) + Li1-xCoO2 → LiCoO2 + 碳\n")

print("計算電容的關係式如下：\n\tQ=AV/d\n")





