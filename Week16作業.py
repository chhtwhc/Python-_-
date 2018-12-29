##資料清洗
import pickle
import os
print("===============【好一個垃圾啊！】===============\n")
see_or_edit = input(">>>看紀錄輸入s、新紀錄輸入e<<<")
if see_or_edit == "s" :
    with open("垃圾資料.pkl", "rb") as f:
        data_history = pickle.load(f)
        most_commom_number_history = 0
        most_commom_item_history = ""
        print("========這是你曾經撿過的垃圾們========")
        for l in range(len(data_history)) :
            detail_item = data_history[l]
            item_history = list(detail_item.keys())[0]
            number_history = data_history[l][item_history]["數量"]
            print("{item_history}：{number_history}個".format(item_history = item_history,number_history = number_history))
            if int(number_history) > most_commom_number_history :
                most_commom_number_history = int(number_history)
                most_commom_item_history = item_history
                continue
            if int(number_history) == most_commom_number_history:
                most_commom_item_history = most_commom_item_history + "、" + item_history
                continue
        print("\n* 你撿過第一名的垃圾是{most_commom_item_history}，數量是{most_commom_number_history}個".format(most_commom_item_history = most_commom_item_history,most_commom_number_history = most_commom_number_history))
if see_or_edit == "e" :
    if os.path.isfile("垃圾資料.pkl") == False :
        data_save =[
            {"寶特瓶":{ ##問題： e 第一次可以成功，s 第一次也可以，可是一但再 e 第二次資料就會被洗掉，變回預設的那個list ##
                "數量":0,
                "地點":"location_瓶",
                "照片":"picture_瓶"}},
            {"保麗龍":{
                "數量":0,
                "地點":"location_龍",
                "照片":"picture_龍"}},
            {"塑膠袋":{
                "數量":0,
                "地點":"location_袋",
                "照片":"picture_袋"}},
            {"瓶蓋":{
                "數量":0,
                "地點":"location_蓋",
                "照片":"picture_蓋"}},
            {"免洗餐具":{
                "數量":"0",
                "地點":"location_餐",
                "照片":"picture_餐"}},
            {"漁業用具":{
                "數量":0,
                "地點":"location_漁",
                "照片":"picture_漁"}},
            {"吸管":{
                "數量":0,
                "地點":"location_管",
                "照片":"picture_管"}},
            {"玻璃瓶":{
                "數量":0,
                "地點":"location_玻",
                "照片":"picture_玻"}},
            {"菸蒂":{
                "數量":0,
                "地點":"location_菸",
                "照片":"picture_菸"}}]
    if os.path.isfile("垃圾資料.pkl") == True :
        with open("垃圾資料.pkl", "rb") as f:
            data_history = pickle.load(f)
            data_save = data_history
    with open("垃圾資料.pkl","wb") as v:
        while True :
            types = ""
            n = 0
            garbage_most = ""
            check = 0
            for i in range(len(data_save)) :
                order = list(data_save[i].keys())
                types += "{sequence}. {garbage_name}\n".format(sequence = i+1,garbage_name = order[0])
            print(types)
            yn = input("是否在清單上?(y/n)")## 有空可以改良成不須Y/N的版本 ##
            if yn == "y":
                garbage = input(">>>你看到的垃圾(輸入0結束紀錄)<<<")
                if garbage == "":
                    continue
                if garbage == str(0) :
                    break
                if 0 < int(garbage) <= len(data_save):
                    item_choose = data_save[int(garbage)-1]
                    for k in item_choose:
                        item_choose[k]["數量"] = int(item_choose[k]["數量"])
                        item_choose[k]["數量"] += 1
                        break
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
                    data_save.append({garbage:{"數量":1,"地點":"location_{}".format(garbage),"照片":"picture_{}".format(garbage)}})
                    continue
            else :
                print("輸入y或n好嗎？臭八七！")
        most_commom_number = 0
        most_commom_item = ""
        for q in range(len(data_save)):
            compare = data_save[q]
            compare_item = list(compare.keys())[0]
            compare_number = data_save[q][compare_item]["數量"]
            if int(compare_number) > most_commom_number :
                most_commom_number = int(compare_number)
                most_commom_item = compare_item
                continue
            if int(compare_number) == most_commom_number:
                most_commom_item = most_commom_item + "、" + compare_item
        print("這次你撿到最多的垃圾是：{item}\n數量是：{number}個".format(item = most_commom_item,number = most_commom_number))
        print("找時間再淨灘一次吧！")## 有時間再加入圖片、圖表、地圖... ##
        data_history = data_save
        pickle.dump(data_history,v)