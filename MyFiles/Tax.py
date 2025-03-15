# -*- coding: utf-8 -*-
"""
#web.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/ul/div[3]/div/div/div/input').send_keys("其他代扣代缴、代收代缴申报")
#web.find_element(By.XPATH,'//*[@id="drawerMain"]/div/div/div[2]/div[2]/div[2]/div/div[5]/div[2]/div[3]/div/a').click() #Xpath定位代扣代缴页面不可行
web.get("https://etax.zhejiang.chinatax.gov.cn:8443/sbzx/view/lzsfjssb/#/declare/dkdj")
time.sleep(2)
web.find_element(By.XPATH,'/html/body/div[7]/div[2]/div/div/div[3]/div/button[2]').click() #打开代扣代缴页面，“确定”保存上次暂存数据
time.sleep(2)
web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/button').click()  #新建
time.sleep(1)
#/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/button
web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/input').send_keys("FJ3442024090349310")
#FJ3442024090349310,对应公司唯一
time.sleep(0.5)
web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[2]/div/div/form/div[16]/div[2]/div/div/div/input').click()
#空点，等待网页计算税金数
time.sleep(3)
###选项框需激活
web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[2]/div/div/form/div[7]/div[2]/div[1]/div/div/div/div').click() 
time.sleep(1)
web.find_element(By.XPATH,'/html/body/div[8]/div/div/div/ul/li[1]').click()  #选择品目，第一个品目，可尝试构建品目列表
#/html/body/div[8]/div/div/div/ul/li[1]
#/html/body/div[8]/div/div/div/ul/li[2]
time.sleep(1)
web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[2]/div/div/form/div[12]/div[2]/div[1]/div/div/div/div').click() 
time.sleep(0.5)
web.find_element(By.XPATH,'/html/body/div[9]/div/div/div/ul/li[2]').click()#选择代扣代缴、代收代缴项目
#/html/body/div[9]/div/div/div/ul/li[2]/label/span[2]
#/html/body/div[9]/div/div/div/ul/li[2]
#/html/body/div[9]/div/div/div/ul/li[1]/label/span[2]
time.sleep(0.5)
web.find_element(By.XPATH,'//*[@id="Id"]/input').send_keys("123456.01")
#//*[@id="Id"]/input
time.sleep(0.5)
web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[2]/div/div/form/div[16]/div[2]/div/div/div/input').click()
time.sleep(1)
#/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[2]/div/div/form/div[16]/div[2]/div/div/div/input
#空点，等待网页计算税金数
web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[3]/div/button[2]').click()
#/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[3]/div/button[2]
time.sleep(1)
response = web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[1]/div/div[2]/button').click()  #点击暂存
time.sleep(1)
web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[1]/div/div[2]/button').is_enabled()
#/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[1]/div/div[2]/button
"""
#小人头问题处理，下移
"""
slider = web.find_element(By.XPATH,'//*[@id="parent"]/div[1]/div[1]')  # 使用适当的XPath定位滑块  
action = ActionChains(web)  
action.click_and_hold(slider).perform()  # 点击并拖动滑块开始位置  
action.move_by_offset(0, 100).perform()  # 移动到目标位置，需要计算偏移量  
action.release().perform()  # 松开鼠标，完成拖动操作

#web.quit()    #退出浏览器
"""
"""
#征收品目
/html/body/div[8]/div/div/div/ul/li[1]
/html/body/div[8]/div/div/div/ul/li[2]
/html/body/div[8]/div/div/div/ul/li[17]
/html/body/div[9]/div/div/div/ul/li[11]
#扣缴项目
/html/body/div[9]/div/div/div/ul/li[1]
/html/body/div[9]/div/div/div/ul/li[2]
/html/body/div[9]/div/div/div/ul/li[3]
/html/body/div[9]/div/div/div/ul/li[10]
"""



from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
def prepara_data():
    print("进入数据准备模块！")
    try:
        df = pd.read_excel(r"D:\Learn\2025\try.xlsx")
        rows_list = []
        for index, row in df.iterrows():
            rows_list.append(row.tolist())  #将每一行数据作为一个列表，并嵌入到一个列表里面
    
        print("数据准备完成")
    except Exception as e:
        print(e)
        
    return rows_list


