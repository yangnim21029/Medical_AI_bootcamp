import requests
import json
import math
import csv
import pandas


GOOGLE_API_KEY = "AIzaSyBC9OXMvpGIVJ5FVakJ00oQXEPq9j5E804"
#'放入自己的google api key'

def getDistance(latA, lonA, latB, lonB):
    """
    經緯度計算距離
    單位:公里(km)
    """
    ra = 6378140  # 赤道半徑
    rb = 6356755  # 極半徑
    flatten = (ra - rb) / ra  # Partial rate of the earth
    # change angle to radians
    radLatA = math.radians(latA)
    radLonA = math.radians(lonA)
    radLatB = math.radians(latB)
    radLonB = math.radians(lonB)

    pA = math.atan(rb / ra * math.tan(radLatA))
    pB = math.atan(rb / ra * math.tan(radLatB))
    x = math.acos(math.sin(pA) * math.sin(pB) + math.cos(pA) * math.cos(pB) * math.cos(radLonA - radLonB))
    c1 = (math.sin(x) - x) * (math.sin(pA) + math.sin(pB)) ** 2 / math.cos(x / 2) ** 2
    c2 = (math.sin(x) + x) * (math.sin(pA) - math.sin(pB)) ** 2 / math.sin(x / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (x + dr)
    distance = round(distance / 1000, 4)
    return f'{distance}'

def get_hos_info(lat, lng):
    '''
    '''
    nearby_hospital_list = Nearby_HosID_list(lat, lng)
    hosIDs = [ nearby_hospital_list[i]['place_id'] for i in range(3)]
    return places_Messages(hosIDs)

def Nearby_HosID_list(lat, lng):
    """
    nearbysearch 附近醫院的ID
    :return: 附近醫院的ID列表
    """
    radius = 1000
    keyword = "醫院"

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&types=".format(
        lat=lat, lng=lng, radius=radius) + "&keyword=" + keyword + "&key=" + GOOGLE_API_KEY

    res = requests.get(url)
    hospiatl_nearby_list = json.loads(res.text)
    return hospiatl_nearby_list["results"]


def places_Messages(placeID_list):
    """
    :return: line bubble message
    """
    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []

    for placeID in placeID_list:
        url = "https://maps.googleapis.com/maps/api/place/details/json?&fields=name,formatted_address,rating,formatted_phone_number,geometry&place_id=" +placeID + "&key=" + GOOGLE_API_KEY + "&language=zh_TW"

        res = requests.get(url)
        place_Data = json.loads(res.text)
        formatted_address = place_Data["result"]["formatted_address"]

        try:
            formatted_phone_number = place_Data["result"]["formatted_phone_number"]
        except:
            print("沒有電話")
        try:
            rating = place_Data["result"]["rating"]
        except:
            print("沒有星數")

        hosname = place_Data["result"]["name"]

        jpg_url="https://www.cathay-ins.com.tw/CXIDocs/PF/image/group/PFA1_0540/persona-hospital@2x.png"
        
        bubble ={
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": hosname,
                        "wrap": True
                    }
                ]
            },
            "hero": {
                "type": "image",
                "size": "full",
                "url": jpg_url
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "電話 : " + formatted_phone_number
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": formatted_address,
                        "wrap": True,
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "電話預約",
                            "uri": ""
                        }
                    }
                ]
            }
        }
        bubbles.append(bubble)

    contents['contents']=bubbles
    return 
    

