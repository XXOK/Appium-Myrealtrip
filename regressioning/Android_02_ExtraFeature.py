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
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'G5'
        desired_caps['noReset'] = 'True'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['newCommandTimeout'] = '7200'
        desired_caps['udid'] = 'LGF700L3d301c77'
        desired_caps['app'] = '/Users/yeonshin/Appium-Myrealtrip/apps/app-staging-debug-521.apk'

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

        # TODO - 이메일 계정 로그인

        # 로그인 페이지 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://signin', 'package': 'com.mrt.ducati.staging'})

        sleep(3)

        # 이메일로 로그인 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_email'))).click()

        # 이메일 주소 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText'))).send_keys(login_email)

        # 비밀번호 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText'))).send_keys(login_password)

        # 로그인 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_login'))).click()

        sleep(1)

        # TODO - 비밀번호 변경

        # 프로필 페이지 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://user', 'package': 'com.mrt.ducati.staging'})

        sleep(3)

        # 설정 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_setting'))).click()

        # 비밀번호 변경 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/layout_password'))).click()

        # 새 비밀번호 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText'))).send_keys('000000')

        # 비밀번호 확인 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText'))).send_keys('000000')

        # 완료 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_done'))).click()

        sleep(2)

        # TODO - 비밀번호 변경 확인

        self.driver.swipe(100, 1500, 100, 150)

        sleep(1)

        # 로그아웃 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_logout'))).click()

        sleep(1)

        # 로그인 페이지 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://signin', 'package': 'com.mrt.ducati.staging'})

        sleep(3)

        # 이메일로 로그인 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_email'))).click()

        # 이메일 주소 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText'))).send_keys(login_email)

        # 비밀번호 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText'))).send_keys('000000')

        # 로그인 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_login'))).click()

        sleep(1)

        # TODO - 비밀번호 재변경

        # 프로필 페이지 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://user', 'package': 'com.mrt.ducati.staging'})

        sleep(3)

        # 설정 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_setting'))).click()

        # 비밀번호 변경 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/layout_password'))).click()

        # 새 비밀번호 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText'))).send_keys(login_password)

        # 비밀번호 확인 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText'))).send_keys(login_password)

        # 완료 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati.staging:id/btn_done'))).click()

        sleep(1)

        # 앱 제거
        self.driver.remove_app('com.mrt.ducati.staging')

    def tearDown(self):
        self.driver.quit()