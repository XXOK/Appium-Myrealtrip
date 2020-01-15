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
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'production_account.json')


class PaymentValidation(unittest.TestCase):
    def elementReset(self):
        self.driver.press_keycode(187)
        sleep(1)

        self.driver.press_keycode(187)
        sleep(1)

    def setUp(self):

        desired_caps = {}
        desired_caps['app'] = '/Users/yeonshin/Appium-Myrealtrip/apps/app-production-release-550.apk'
        desired_caps['appPackage'] = 'com.mrt.ducati'
        desired_caps['appWaitActivity'] = 'SplashActivity'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'S8'
        desired_caps['udid'] = 'ce081718aa30e13102'
        desired_caps['newCommandTimeout'] = '7200'
        desired_caps['adbExecTimeout'] = '3000'
        desired_caps['androidInstallTimeout'] = '50000'
        desired_caps['noReset'] = 'True'
        desired_caps['autoGrantPermissions']  = 'True'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['autoWebView'] = 'True'

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
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_next'))).click()

        # 두번째 튜토리얼 화면 다음 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_next'))).click()

        # 세번째 튜토리얼 화면 다음 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_next'))).click()

        try:
            # 알림 설정 팝업 나중에 탭
            wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_negative'))).click()

        except:
            pass

        # TODO - 이메일 회원가입

        # 회원 가입 페이지 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://signup', 'package': 'com.mrt.ducati'})

        sleep(3)

        # 이름 입력
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_name'))).send_keys(name)

        # 이메일 주소 입력
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_email'))).send_keys(normal_email)

        # 비밀번호 입력
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_password'))).send_keys(normal_password)

        # 비밀번호 확인 입력
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_password_confirm'))).send_keys(normal_password)

        self.driver.swipe(100, 1600, 100, 150)

        sleep(3)

        # 전체 약관 동의 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/chk_terms_all'))).click()

        # 회원가입 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_signup'))).click()

        # 휴대폰 번호 입력
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_phone_number'))).send_keys(phone)

        # 문자로 인증번호 보내기 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_send'))).click()

        # 인증번호 입력
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_code'))).send_keys(code)

        # 인증하기 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_verify'))).click()

        sleep(5)

        # TODO - 이메일 회원가입 확인

        # 프로필 페이지 진입
        try:
            self.driver.execute_script('mobile: deepLink', {'url': 'mrt://user', 'package': 'com.mrt.ducati'})
        except:
            pass  # adb 자체 오류로 인해 에러 무시

        sleep(3)

        # 이름/이메일 확인
        normal_name = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/txt_user_name'))).text
        normal_id = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/txt_email'))).text

        if normal_name == name:
            pass
        else:
            raise Exception('이메일 회원가입 실패', normal_name, normal_id)

        if normal_id == normal_email:
            pass
        else:
            raise Exception('이메일 회원가입 실패', normal_name, normal_id)

        # TODO - 이메일 로그아웃

        # 설정 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_setting'))).click()

        sleep(2)

        self.driver.swipe(100, 1500, 100, 150)

        sleep(1)

        # 로그아웃 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_logout'))).click()

        sleep(1)

        # TODO - 이메일 로그인

        # 로그인 페이지 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://signin', 'package': 'com.mrt.ducati'})

        sleep(3)

        # 이메일로 로그인 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_email'))).click()

        # 이메일 주소 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText'))).send_keys(normal_email)

        # 비밀번호 입력
        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText'))).send_keys(normal_password)

        # 로그인 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_login'))).click()

        sleep(5)

        # 프로필 페이지 진입
        try:
            self.driver.execute_script('mobile: deepLink', {'url': 'mrt://user', 'package': 'com.mrt.ducati'})
        except:
            pass  # adb 자체 오류로 인해 에러 무시

        sleep(3)

        if normal_name == name:
            pass

        else:
            raise Exception('이메일 로그인 실패', normal_name, normal_id)

        if normal_id == normal_email:

            # 설정 버튼 탭
            wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_setting'))).click()

            sleep(2)

            self.driver.swipe(100, 1500, 100, 150)

            sleep(1)

            # 로그아웃 버튼 탭
            wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_logout'))).click()

            sleep(1)

        else:
            raise Exception('이메일 로그인 실패', normal_name, normal_id)

        # TODO - 페이스북 회원가입

        # 회원 가입 페이지 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://signup', 'package': 'com.mrt.ducati'})

        sleep(3)

        # 페이스북으로 회원가입 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_signup_fb'))).click()

        sleep(3)

        try:
            # 페이스북 이메일 입력
            wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.EditText')))[0].send_keys(facebook_email)

            # 페이스북 비밀번호 입력
            wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.EditText')))[1].send_keys(facebook_password)

            # 로그인 버튼 탭
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'android.widget.Button'))).click()

            # ~님으로 계속 버튼 탭
            wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[1].click()

            sleep(3)

            # 전체 약관 동의 버튼 탭
            wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/chk_terms_all'))).click()

            sleep(2)

            # 회원가입 버튼 탭
            wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_signup'))).click()

            sleep(5)

        except:
            # 계속 버튼 탭
            wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[0].click()

            # 전체 약관 동의 버튼 탭
            wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/chk_terms_all'))).click()

            sleep(2)

            self.driver.swipe(100, 1500, 100, 150)

            sleep(1)

            # 회원가입 버튼 탭
            wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_signup'))).click()

            sleep(5)

        # TODO - 페이스북 회원가입 확인

        # 프로필 페이지 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://user', 'package': 'com.mrt.ducati'})

        sleep(3)

        # 이름/이메일 확인
        facebook_name = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/txt_user_name'))).text
        facebook_id = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/txt_email'))).text

        if facebook_name == 'MRT Kang':
            pass
        else:
            raise Exception('페이스북 회원가입 실패', facebook_name, facebook_id)

        if facebook_id == facebook_email:
            pass
        else:
            raise Exception('페이스북 회원가입 실패', facebook_name, facebook_id)

        # TODO - 페이스북 로그아웃

        # 설정 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_setting'))).click()

        sleep(2)

        self.driver.swipe(100, 1500, 100, 150)

        sleep(1)

        # 로그아웃 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_logout'))).click()

        sleep(1)

        # TODO - 페이스북 로그인

        # 로그인 페이지 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://signin', 'package': 'com.mrt.ducati'})

        sleep(3)

        # 페이스북으로 로그인 버튼 탭
        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_facebook'))).click()

        sleep(2)

        # 계속 버튼 탭
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[0].click()

        sleep(2)

        # 프로필 페이지 진입
        self.driver.execute_script('mobile: deepLink', {'url': 'mrt://user', 'package': 'com.mrt.ducati'})

        sleep(3)

        if facebook_name == 'MRT Kang':
            pass
        else:
            raise Exception('페이스북 회원가입 실패', facebook_name, facebook_id)

        if facebook_id == facebook_email:

            # 설정 버튼 탭
            wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_setting'))).click()

            sleep(2)

            self.driver.swipe(100, 1500, 100, 150)

            sleep(1)

            # 로그아웃 버튼 탭
            wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_logout'))).click()

            sleep(1)

        else:
            raise Exception('페이스북 회원가입 실패', facebook_name, facebook_id)

        # # TODO - 네이버 회원가입
        #
        # # 회원 가입 페이지 진입
        # self.driver.execute_script('mobile: deepLink', {'url': 'mrt://signup', 'package': 'com.mrt.ducati'})
        #
        # sleep(3)
        #
        # # 네이버로 회원가입 버튼 탭
        # wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_signup_naver'))).click()
        #
        # sleep(3)
        #
        # try:
        #     # 이름 입력
        #     wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_name'))).send_keys(name)
        #
        #     # 전체 약관 동의 버튼 탭
        #     wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/chk_terms_all'))).click()
        #
        #     sleep(2)
        #
        #     # 회원가입 버튼 탭
        #     wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_signup'))).click()
        #
        #     sleep(5)
        #
        # except:
        #     try:
        #         # 네이버 로그인 동의 페이지에 위치 하는지 검증
        #         foo = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Image')))[1]
        #
        #         self.driver.swipe(100, 1500, 100, 150)
        #
        #         sleep(1)
        #
        #         # 동의하기 버튼 탭
        #         wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[1].click()
        #
        #         # 이름 입력
        #         wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_name'))).send_keys(name)
        #
        #         # 전체 약관 동의 버튼 탭
        #         wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/chk_terms_all'))).click()
        #
        #         sleep(2)
        #
        #         self.driver.swipe(100, 1500, 100, 150)
        #
        #         sleep(1)
        #
        #         # 회원가입 버튼 탭
        #         wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_signup'))).click()
        #
        #         sleep(5)
        #
        #     except:
        #         # 네이버 이메일 입력
        #         wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.EditText')))[0].send_keys(naver_email)
        #
        #         # 네이버 비밀번호 입력
        #         wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.EditText')))[1].send_keys(naver_password)
        #
        #         # 로그인 상태 유지 버튼 탭
        #         wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'android.widget.CheckBox'))).click()
        #
        #         # 로그인 버튼 탭
        #         wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[2].click()
        #
        #         sleep(3)
        #
        #         self.driver.swipe(100, 1500, 100, 150)
        #
        #         # 동의하기 버튼 탭
        #         wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[1].click()
        #
        #         # 이름 입력
        #         wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/input_name'))).send_keys(name)
        #
        #         # 전체 약관 동의 버튼 탭
        #         wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/chk_terms_all'))).click()
        #
        #         sleep(2)
        #
        #         self.driver.swipe(100, 1500, 100, 150)
        #
        #         sleep(1)
        #
        #         # 회원가입 버튼 탭
        #         wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_signup'))).click()
        #
        #         sleep(5)
        #
        # # TODO - 네이버 회원가입 확인
        #
        # # 프로필 페이지 진입
        # self.driver.execute_script('mobile: deepLink', {'url': 'mrt://user', 'package': 'com.mrt.ducati'})
        #
        # sleep(3)
        #
        # # 이름/이메일 확인
        # naver_name = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/txt_user_name'))).text
        # naver_id = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/txt_email'))).text
        #
        # if naver_name == name:
        #     pass
        # else:
        #     raise Exception('네이버 회원가입 실패', naver_email, naver_id)
        #
        # if  naver_id == naver_email+'@naver.com':
        #     pass
        # else:
        #     raise Exception('네이버 회원가입 실패', naver_email, naver_id)
        #
        # # TODO - 네이버 로그아웃
        #
        # # 설정 버튼 탭
        # wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_setting'))).click()
        #
        # sleep(2)
        #
        # # 로그아웃 버튼 탭
        # wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_logout'))).click()
        #
        # sleep(1)
        #
        # # TODO - 네이버 로그인
        #
        # # 로그인 페이지 진입
        # self.driver.execute_script('mobile: deepLink', {'url': 'mrt://signin', 'package': 'com.mrt.ducati'})
        #
        # sleep(2)
        #
        # # 네이버로 로그인 버튼 탭
        # wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_naver'))).click()
        #
        # sleep(2)
        #
        # # 네이버 로그인 동의 페이지에 위치 하는지 검증
        # foo = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Image')))[1]
        #
        # self.driver.swipe(100, 1500, 100, 150)
        #
        # sleep(2)
        #
        # # 동의하기 버튼 탭
        # wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))[1].click()
        #
        # sleep(5)
        #
        # # 프로필 페이지 진입
        # self.driver.execute_script('mobile: deepLink', {'url': 'mrt://user', 'package': 'com.mrt.ducati'})
        #
        # sleep(3)
        #
        # if naver_name == name:
        #     pass
        # else:
        #     raise Exception('네이버 회원가입 실패', naver_email, naver_id)
        #
        # if  naver_id == naver_email+'@naver.com':
        #     pass
        # else:
        #     raise Exception('네이버 회원가입 실패', naver_email, naver_id)

        # 앱 제거
        self.driver.remove_app('com.mrt.ducati')

    def tearDown(self):
        self.driver.quit()