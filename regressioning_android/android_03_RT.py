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
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'account1.json')


class SignUp(unittest.TestCase):
    def elementReset(self):
        self.driver.press_keycode(187)
        sleep(1)

        self.driver.press_keycode(187)
        sleep(1)

    def setUp(self, reset=False):

        desired_caps = {}
        desired_caps['appPackage'] = 'com.mrt.ducati'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'Nexus 5X'
        desired_caps['udid'] = '10.100.101.32:5001'
        desired_caps['app'] = PATH(
            '../apps/com.mrt.ducati_2018-09-18.apk'
        )
        # 00c90f3bd27532b3

        self.driver = webdriver.Remote('http://10.100.100.220:4722/wd/hub', desired_caps)

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

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.a.d[5]/android.view.ViewGroup/android.widget.ImageView'))).click()
        # 네비게이션 바 프로필 버튼 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_email'))).click()
        # 이메일로 로그인 버튼 탭

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

        login_user_name = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/txt_user_name'))).text
        # 사용자 이름 변수 할당

        login_user_email = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/txt_email'))).text
        # 사용자 이메일 변수 할당

        if not login_user_name == name:
            raise Exception('로그인된 사용자의 이름이 테스트계정과 상이하여 테스트를 종료합니다.', '노출되는 이름 :', login_user_name)

        if not login_user_email == email:
            raise Exception('로그인된 사용자의 이름이 테스트계정과 상이하여 테스트를 종료합니다.', '노출되는 이메일 :', login_user_email)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.a.d[1]/android.view.ViewGroup'))).click()
        # 네비게이션 바 홈 버튼 탭


    def tearDown(self):
        self.driver.quit()