import requests
import json
# 資料來源 : https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx

# 爬蟲要先整合資料型態; 轉為數組為佳

# 主程式
if __name__ == '__main__':
    # 1.取得原始資料
    url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
    source = requests.get(url).text
    print(type(source))  # 型態為str(字串)
    # 2. 將 str字串(此json 資料) 轉成 數組 以利後續 分析
    data = json.loads(source)
    print('資料型態:', type(data))
    print('資料比數:', len(data))  # 有384筆資料
    print('資料內容', data)
    # 3. 決定要使用哪些欄位(此時刪除不要的資料欄位,或是選擇要的資料欄位內容)
    # 此練習需要的欄位: 品名, 廠商名稱, 不合格原因, 行政處分
    bad_rice = []  # 建立新的資料list
    for item in data:   # 每一個列叫做item ,隨便取名子~~
        rice = {}
        rice.setdefault('品名', item['品名'])
        rice.setdefault('廠商名稱', item['廠商名稱'])
        rice.setdefault('不合格原因', item['不合格原因'])
        rice.setdefault('行政處分', item['行政處分'])
        bad_rice.append(rice)
    print('bad_rice:')
    print(bad_rice)
    # 4. 分析資料
    keyword = input('請輸入品名關鍵字: ').strip()  # in case 有白目使用者按太多空白建 LOL
    result = []  # 這裡要有存放空見給之後分析的資料結果
    for item in bad_rice:
        if keyword in item['品名']:
            result.append(item)  # 將輔合的資料存放到result中
    # 5. 輸出分析結果
    print('分析結果:')
    for item in result:
        print(item)
     # 6. 將結果存檔
    if len(result) > 0:  # 資料大於0筆 進行存檔
        file_name = 'result_{0}.txt'.format(keyword)
        file = open('result.txt', 'w', encoding='UTF-8')
         # 將資料逐筆寫入
        for item in result:
            file.write(str(item))   #要記得轉成str字串才能寫入
            file.write('\n')   # 換行用的寫法
        print('寫黨完成')
    else:
        print('查無資料')




# 輸出結果:
# 請輸入品名關鍵字: 池上
# 分析結果:
# {'品名': '池上米-鴻興牌', '廠商名稱': '永興商行', '不合格原因': '品質規格應依規定標示CNS 2等；未標示碾製日期。', '行政處分': '命限期\n改善'}
# 寫黨完成
# {'品名': '池上多力米', '廠商名稱': '池上多力米股份有限公司', '不合格原因': '產品標示之CNS1等，內容物合計被害粒及白粉質粒分析值為11%，超過104.9.23修正公布之白米CNS1等標準(稉型白米最高限度10%)。', '行政處分': '命限期改正'}
# 寫黨完成
# {'品名': '池上特產御饌越光米', '廠商名稱': '德恆商行', '不合格原因': '應標示事項未標示在包袋上，且碾製日期及保存期限未依糧食標示辦法第4條第5款規定，印刷或打印於包袋上。', '行政處分': '命限期改正'}
# 寫黨完成
# {'品名': '池上米', '廠商名稱': '日益實業社', '不合格原因': '包袋未標示碾製日期；且標示產地字體小於0.6公分；被害及白粉質粒分析值16，超過包袋標示CNS二等之標準(稉型白米最高限度15)。', '行政處分': '命限期改正'}
# 寫黨完成