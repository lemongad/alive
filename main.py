from playwright.sync_api import Playwright, sync_playwright, expect
import random
import time
wait_time = random.randint(10, 60)
sleep_time = random.randint(3, 10)
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    try:
        page.set_default_timeout(30000)
        page.goto("https://cloud.okteto.com/login")
        print("Connect to okteto.com") 
    except Exception:
    # 在发生异常时执行的操作
        print("Connect to oktetois err! skip!")
        pass
    time.sleep(10)
    try:
      with page.expect_popup() as page1_info:
          page.get_by_role("button", name="Log in with GitHub").click()
      time.sleep(10)  
      print("Log in with GitHub")   
      page1 = page1_info.value
      time.sleep(sleep_time)
      page1.get_by_label("Username or email address").click()
      page1.get_by_label("Username or email address").fill("${YONGHU}")
      time.sleep(sleep_time)
      page1.get_by_label("Password").click()
      page1.get_by_label("Password").fill("${PW}")
      time.sleep(sleep_time)
      page1.get_by_role("button", name="Sign in").click()
      time.sleep(10)
      try:
         page1.get_by_role("button", name="Authorize Okteto Cloud").click()
      except Exception:
    # 在发生异常时执行的操作
         print("Authorize Okteto does not exist, skip!")
         pass
      page1.close()
      print("Log in okteto sucessful") 
      time.sleep(sleep_time)
      page.goto("https://cloud.okteto.com/")
      time.sleep(sleep_time)
    except Exception:
    # 在发生异常时执行的操作
        print("oko Sign in is err! skip!")
        pass
    try:
      page.goto("https://cloud.okteto.com/spaces/${YONGHU}")
      time.sleep(sleep_time)
    except Exception:
    # 在发生异常时执行的操作
        print("oko to Deployment is err! skip!")
        pass
    try:
        time.sleep(3)   
        page.get_by_role("button", name="Redeploy").click()
        time.sleep(3)  
        page.get_by_role("button", name="Relaunch").click()
        time.sleep(sleep_time)
        print("Redeploy oko") 
    except Exception:
    # 在发生异常时执行的操作
        print("Redeploy oko  is err!")
        pass
    page2 = context.new_page()
    page2.set_default_timeout(60000)
    try:
        page2.goto("https://webapp.io")
        print("goto webapp")
        time.sleep(sleep_time)
        page2.get_by_role("link", name="Login").click()
        time.sleep(sleep_time)
        print("Login webapp")
        page2.get_by_role("link", name="Log in with GitHub").click()
        time.sleep(2)
    except Exception:
    # 在发生异常时执行的操作
        print("webapp Log in is err!")
        pass
    try:
         page2.get_by_label("Username or email address").click()
         time.sleep(2)
         print("Login email address")
         page2.get_by_label("Username or email address").fill("${YONGHU}")
         page2.get_by_label("Password").click()
         time.sleep(2)
         page2.get_by_label("Password").fill("${PW}")
         print("Login Password")
         page2.get_by_role("button", name="Sign in").click()
         time.sleep(sleep_time)
         print("webapp Log in with GitHub")
    except Exception:
    # 在发生异常时执行的操作
        print("webapp Log in with GitHub is skip!")
        pass
    try:
        element = page2.get_by_text("Authorize")
        element.click()
        print("webapp GitHub Authorize")
    except Exception:
        # 在发生异常时执行的操作
        print("webapp GitHub Authorize is not exsit, skip!")
        pass
    try:
        page2.get_by_role("link", name="Skip Onboarding").click()
        print("Skip Onboarding")
        print("Logged in webapp successfully") 
    except Exception:
    # 在发生异常时执行的操作
        print("Skip Onboarding is err!")
        pass

    time.sleep(sleep_time)
    try:
        page2.goto("https://webapp.io/${YONGHU}/deployments")
        time.sleep(sleep_time)
        element = page2.get_by_text("onwebapp.io")
        element.click()
        print("goto webapp Deployments")
    except Exception:
      # 在发生异常时执行的操作
        print("goto webapp Deployments is err!")
        pass
    try:
        print("goto yourname.onwebapp.io")
        time.sleep(sleep_time)
        page2.get_by_role("button", name="Manual Deploy").click()
        print("Manual Deploy")
        time.sleep(wait_time)
    except Exception:
      # 在发生异常时执行的操作
        print("Manual Deploy is err!")
        pass
    count = 0
    while count < 200:
      count += 1   
      print("第 {} 次保活开始".format(count))
      try:
        page2.bring_to_front()
        time.sleep(sleep_time) 
        page2.goto("https://webapp.io/${YONGHU}/deployments")
        time.sleep(sleep_time)
        element = page2.get_by_text("onwebapp.io")
        element.click()
        print("goto webapp Deployments")
      except Exception:
      # 在发生异常时执行的操作
        print("goto webapp Deployments is err!")
        pass
      try:
        print("goto yourname.onwebapp.io")
        time.sleep(sleep_time)
        page2.get_by_role("button", name="Connect to debugging terminal").click()
        print("Connect to debugging terminal")
        time.sleep(wait_time)
        time.sleep(wait_time)
        time.sleep(wait_time)
      except Exception:
      # 在发生异常时执行的操作
        print("Connect to debugging is err!")
        pass
      try:
        page.bring_to_front()
        time.sleep(sleep_time)
        page.goto("https://cloud.okteto.com/spaces/${YONGHU}")
        time.sleep(sleep_time)
        page.locator(".ResourceListItemParentArrow > .Icon > svg").click()
        time.sleep(sleep_time)
        page.get_by_text("Deployment").click()
        print("oko Deployment")
        time.sleep(sleep_time)
      except Exception:
    # 在发生异常时执行的操作
        print("oko Deployment  is err!")
        pass
      try:
        page.get_by_text("YAML").click()
        time.sleep(wait_time)
        print("oko YAML")
        page.get_by_text("Logs").click()
        time.sleep(wait_time)
        print("oko Logs")
      except Exception:
    # 在发生异常时执行的操作
        print("oko YAML  is err!")
        pass
      page3 = context.new_page() 
      try:
             page3.goto("https://${URL}")
             print("go to ${URL}")
      except Exception:
             pass
      time.sleep(sleep_time) 
      try:
             page3.goto("https://${URL2}")
             print("go to ${URL2}")
      except Exception:
             pass
      time.sleep(sleep_time)
      page3.close() 
      try:
        page2.bring_to_front()
        time.sleep(sleep_time)
        page2.get_by_role("button", name="Disconnect from debugging terminal").click()
        print("Disconnect from debugging terminal")
      except Exception:
      # 在发生异常时执行的操作
        print("Disconnect from debugging terminal is err!")
        pass
      time.sleep(sleep_time)
      print("第 {} 次保活结束".format(count))
    page.close()
    # -------6.1-12:05--------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
      
