from selenium import webdriver
from selenium.webdriver.common.by import By
import pyotp
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from omegaconf import OmegaConf
from subprocess import CREATE_NO_WINDOW

env = OmegaConf.load("env.yaml")

options = Options()
options.add_experimental_option('detach', True)

service = Service(env.webdriver_path)
service.creation_flags = CREATE_NO_WINDOW
driver=webdriver.Chrome(service=service, options=options)

driver.get("https://www.cle.osaka-u.ac.jp/")
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id=\"loginsaml\"]").click()

driver.find_element(By.XPATH, "//*[@id=\"USER_ID\"]").send_keys(env.CLE_id)
driver.find_element(By.XPATH, "//*[@id=\"USER_PASSWORD\"]").send_keys(env.CLE_password)
driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/div/input").click()

#MFA認証画面に遷移する場合，tokenを取得
if(driver.current_url=='https://ou-idp.auth.osaka-u.ac.jp/idp/authnPwd'):
    totp=pyotp.TOTP(env.otp_key)
    token = totp.now()
    driver.find_element(By.XPATH, "//*[@id=\"OTP_CODE\"]").send_keys(token)
    driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/table/tbody/tr[7]/td/div/button").click()

if(driver.current_url == "https://ou-idp.auth.osaka-u.ac.jp/idp/otpAuth"):
    driver.find_element(By.XPATH, "/html/body/form/table[2]/tbody/tr[4]/td[1]/input").click()
    driver.find_element(By.XPATH, "//*[@id=\"ok\"]").click()

driver.service.stop()
