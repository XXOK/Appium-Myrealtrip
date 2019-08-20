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
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'account_01.json')


class CreateAccount(unittest.TestCase):
    def elementReset(self):
        self.driver.press_keycode(187)
        sleep(1)

        self.driver.press_keycode(187)
        sleep(1)

    def setUp(self):

        desired_caps = {}
        desired_caps['appPackage'] = 'com.mrt.ducati'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'V40'
        desired_caps['fullReset'] = 'true'
        desired_caps['newCommandTimeout'] = '7200'
        desired_caps['udid'] = 'LMV409N1695c8b6'
        desired_caps['app'] = PATH(
            '../apps/myrealtrip.apk'
        )

        self.driver = webdriver.Remote('http://10.60.181.33:4723/wd/hub', desired_caps)

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

        # TODO.0 회원가입 페이지 진입

        wait.until(EC.visibility_of_element_located((By.XPATH, '//android.support.v7.app.a.d[@content-desc="프로필"]'))).click()
        # 네비게이션 바 프로필 버튼 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_signup'))).click()
        # 회원가입 버튼 탭

        # TODO.1 회원정보 입력

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_name'))).send_keys(wording)
        # 이름 입력
        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_email'))).send_keys(email)
        # 이메일 주소 입력
        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_password'))).send_keys(password)
        # 비밀번호 입력
        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_password_confirm'))).send_keys(password)
        # 비밀번호 확인 입력
        self.elementReset()

        self.driver.swipe(100, 1000, 100, 150)
        sleep(1)

        # TODO.2 약관 동의 선택

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/chk_policy_term'))).click()
        # 회원가입 및 운영약관 동의 (필수) 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/chk_privacy_term'))).click()
        # 개인정보 수집 및 이용 동의 (필수) 탭

        # TODO.3 회원가입

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_signup'))).click()
        # 회원가입 버튼 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'android:id/button2'))).click()
        # 마케팅 푸쉬 동의 팝업 > 취소 버튼 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_signup'))).click()
        # 회원가입 버튼 탭

        wait.until(EC.visibility_of_element_located((By.XPATH, '//android.support.v7.app.a.d[@content-desc="이메일 인증"]'))).click()
        # 이메일 인증 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_send'))).click()
        # 인증 이메일 보내기 버튼 탭




    def tearDown(self):
        self.driver.quit()