def log_in(tax_num ,person_name,person_password):
    print("进入税局登录模块！")
    try:
        ##/html/body/div[7]/div[2]/div/div/div[3]/div/button[2]
        web = Chrome(service =Service(r'D:\Drivers\Chromedriver\chromedriver.exe')) #多次运行会启动多个浏览器，不建议！
        web.maximize_window() 
        web.get("https://tpass.zhejiang.chinatax.gov.cn:8443/#/login?redirect_uri=https%3A%2F%2Fetax.zhejiang.chinatax.gov.cn%3A8443%2Fmhzx%2Fapi%2Fmh%2Ftpass%2Fcode&client_id=tct8zta97w6c46zdt9zc2648227df5z2&response_type=code&state=5f5a31bc9fad49378632d29a25b5599b")
        #web.find_element(By.XPATH,'/html/body/div[2]/section/header/div/div/ul/div/div/span[5]/span').click()
        time.sleep(2)
        web.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/form/div[1]/div/div/div/div[1]/input').send_keys(tax_num)
        web.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/form/div[2]/div/div/div/input').send_keys(person_name)
        web.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/form/div[3]/div[1]/div/div[2]/div/input').send_keys(person_password)
        slider = web.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/form/div[4]/div/div/div/div/div[3]')  # 使用适当的XPath定位滑块  
        action = ActionChains(web)  
        action.click_and_hold(slider).perform()  # 点击并拖动滑块开始位置  
        action.move_by_offset(500, 0).perform()  # 移动到目标位置，需要计算偏移量  
        action.release().perform()  # 松开鼠标，完成拖动操作
        
        web.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/form/div[5]/div/button').click()
        time.sleep(3)
    except Exception as e:
        print(e)
        print("登录失败！")
    return web

def redirect_url(web):
    print("进入跳转代扣代缴界面模块！")
    try:
        web.get("https://etax.zhejiang.chinatax.gov.cn:8443/sbzx/view/lzsfjssb/#/declare/dkdj")
        time.sleep(2)
        #web.find_element(By.XPATH,'/html/body/div[7]/div[2]/div/div/div[3]/div/button[2]').click() #打开代扣代缴页面，“确定”保存上次暂存数据
        #time.sleep(2)
        print("进入代扣代缴申报页面")
    except Exception as e:
        print(e)
        print("跳转代扣代缴页面失败！")
    return web
        
def fill_blank(rows_list,web):
    print("进入将本地数据填入税局模块！")
    done_list = []
    try:   
        for item in rows_list:
            FJ=item[2]
            tax_base=item[8]
            imposed_on_item = item[5]
            deduction_item = item[7]
            web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/button').click()  #新建
            time.sleep(1)
            web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/input').send_keys(FJ)
            web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[2]/div/div/form/div[16]/div[2]/div/div/div/input').click()
            time.sleep(3)
            web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[2]/div/div/form/div[7]/div[2]/div[1]/div/div/div/div').click() 
            time.sleep(2)
            web.find_element(By.XPATH,'/html/body/div[8]/div/div/div/ul/li[{}]'.format(imposed_on_item)).click() #征收品目,品目较多，没办法一次性加载完，会出现找不到元素的情况
            time.sleep(1)
            web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[2]/div/div/form/div[12]/div[2]/div[1]/div/div/div/div').click() 
            time.sleep(0.5)
            web.find_element(By.XPATH,'/html/body/div[9]/div/div/div/ul/li[{}]'.format(deduction_item)).click() #代扣代缴项目
            time.sleep(0.5)
            web.find_element(By.XPATH,'//*[@id="Id"]/input').send_keys(tax_base)   #填入税基
            time.sleep(0.5)
            web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[2]/div/div/form/div[16]/div[2]/div/div/div/input').click()  #空点，激活税局计算税金
            web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div[3]/div/button[2]').click() #点击确认
            print("{},填写完毕！".format(FJ))
            done_list.append(FJ)
            time.sleep(1)
            web.find_element(By.XPATH,'/html/body/section/section/section/main/div/div/div/div[1]/div[2]/div[1]/div/div[2]/button').click()  #点击暂存
            time.sleep(1)
        print("恭喜，填写完毕！")
    except Exception as e:
        print(e)
        print("未填写完成，仅完成{}条！".format(len(done_list)))
    return None



if __name__=="__main__":
    start_time = time.time()
    tax_num = "91330000733796106P"
    person_name = "18595439359"
    person_password = "*ssjssj123"
    rows_list = prepara_data()
    web = log_in(tax_num ,person_name,person_password )
    web = redirect_url(web)
    fill_blank(rows_list,web)
    end_time = time.time()
    print("本次执行公司主体为{}，共耗时{}秒！".format(tax_num,(end_time-start_time)))
    web.quit()
"""
待优化方向：
1、申报属期分为上一期和本期，区分关联公司和非关联公司；
2、循环多家主体；
3、扩张多省税局；
4、校验税金总数，不一定有必要，但是可以考虑。
"""


