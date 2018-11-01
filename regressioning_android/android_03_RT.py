# -*- coding: utf-8 -*-

import os
import pdb
import pytest
import unittest
import json
from time import sleep
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_SECRET_DIR = os.path.join(BASE_DIR, '.config')
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'account2.json')


class PaymentValidation(unittest.TestCase):
    def elementReset(self):
        self.driver.press_keycode(187)
        sleep(1)

        self.driver.press_keycode(187)
        sleep(1)

    def setUp(self, reset=False):

        desired_caps = {}
        desired_caps['appPackage'] = 'com.mrt.ducati'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'G5'
        desired_caps['udid'] = '10.100.103.227:5002'
        desired_caps['app'] = PATH(
            '../apps/com.mrt.ducati_2018-09-18.apk'
        )
        # LGF700L3d301c77

        self.driver = webdriver.Remote('http://10.100.100.220:4723/wd/hub', desired_caps)

        if reset == False:
            desired_caps['fullReset'] = False
            desired_caps['noReset'] = True
        return desired_caps

    def runTest(self):
        wd = self.driver
        wait = WebDriverWait(wd, 15)

        config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())
        name = config_secret['ACCOUNT']['NAME']
        phone = config_secret['ACCOUNT']['PHONE']
        email = config_secret['ACCOUNT']['EMAIL']
        password = config_secret['ACCOUNT']['PASSWORD']
        wording = config_secret['ACCOUNT']['WORDING']

        sleep(3)

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_next'))).click()
        # 첫번째 튜토리얼 화면 다음 버튼 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_next'))).click()
        # 두번째 튜토리얼 화면 다음 버튼 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_next'))).click()
        # 세번째 튜토리얼 화면 다음 버튼 탭

        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_positive'))).click()
            # 알림 설정 팝업 동의하기

            self.driver.quit()

            self.setUp()

            self.runTest()
            sleep(5)

        except:
            pass

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/searchbar'))).click()
        # 검색 버튼 탭
        sleep(3)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/search_view'))).click()
        # 검색 텍스트 박스 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/search_view'))).send_keys('osa')
        # 'osa' 입력
        sleep(3)

        region_osaka = wait.until(EC.visibility_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]'))).text
        # 오사카 도시명 워딩 변수 할당

        if not region_osaka == '오사카':
            raise Exception('검색 결과의 나라/도시 이름이 오사카와 상이하여 테스트를 종료합니다.', '노출되는 나라/도시 :', region_osaka)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView[2]'))).click()
        # 여행지 검색 결과 중 첫번째 검색 결과 탭
        sleep(1)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_nav_tour'))).click()
        # 네비게이션 바 투어&티켓 버튼 탭
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.a.d[3]/android.widget.TextView'))).click()
        # 카테고리 영역 티켓/교통패스 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]'))).click()
        # 상품 목록 > 첫번째 상품 탭

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_reservation'))).click()
        # 비로그인 상태에서 구매하기 버튼 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_email'))).click()
        # 이메일로 로그인 버튼 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText'))).click()
        # 이메일 텍스트 박스 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText'))).send_keys(email)
        # 이메일 주소 입력

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText'))).click()
        # 비밀번호 텍스트 박스 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText'))).send_keys(password)
        # 비밀번호 입력

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_login'))).click()
        # 로그인 버튼 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton'))).click()
        # 휴대폰 인증하기 화면 X 버튼 탭(휴대폰 미인증 계정인 경우)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_reservation'))).click()
        # 구매하기 버튼 탭
        sleep(10)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText'))).click()
        # 날짜 선택 셀렉트 박스 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View'))).click()
        # 다음 달 이동 버튼 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.GridView/android.view.View[5]/android.view.View[4]/android.view.View'))).click()
        sleep(1)
        # 당일 +30일 날짜 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[3]/android.widget.Button'))).click()
        # 옵션 선택 첫번째 +1 탭
        sleep(1)

        self.driver.swipe(100, 1000, 100, 150)
        sleep(1)

        self.driver.swipe(100, 1000, 100, 150)
        sleep(1)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'checkPriceBtn'))).click()
        # 금액 조회하기 버튼 탭
        sleep(1)

        self.driver.swipe(100, 1000, 100, 150)
        sleep(1)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.Button'))).click()
        # 구매하기 버튼 탭
        sleep(5)

        count = 0

        while True:
            self.driver.swipe(100, 1000, 100, 150)
            sleep(3)

            if count == 6:
                break

            else:
                count += 1
        # 화면 최하단까지 스크롤

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'reservation-btn'))).click()
        # 결제하기 버튼 탭 (벨리데이션 체크)
        sleep(1)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[4]/android.widget.EditText'))).click()
        # 여행자 연락처 텍스트 박스 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[4]/android.widget.EditText'))).send_keys(phone)
        # 여행자 연락처 입력
        sleep(1)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View[3]/android.widget.Spinner'))).click()
        # 여행컨셉 > 연령대 셀렉트 박스 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]'))).click()
        # 20대 탭

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View[5]/android.widget.Spinner'))).click()
        # 여행컨셉 셀렉트 박스 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]'))).click()
        # 혼자 떠나는 여행 탭
        sleep(1)

        self.elementReset()

        self.driver.swipe(100, 500, 100, 150)
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[4]/android.view.View[3]/android.widget.EditText'))).click()
        # 추가정보 텍스트 박스 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[4]/android.view.View[3]/android.widget.EditText'))).send_keys(wording)
        # 추가정보 텍스트 입력
        sleep(1)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'type-vbank'))).click()
        # 결제정보 무통장 입금 탭

        self.driver.swipe(100, 1000, 100, 150)
        sleep(1)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'checkbox_terms_traveler'))).click()
        # 여행자 약관 동의 버튼 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'reservation-btn'))).click()
        # 결제하기 버튼 탭
        sleep(10)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[2]'))).click()
        # 전체동의 버튼 탭

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'vactBankCode'))).click()
        # 은행 선택 셀렉트 박스 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[5]'))).click()
        # 우리은행 탭

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[4]/android.view.View[2]'))).click()
        # 다음 버튼 탭
        sleep(5)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[4]'))).click()
        # 현금 캐시백 팝업 닫기 버튼 탭

        self.elementReset()

        payment_compelete = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[6]/android.view.View[1]'))).text
        # 결제 완료화면 > 무통장입금 대기 워딩 변수 할당

        if not payment_compelete == '무통장입금 대기':
            raise Exception('무통장입금 결제 완료 화면과 현재 노출 화면이 상이하여 테스트를 종료합니다.', '노출되는 결과 화면 :', payment_compelete)

        count = 0

        while True:
            self.driver.swipe(100, 1000, 100, 150)
            sleep(3)

            if count == 3:
                break

            else:
                count += 1
        # 화면 최하단까지 스크롤

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[6]/android.view.View[7]/android.view.View'))).click()
        # 확인 버튼 탭
        sleep(5)

        self.elementReset()

        landing_page = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[1]'))).text
        # 렌딩 페이지 > 예약내역 워딩 변수 할당

        if not landing_page == '예약내역':
            raise Exception('결제 완료 후 랜딩 페이지가 나의 여행과 상이하여 테스트를 종료합니다.', '노출되는 렌딩 페이지 화면 :', landing_page)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout'))).click()
        # 예약 상품 영역 탭
        sleep(5)

        self.driver.swipe(100, 1000, 100, 150)
        sleep(1)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_cancellation'))).click()
        # 취소 하기 버튼 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_reg'))).click()
        # 등록 버튼 탭

        sleep(1)

    def tearDown(self):
        self.driver.quit()