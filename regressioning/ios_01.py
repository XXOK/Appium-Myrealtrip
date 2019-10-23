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
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_SECRET_DIR = os.path.join(BASE_DIR, '.config')
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'staging_account.json')


class PaymentValidation1(unittest.TestCase):
    def elementReset(self):
        self.driver.press_keycode(187)
        sleep(1)

        self.driver.press_keycode(187)
        sleep(1)

    def setUp(self):

        desired_caps = {}
        desired_caps['bundleId'] = 'com.myrealtrip.traveler.dev'
        desired_caps['platformName'] = 'ios'
        desired_caps['platformVersion'] = '11.4.1'
        desired_caps['deviceName'] = 'iPhone 8'
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['app'] = '/Users/yeonshin/Library/Developer/Xcode/DerivedData/traveler-bdjcyjbwiyeflagvvnuveopuxftj/Build/Products/Debug-iphoneos/MyRealTripTraveler-staging.app'
        desired_caps['udid'] = '319dbb0ed0907c33a70c00996456e0983f265474'
        desired_caps['xcodeOrgId'] = 'EKD5J8G5SA'
        desired_caps['xcodeSigningId'] = 'iPhone Developer'
        desired_caps['fullReset'] = 'false'
        desired_caps['noReset'] = 'true'
        desired_caps['newCommandTimeout'] = 50000

        self.driver = webdriver.Remote('http://10.60.181.33:4723/wd/hub', desired_caps)

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
        wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeButton[@name="다음"]'))).click()

        # 두번째 튜토리얼 화면 다음 버튼 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeButton[@name="다음"]'))).click()

        # 세번째 튜토리얼 화면 시작하기 버튼 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeButton[@name="시작하기"]'))).click()

        sleep(3)

        # 시스템 얼럿 확인 탭
        self.driver.switch_to.alert.accept()

        # 광고 동의 페이지 알림 설정 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeButton[@name="알림 설정"]'))).click()

        # 광고 동의 확인 팝업 확인 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeButton[@name="확인"]'))).click()

        sleep(2)

        # # TODO - 최근 검색어
        #
        # # 검색 바 탭
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeApplication[@name="마이리얼트립D"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther'))).click()
        #
        # # 검색어 입력
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeApplication[@name="마이리얼트립D"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField'))).send_keys('런던')
        #
        # # TODO - 최근 본 여행지
        #
        # # 검색 결과 탭
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeApplication[@name="마이리얼트립D"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]'))).click()
        #
        # sleep(10)
        #
        # # 뒤로가기 버튼 탭
        # TouchAction(self.driver).tap(x=36, y=57).perform()

        # pdb.set_trace()

        # 프로필 버튼 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeApplication[@name="마이리얼트립D"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]'))).click()

        # 회원가입 버튼 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeButton[@name="회원가입"]'))).click()

        # 이름 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeApplication[@name="마이리얼트립D"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeTextField'))).send_keys(name)

        # 이메일 주소 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/XCUIElementTypeApplication[@name="마이리얼트립D"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]/XCUIElementTypeTextField'))).send_keys(normal_email)

        # 비밀번호 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeApplication[@name="마이리얼트립D"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeSecureTextField'))).send_keys(normal_password)

        # 비밀번호 확인 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeApplication[@name="마이리얼트립D"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]/XCUIElementTypeSecureTextField'))).send_keys(normal_password)

        self.driver.swipe(100, 1500, 100, 150)

        # 전체 약관 동의 버튼 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeButton[@name="전체 약관 동의"]'))).click()

        # 회원가입 버튼 탭
        wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeButton[@name="회원가입"]'))).click()

















        # wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeApplication[@name="마이리얼트립D"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[4]'))).click()
        #
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeOther[@name="예약내역 - tab - 4 of 4"]'))).click()
        #
        # self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="프로필 - tab - 5 of 5"]').click()
        #
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeOther[@name="프로필 - tab - 5 of 5"]'))).click()
        #
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeApplication[@name="마이리얼트립D"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]'))).click()
        #
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//XCUIElementTypeButton[@name="여행지나 상품을 검색해보세요."]'))).click()



    def tearDown(self):
        self.driver.quit()