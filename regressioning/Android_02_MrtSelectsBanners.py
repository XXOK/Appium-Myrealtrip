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


class MrtSelectsBanners(unittest.TestCase):
    def elementReset(self):
        self.driver.press_keycode(187)
        sleep(1)

        self.driver.press_keycode(187)
        sleep(1)

    def setUp(self):

        desired_caps = {}
        desired_caps['appPackage'] = 'com.mrt.ducati'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'Nexus 5X'
        desired_caps['fullReset'] = 'true'
        desired_caps['newCommandTimeout'] = '7200'
        desired_caps['udid'] = '00c90f3bd27532b3'
        desired_caps['app'] = PATH(
            '../apps/app-production-release.apk'
        )

        self.driver = webdriver.Remote('http://10.60.181.33:4722/wd/hub', desired_caps)

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

        # TODO.0 페이스북 로그인

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.a.d[5]/android.view.ViewGroup/android.widget.ImageView'))).click()
        # 네비게이션 바 프로필 버튼 탭

        wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/btn_facebook'))).click()
        # 페이스북으로 로그인 버튼 탭
        sleep(3)

        try:
            facebook_login_text = wait.until(EC.visibility_of_element_located, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]').text
            if facebook_login_text == '회원님은 이전에 Facebook으로 myrealtrip 앱에 로그인하셨습니다. 계속 이 권한을 유지하시겠어요?':
                wait.until(EC.visibility_of_element_located((By.ID, 'u_0_9'))).click()
                sleep(1)
        except:
            wait.until(EC.visibility_of_element_located((By.ID, 'u_0_3'))).click()
            sleep(1)

        login_user_name = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/txt_user_name'))).text
        # 사용자 이름 변수 할당

        login_user_email = wait.until(EC.visibility_of_element_located((By.ID, 'com.mrt.ducati:id/txt_email'))).text
        # 사용자 이메일 변수 할당

        if not login_user_name == name:
            raise Exception('로그인된 사용자의 이름이 테스트계정과 상이하여 테스트를 종료합니다.', '노출되는 이름 :', login_user_name)

        if not login_user_email == email:
            raise Exception('로그인된 사용자의 이름이 테스트계정과 상이하여 테스트를 종료합니다.', '노출되는 이메일 :', login_user_email)

        # TODO.1 마이리얼트립 Selects - 친구 초대

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.a.d[1]/android.view.ViewGroup'))).click()
        # 네비게이션 바 홈 버튼 탭

        self.driver.swipe(100, 1000, 100, 150)
        sleep(1)

        self.driver.swipe(100, 1000, 100, 150)
        sleep(1)

        self.elementReset()

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]'))).click()
        # 친구 초대 배너 탭

        invitepage_tool_bar = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'))).text
        # 친구 초대 페이지 툴바 문구 변수 할당

        if not invitepage_tool_bar == '친구 초대':
           raise Exception('친구 초대 페이지 툴바 문구가 상이하여 테스트를 종료합니다.', '노출되는 문구 :', invitepage_tool_bar)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageButton'))).click()
        # 뒤로가기 버튼 탭

        # TODO.2 마이리얼트립 Selects - 렌터카

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]'))).click()
        # 렌터카 배너 탭

        rentpage_tool_bar = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView'))).text
        # 렌터카 페이지 툴바 문구 변수 할당

        if not rentpage_tool_bar == '마이리얼트립':
           raise Exception('렌터카 페이지 툴바 문구가 상이하여 테스트를 종료합니다.', '노출되는 문구 :', rentpage_tool_bar)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton'))).click()
        # 뒤로가기 버튼 탭

        # TODO.3 마이리얼트립 Selects - 테마 여행

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[3]'))).click()
        # 테마 여행 배너 탭

        self.elementReset()

        themepage_tool_bar = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView'))).text
        # 테마 여행 페이지 툴바 문구 변수 할당

        if not themepage_tool_bar == '테마 여행':
           raise Exception('테마 여행 페이지 툴바 문구가 상이하여 테스트를 종료합니다.', '노출되는 문구 :', themepage_tool_bar)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton'))).click()
        # 닫기 버튼 탭

        # TODO.4 마이리얼트립 Selects - 여행 체크리스트

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[4]'))).click()
        # 여행 체크리스트 배너 탭

        checklistpage_tool_bar = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView'))).text
        # 여행 체크리스트 페이지 툴바 문구 변수 할당

        if not checklistpage_tool_bar == '마이리얼트립':
           raise Exception('여행 체크리스트 페이지 툴바 문구가 상이하여 테스트를 종료합니다.', '노출되는 문구 :', checklistpage_tool_bar)

        wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton'))).click()
        # 뒤로가기 버튼 탭

    def tearDown(self):
        self.driver.quit()