def getTargetClass(lat, lng, class_name):
    '''
    當有語言科別辨識，給予地圖資訊，會經過CSV過濾，回傳 flex
    '''
    # 取得所有醫院名稱和 ID
    csv_file_path = "DepartmentData.csv"
    class_list = None

    with open(csv_file_path, mode='r', encoding='utf-8') as f:
        rows = csv.DictReader(f)
        class_list = [row for row in rows]

    class_list = list(map(lambda x: {'class_name': x['0'], 'compare_hospotal_id': x['1']}, class_list))

    # 詳細醫院資料
    detail_csv_file_path = "hos_df_v2.2.csv"

    detail_list = None

    with open(detail_csv_file_path, mode='r', encoding='utf-8') as f:
        rows = csv.DictReader(f)
        detail_list = list((row) for row in rows)

    detail_list = list(
        map(lambda x: {'Hosp_ID': x['Hosp_ID'], 'Hosp_Name': x['Hosp_Name'], 'Special_Type': x['Special_Type'],
                       'Special_Name': x['Special_Name'], 'Regist_Fee': x['Regist_Fee'],
                       'EM_Regist_Fee': x['EM_Regist_Fee'], 'Fee_Remark': x['Fee_Remark'], 'Address': x['Address'],
                       'Tel_Num': x['Tel_Num'], 'Stars': x['Stars'], 'Comments': x['Comments']}, detail_list))

    # 取得科目對應醫院ID
    filter_class_list = list(filter(lambda x: x['class_name'] == class_name, class_list))
    if(len(filter_class_list)==0):
        # 空 flex
        return emptyContents()
    target_class_list = filter_class_list[0]['compare_hospotal_id'][1:][:-1].split(',')
    target_class_list = list(map(lambda x: x.strip()[1:][:-1], target_class_list))
    
    return target_class_list, detail_list

def hosID_filter(lat, lng, class_name):
    
    target_class_list, detail_list = getTargetClass(lat, lng, class_name)

    # 過濾有缺失值的醫院
    target_detail_list = [detail for detail in detail_list if detail['Hosp_ID'] in target_class_list] 
    
    #用星號和留言量排序
    sort_rating_list = sorted(target_detail_list, key=lambda s: (s['Stars'], s['Comments']), reverse=True) #
    sort_rating_list = list(filter(lambda x: x['Stars'] != '\\N', sort_rating_list))
    target_name_list = list(map(lambda x: x['Hosp_Name'], sort_rating_list))
    
    # 讀取醫院經緯度資料
    location_list = pandas.read_excel('hospital-location.xlsx', engine='openpyxl')
    target_location_list = location_list.loc[location_list['醫院名稱'].isin(target_name_list)].values.tolist()

    # 過濾兩公里之外的醫院
    compare_hospital_list = []
    pickCount = 3
    for location in target_location_list:
        distance = float(getDistance(lat, lng, location[2], location[3]))
        if (distance <= 3 and pickCount != 0):
            print(str(distance) + 'km')
            compare_hospital_list.append(location[1])
            pickCount = pickCount - 1

    #過濾後資料
    filter_hospital_data = list(filter(lambda x: x['Hosp_Name'] in compare_hospital_list, detail_list))
    return filter_hospital_data

def makebubblefromdata(hospital_data):
    #製作line訊息
    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []

    for detail in hospital_data:
        import random
        jpg_url = random.choice(["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT24omhm_NFsqa0H93BCj3CzH1IUHNZ7EinQg&usqp=CAU","https://www.cathay-ins.com.tw/CXIDocs/PF/image/group/PFA1_0540/persona-hospital@2x.png","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVwmNyfhQvLHiju0RIWC14OiM7CoRfiJPheQ&usqp=CAU","https://img.ixintu.com/download/jpg/20200802/a55dba541a20c31c3d7521d8fd1e491a_512_512.jpg!ys"])
        bubble = {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": detail['Hosp_Name'],
                        "wrap": True
                    }
                ]
            },
            "hero": {
                "type": "image",
                "size": "full",
                "url": jpg_url
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "電話 : " + detail['Tel_Num']
                    },
                    {
                        "type": "text",
                        "text": "等級 : " + detail['Special_Name']
                    },
                    {
                        "type": "text",
                        "text": "地址 : " + detail['Address']
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "電話預約",
                            "uri": detail["Tel_Num"]
                        }
                    }
                ]
            }
        }
        bubbles.append(bubble)

    contents['contents']=bubbles
    return contents

def emptyContents():
    return {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIH34HtYbba1FyTgaE6n6pyAd-Y6R7TnGFpQ&usqp=CAU",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "fit",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    },
    "contents": [
      {
        "type": "text",
        "text": "目前無推薦醫院",
        "size": "xl",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": []
      }
    ]
  }
}

def emptyContents():
    return {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIH34HtYbba1FyTgaE6n6pyAd-Y6R7TnGFpQ&usqp=CAU",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "fit",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    },
    "contents": [
      {
        "type": "text",
        "text": "目前無推薦醫院",
        "size": "xl",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": []
      }
    ]
  }
}


if __name__ == '__main__' :
    pass