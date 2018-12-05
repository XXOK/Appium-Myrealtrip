# -*- coding: utf-8 -*-

import os
import pdb
import pytest
import unittest
import json
import random
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
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'account1.json')


class PaymentValidation(unittest.TestCase):
    def elementReset(self):
        self.driver.press_keycode(187)
        sleep(1)

        self.driver.press_keycode(187)
        sleep(1)

    def setUp(self):

        desired_caps = {}
        desired_caps['appPackage'] = 'com.mrt.ducati'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'G6'
        desired_caps['fullReset'] = 'true'
        desired_caps['newCommandTimeout'] = '7200'
        desired_caps['udid'] = 'LGMG600Kb3bcdb21'
        desired_caps['app'] = PATH(
            '../apps/app-production-release.apk'
        )

        self.driver = webdriver.Remote('http://10.100.100.220:4722/wd/hub', desired_caps)

    def runTest(self):

        wd = self.driver
        wait = WebDriverWait(wd, 15)

        config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())
        name = config_secret['ACCOUNT']['NAME']
        phone = config_secret['ACCOUNT']['PHONE']
        email = config_secret['ACCOUNT']['EMAIL']
        password = config_secret['ACCOUNT']['PASSWORD']
        wording = config_secret['ACCOUNT']['WORDING']

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

        # TODO.0 뉴나도 페이지 진입

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_nav_tour'))).click()
        # 네비게이션 바 투어&티켓 버튼 탭

        self.elementReset()

        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[1]/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView'))).click()
        # 인기 여행지 첫번째 도시(오사카) 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.a.d[3]/android.widget.TextView'))).click()
        # 카테고리 영역 티켓/교통패스 탭

        # TODO.1 비로그인 상태에서 임의의 상품 구매하기

        random_range = random.randrange(1, 5)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup'+'['+str(random_range)+']'))).click()
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

        # TODO.2 로그인 상태에서 임의의 상품 구매하기

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

        reservation_wording = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]'))).text

        if not reservation_wording == '구매하기':
           raise Exception('구매하기 페이지 문구가 상이하여 테스트를 종료합니다.', '노출되는 문구 :', reservation_wording)

        sleep(1)

    def tearDown(self):
        self.driver.quit()