##資料清洗
data = {
    "寶特瓶":{
        "數量":"number_瓶",
        "地點":"location_瓶",
        "照片":"picture_瓶"},
    "保麗龍":{
        "數量":"number_龍",
        "地點":"location_龍",
        "照片":"picture_龍"},
    "塑膠袋":{
        "數量":"number_袋",
        "地點":"location_袋",
        "照片":"picture_袋"},
    "瓶蓋":{
        "數量":"number_蓋",
        "地點":"location_蓋",
        "照片":"picture_蓋"},
    "免洗餐具":{
        "數量":"number_餐",
        "地點":"location_餐",
        "照片":"picture_餐"},
    "漁業用具":{
        "數量":"number_漁",
        "地點":"location_漁",
        "照片":"picture_漁"},
    "吸管":{
        "數量":"number_管",
        "地點":"location_管",
        "照片":"picture_管"},
    "玻璃瓶":{
        "數量":"number_玻",
        "地點":"location_玻",
        "照片":"picture_玻"},
    "菸蒂":{
        "數量":"number_菸",
        "地點":"location_菸",
        "照片":"picture_菸"}
        }
while True :
    order_list = []
    types = ""
    for a in data :
        order_list.append(a)
    for i in range(len(order_list)) :
        types += "{sequence}. {garbage_name}\n".format(sequence = i+1,garbage_name = order_list[i])
    print(types)
    yn = input("是否在清單上?(y/n)")## 有空可以改良成不須Y/N的版本 ##
    if yn == "y":
        garbage = input(">>>你看到的垃圾(輸入0結束紀錄)<<<")
        if garbage == "":
            continue
        if garbage == str(0) :
            break
        if 0 < int(garbage) <= len(order_list):
            print("ok")## 進入下一階段：開始編輯data ##
            continue
        else :
            print("輸入編號好嗎？臭八七！")
        continue
    if yn == "n":
        garbage = input(">>>你看到的垃圾(輸入0結束紀錄)<<<")
        if garbage == "":
            continue
        if garbage == str(0) :
            break
        else:
            data[garbage] = {"數量":"number_{}","地點":"location_{}","照片":"picture_{}".format(garbage)}
            continue
    else :
        print("輸入y或n好嗎？臭八七！")
print("找時間再淨灘一次吧！")## output階段要改成數據、圖表、地圖... ##