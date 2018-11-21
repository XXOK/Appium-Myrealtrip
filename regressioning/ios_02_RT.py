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


class PaymentValidation2(unittest.TestCase):
    def elementReset(self):
        self.driver.press_keycode(187)
        sleep(1)

        self.driver.press_keycode(187)
        sleep(1)

    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'ios'
        desired_caps['platformVersion'] = '12.1'
        desired_caps['deviceName'] = 'iPhone'
        desired_caps['noReset'] = 'true'
        desired_caps['newCommandTimeout'] = '7200'
        desired_caps['bundleId'] = 'com.mrt.ducati'
        desired_caps['udid'] = 'A2E10077-6EBE-402F-80A6-2A72E56964E0'
        desired_caps['app'] = PATH(
            '/Users/yeonshin/Appium-Myrealtrip/apps/MyRealTripTraveler.app'
        )

        self.driver = webdriver.Remote('http://10.100.100.220:4724/wd/hub', desired_caps)

    def runTest(self):
        wd = self.driver
        wait = WebDriverWait(wd, 15)

        config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())
        name = config_secret['ACCOUNT']['NAME']
        phone = config_secret['ACCOUNT']['PHONE']
        email = config_secret['ACCOUNT']['EMAIL']
        password = config_secret['ACCOUNT']['PASSWORD']
        wording = config_secret['ACCOUNT']['WORDING']

        pass

    def tearDown(self):
        self.driver.quit()