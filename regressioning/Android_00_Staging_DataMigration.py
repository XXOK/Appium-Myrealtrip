# -*- coding: utf-8 -*-

import os
import pdb
import pytest
import unittest
import json
import random
import sys, traceback
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_SECRET_DIR = os.path.join(BASE_DIR, '.config')
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'staging_account.json')


class PaymentValidation(unittest.TestCase):
    def elementReset(self):
        self.driver.press_keycode(187)
        sleep(1)

        self.driver.press_keycode(187)
        sleep(1)

    def setUp(self):

        desired_caps = {}
        desired_caps['appPackage'] = 'com.mrt.ducati.staging'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8'
        desired_caps['deviceName'] = 'Nexus 5X'
        desired_caps['noReset'] = 'True'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['newCommandTimeout'] = '7200'
        desired_caps['udid'] = '00c90f3bd27532b3'
        desired_caps['app'] = '/Users/yeonshin/Appium-Myrealtrip/apps/app-staging-debug-520.apk'

        self.driver = webdriver.Remote('http://10.60.181.33:4722/wd/hub', desired_caps)

    def runTest(self):

        wd = self.driver
        wait = WebDriverWait(wd, 15)

        config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())
        name = config_secret['ACCOUNT']['NAME']
        phone = config_secret['ACCOUNT']['PHONE']
        wording = config_secret['ACCOUNT']['WORDING']
        code = config_secret['ACCOUNT']['CODE']
        normal_email = config_secret['ACCOUNT']['NORMAL_EMAIL']
        normal_password = config_secret['ACCOUNT']['NORMAL_PASSWORD']
        facebook_email = config_secret['ACCOUNT']['FACEBOOK_EMAIL']
        facebook_password = config_secret['ACCOUNT']['FACEBOOK_PASSWORD']
        naver_email = config_secret['ACCOUNT']['NAVER_EMAIL']
        naver_password = config_secret['ACCOUNT']['NAVER_PASSWORD']
        login_email = config_secret['ACCOUNT']['LOGIN_EMAIL']
        login_password = config_secret['ACCOUNT']['LOGIN_PASSWORD']

        sleep(5)

        # TODO - 튜토리얼 확인

        # 첫번째 튜토리얼 화면 다음 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_next'))).click()

        # 두번째 튜토리얼 화면 다음 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_next'))).click()

        # 세번째 튜토리얼 화면 다음 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_next'))).click()

        try:
            # 알림 설정 팝업 나중에 탭
            wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_negative'))).click()

        except:
            pass

        # TODO - 최근 검색어

        # 검색 바 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/searchbar'))).click()

        # 검색어 입력
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/search_view'))).send_keys('london')

        sleep(1)

        self.elementReset()

        # TODO - 최근 본 여행지

        # 검색 결과 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.TextView'))).click()

        # 여행지 케러셀 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]'))).click()

        # 뒤로가기 버튼 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.ImageButton'))).click()

        # 뒤로가기 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_back'))).click()

        # 뒤로가기 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_back'))).click()

        self.elementReset()

        # # TODO - 최근 검색한 항공권
        #
        # # self.driver.execute_script('mobile: deepLink', {'url': 'mrt://web?url=https%3A%2F%2Fflights.staging-myrealtrip.com%2Fair%2Fb2c%2FAIR%2FMBL%2FAIRMBLSCH0100100010.k1%3Finitform%3DRT%26domintgubun%3DI%26depctycd%3DSEL%26depctycd%3DLAX%26depctycd%3D%26depctycd%3D%26depctynm%3D%25EC%2584%259C%25EC%259A%25B8%26depctynm%3D%25EB%25A1%259C%25EC%258A%25A4%25EC%2595%25A4%25EC%25A0%25A4%25EB%25A0%2588%25EC%258A%25A4%26depctynm%3D%26depctynm%3D%26arrctycd%3DLAX%26arrctycd%3DSEL%26arrctycd%3D%26arrctycd%3D%26arrctynm%3D%25EB%25A1%259C%25EC%258A%25A4%25EC%2595%25A4%25EC%25A0%25A4%25EB%25A0%2588%25EC%258A%25A4%26arrctynm%3D%25EC%2584%259C%25EC%259A%25B8%26arrctynm%3D%26arrctynm%3D%26depdt%3D2019-10-04%26depdt%3D2019-10-09%26depdt%3D%26depdt%3D%26opencase%3DN%26opencase%3DN%26opencase%3DN%26openday%3D%26openday%3D%26openday%3D%26depdomintgbn%3DI%26secrchType%3DFARE%26maxprice%3D%26availcount%3D250%26tasktype%3DB2C%26adtcount%3D1%26chdcount%3D0%26infcount%3D0%26cabinclass%3DY%26nonstop%3DY%26freebag%3D%26orgDepctycd%3D%26orgDepctycd%3D%26orgDepctycd%3D%26orgDepctycd%3D%26orgArrctycd%3D%26orgArrctycd%3D%26orgArrctycd%3D%26orgArrctycd%3D%26orgPreferaircd%3D%26preferaircd%3DKE%26KSESID%3Dair%253Ab2c%253ASELK138RB%253ASELK138RB%253A%253A00', 'package': 'com.mrt.ducati.staging'})
        #
        # # self.driver.execute_script('mobile: deepLink', {'url': 'mrt://flights', 'package': 'com.mrt.ducati.staging'})
        #
        # # 메인 화면 - 항공권 버튼 탭
        # wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_flight'))).click()
        #
        # sleep(5)
        #
        # self.elementReset()
        #
        # # 도착지 선택
        # # wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[3]'))).click()
        # wait.until(EC.visibility_of_element_located((By.ID, 'int_arr_city'))).click()
        #
        # sleep(5)
        #
        # self.elementReset()
        #
        # # 런던 선택
        # wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.widget.GridView/android.view.View[10]/android.view.View[2]/android.view.View'))).click()
        #
        # self.elementReset()
        #
        # # 여행 날짜 선택
        # wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.ListView[2]'))).click()
        #
        # # 출국 날짜 선택
        # wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View/android.widget.GridView[2]/android.view.View[3]/android.view.View[4]'))).click()
        #
        # # 귀국 날짜 선택
        # wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View/android.widget.GridView[2]/android.view.View[4]/android.view.View[4]'))).click()
        #
        # # # 출국 날짜 선택
        # # wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View/android.widget.GridView[1]/android.view.View[4]/android.view.View[5]'))).click()
        # #
        # # # 귀국 날짜 선택
        # # wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View/android.widget.GridView[1]/android.view.View[5]/android.view.View[5]'))).click()
        #
        # # 선택한 날짜 확인
        # wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[4]/android.view.View'))).click()
        #
        # # 항공권 검색 버튼 탭
        # wait.until(EC.visibility_of_element_located((By.ID, 'search'))).click()
        #
        # sleep(1)
        #
        # # 툴바 닫기 버튼 탭
        # wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/menu_close'))).click()
        #
        # # # 시스템 팝업 확인 탭
        # # wait.until(EC.visibility_of_element_located((By.ID, 'android:id/button1'))).click()
        #
        # sleep(1)
        #
        # self.elementReset()

        dummy = 0

        # TODO - 최근 검색한 호텔

        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://accommodations/hotel', 'package': 'com.mrt.ducati.staging'})

        # 여행지 또는 숙소명 검색
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]'))).click()

        # london 검색
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/input_query'))).send_keys('london')

        self.elementReset()

        # 검색 결과 첫번째 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]'))).click()

        # 호텔 검색 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_search'))).click()

        sleep(1)

        # 툴바 뒤로가기 버튼 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton'))).click()

        # TODO - 최근 본 상품

        # 상품 상세화면 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://offers/5047', 'package': 'com.mrt.ducati.staging'})

        sleep(5)

        self.elementReset()

        # TODO - 예약 내역

        # 구매하기 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_reservation'))).click()

        # 이메일로 로그인 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_email'))).click()

        # 이메일 주소 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText'))).send_keys(login_email)

        # 비밀번호 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText'))).send_keys(login_password)

        # 로그인 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_login'))).click()

        sleep(1)

        # 구매하기 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_reservation'))).click()

        sleep(7)

        self.elementReset()

        # 날짜 선택 탭
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'android.widget.EditText'))).click()
        sleep(3)

        # 다음 달 이동 버튼 탭
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.view.View')))[8].click()
        sleep(3)

        # 당일 +30일 날짜 탭
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.view.View')))[60].click()
        sleep(3)

        # 옵션 선택 첫번째 +1 탭
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[1].click()
        sleep(1)

        # 금액 조회하기 버튼 탭
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[2].click()
        sleep(3)

        self.driver.swipe(100, 1500, 100, 150)

        # 구매하기 버튼 탭
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[3].click()
        sleep(3)

        try:
            # 예약 정보 불러오기 팝업 닫기
            wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[0].click()
            sleep(3)

        except:
            pass

        # 구매하기 페이지의 최하단까지 스크롤
        self.driver.swipe(100, 1500, 100, 150)
        sleep(1)

        self.driver.swipe(100, 1500, 100, 150)
        sleep(1)

        self.driver.swipe(100, 1500, 100, 150)
        sleep(1)

        # 여행정보가 최상단에 위치하도록 결제하기 버튼 탭
        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'android.widget.Button'))).click()
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[1].click()

        sleep(3)

        # 여행컨셉 여행 목적 버튼 탭
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Spinner')))[1].click()

        # 여행 목적 '혼자 떠나는 여행' 탭
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.CheckedTextView')))[1].click()

        sleep(1)

        # 결제정보 '무통장 입금' 탭
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.RadioButton')))[2].click()

        sleep(1)

        self.driver.swipe(100, 1500, 100, 150)
        sleep(1)

        # 약관 동의 탭
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'android.widget.CheckBox'))).click()

        # 결제하기 버튼 탭
        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'android.widget.Button'))).click()
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[1].click()

        sleep(5)

        # 전체동의 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[2]'))).click()

        # 은행선택 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View[2]/android.widget.Spinner'))).click()

        # 입금은행 '우리은행' 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[5]'))).click()

        self.elementReset()

        # 다음 버튼 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[6]/android.view.View[2]'))).click()

        sleep(10)

        # TODO - 위시리스트

        # 위시리스트 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://wishlist', 'package': 'com.mrt.ducati.staging'})

        sleep(3)

        # 나라 명
        old_wish_list_title = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.TextView')))[0].text

        # 위시리스트 개수
        old_wish_list_subtitle = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.TextView')))[1].text

        # TODO - 메시지

        # 메시지 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://rooms', 'package': 'com.mrt.ducati.staging'})

        sleep(3)

        old_message_counts = len(wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.ImageView'))))


        # TODO - 앱 업데이트

        # 신규 앱 설치
        self.driver.install_app('/Users/yeonshin/Appium-Myrealtrip/apps/app-staging-debug-521.apk')

        # 앱 실행
        self.driver.launch_app()

        sleep(5)

        try:
            # 알림 설정 팝업 나중에 탭
            wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_negative'))).click()

        except:
            pass

        # TODO - 최근 검색어 확인

        # 검색 바 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/searchbar'))).click()

        recent_search_word = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.support.v7.widget.RecyclerView[1]/android.widget.TextView'))).text

        if recent_search_word == 'london':
            print('최근 검색어 데이터 마이그레이션 완료되었습니다.')
        else:
            raise Exception('업데이트한 앱의 최근 검색어와 기존에 검색했던 검색어가 서로 상이합니다. ', '현재 상단의 노출되는 검색어 :', recent_search_word)

        # 뒤로가기 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_back'))).click()

        # TODO - 최근 본 여행지 확인

        recent_search_destination = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView'))).text

        if recent_search_destination == '런던':
            print('최근 본 여행지 데이터 마이그레이션 완료되었습니다.')
        else:
            raise Exception('업데이트한 앱의 최근 본 여행지와 기존에 검색했던 최근 본 여행지가 서로 상이합니다.')

        # TODO - 최근 검색한 호텔 확인

        # 호텔 홈 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://accommodations/hotel', 'package': 'com.mrt.ducati.staging'})

        sleep(3)

        recent_search_hotel_title = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[1]/android.support.v7.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView[1]'))).text

        if recent_search_hotel_title == 'London':
            print('최근 검색한 호텔 데이터 마이그레이션 완료되었습니다.')
        else:
            raise Exception('업데이트한 앱의 최근 검색한 호텔의 검색어와 기존에 검색했던 최근 검색한 호텔의 검색어가 서로 상이합니다.', '현재 노출되는 호텔 검색어 :', recent_search_hotel_title)

        # 뒤로가기 버튼 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '//android.widget.FrameLayout[@content-desc="숙소"]/android.view.ViewGroup/android.widget.ImageButton'))).click()

        # TODO - 최근 본 상품 확인

        # 최근 본 상품 영역까지 스크롤
        el1 = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_hotel')))
        el2 = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/indicator')))
        self.driver.scroll(el2, el1)
        sleep(1)

        recent_search_item = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[2]'))).text

        if recent_search_item == '파리 바토무슈 E-티켓(바코드) [교환없이 즉시 탑승]':
            print('최근 본 상품 데이터 마이그레이션 완료되었습니다.')
        else:
            raise Exception('업데이트한 앱의 최근 본 상품의 제목과 기존에 검색했던 최근 본 상품의 제목이 서로 상이합니다.', '현재 노출되는 상품 제목 :', recent_search_item)

        # TODO - 예약 내역 확인

        # 예약 내역 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://reservations', 'package': 'com.mrt.ducati.staging'})

        sleep(3)

        recent_search_reservation_status = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/txt_status'))).text

        recent_search_reservation_title = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/txt_title'))).text

        if recent_search_reservation_status + recent_search_reservation_title == '결제 대기파리 바토무슈 E-티켓(바코드) [교환없이 즉시 탑승]':
            print('예약 내역 데이터 마이그레이션 완료되었습니다.')
        else:
            raise Exception('업데이트한 앱의 예약 내역과 기존 예약 내역이 서로 상이합니다.', '현재 최상단에 노출되는 예약내역 :', recent_search_reservation_status + recent_search_reservation_title)

        # TODO - 위시리스트

        # 위시리스트 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://wishlist', 'package': 'com.mrt.ducati.staging'})

        sleep(3)

        # 나라 명
        wish_list_title = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.TextView')))[0].text

        # 위시리스트 개수
        wish_list_subtitle = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.TextView')))[1].text

        if wish_list_title + wish_list_subtitle == old_wish_list_title + old_wish_list_subtitle:
            print('위시리스트 데이터 마이그레이션 완료되었습니다.')
        else:
            raise Exception('업데이트한 앱의 위시리스트와 기존 위시리스트가 서로 상이합니다.', '현재 노출되는 위시리스트 :', wish_list_title + wish_list_subtitle, '대상 : ', old_wish_list_title + old_wish_list_subtitle)

        # TODO - 메시지

        # 메시지 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://rooms', 'package': 'com.mrt.ducati.staging'})

        sleep(3)

        message_counts = len(wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.ImageView'))))

        if message_counts == old_message_counts:
            print('메시지 데이터 마이그레이션 완료되었습니다.')
        else:
            raise Exception('업데이트한 앱의 메시지 개수와 기존 메시지 개수가 서로 상이합니다.', '현재 노출되는 메시지 개수 :', message_counts, '대상 : ', old_message_counts)

        self.driver.remove_app('com.mrt.ducati.staging')

    def tearDown(self):
        self.driver.quit()