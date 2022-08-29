from selenium import webdriver
import random
import time

option = webdriver.ChromeOptions()
option.add_argument('headless')
url = 'https://www.wenjuan.com/s/nii632x/#'
t = 2
# 设置提交问卷次数
path = r"D:\chrom google\chromedriver_win32\chromedriver.exe"

for times in range(t):
    driver = webdriver.Chrome(executable_path=path, options=option)
    driver.get(url)
    # 定位所有的问卷问题
    questions = driver.find_elements_by_css_selector('.matrix')
    for index, answers in enumerate(questions):

        # 定位所有问卷问题选项
        answer = answers.find_elements_by_css_selector('.icheckbox_div')
        # 定位需要填写文字的选项，并填入相关内容
        if not answer:
            blank_potion = answers.find_element_by_css_selector('.blank.option')
            blank_potion.send_keys('无')
            continue
        # 单选题处理
        if index == 0 or index == 2 or index == 3 or index == 7 or index == 11:
            choose_ans = answer[random.randint(0, 1)]
            choose_ans.click()
            time.sleep(random.randint(0, 1))

        elif index == 5 or index == 6:
            choose_ans = answer[random.randint(0, 2)]
            choose_ans.click()
            time.sleep(random.randint(0, 1))

        elif index == 1:
            choose_ans = answer[random.randint(0, 3)]
            choose_ans.click()
            time.sleep(random.randint(0, 1))
        elif index == 4 or index == 10 or index == 12 or index == 13:
            choose_ans = answer[random.randint(0, 4)]
            choose_ans.click()
            time.sleep(random.randint(0, 1))

        # 多选题处理
        elif index == 8:
            for i in range(1, random.randint(3, 4)):
                choose_ans = answer[random.randint(0, 6)]
                choose_ans.click()
                time.sleep(random.randint(0, 1))


    subumit_button = driver.find_element_by_css_selector('#next_button')
    subumit_button.click()
    print('已经成功提交了{}次问卷'.format(int(times) + int(1)))
    # 延迟问卷结果提交时间，以免间隔时间太短而无法提交
    time.sleep(4)
    driver.quit()

    from selenium import webdriver
    import random
    import time

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    url = 'https://www.wenjuan.com/s/nii632x/#'
    t = 2
    # 设置提交问卷次数
    path = r"D:\chrom google\chromedriver_win32\chromedriver.exe"

    for times in range(t):
        driver = webdriver.Chrome(executable_path=path, options=option)
        driver.get(url)
        # 定位所有的问卷问题
        questions = driver.find_elements_by_css_selector('.matrix')
        for index, answers in enumerate(questions):

            # 定位所有问卷问题选项
            answer = answers.find_elements_by_css_selector('.icheckbox_div')
            # 定位需要填写文字的选项，并填入相关内容
            if not answer:
                blank_potion = answers.find_element_by_css_selector('.blank.option')
                blank_potion.send_keys('无')
                continue
            # 单选题处理
            if index == 0 or index == 2 or index == 3 or index == 7 or index == 11:
                choose_ans = answer[random.randint(0, 1)]
                choose_ans.click()
                time.sleep(random.randint(0, 1))

            elif index == 5 or index == 6:
                choose_ans = answer[random.randint(0, 2)]
                choose_ans.click()
                time.sleep(random.randint(0, 1))

            elif index == 1:
                choose_ans = answer[random.randint(0, 3)]
                choose_ans.click()
                time.sleep(random.randint(0, 1))
            elif index == 4 or index == 10 or index == 12 or index == 13:
                choose_ans = answer[random.randint(0, 4)]
                choose_ans.click()
                time.sleep(random.randint(0, 1))

            # 多选题处理
            elif index == 8:
                for i in range(1, random.randint(3, 4)):
                    choose_ans = answer[random.randint(0, 6)]
                    choose_ans.click()
                    time.sleep(random.randint(0, 1))

        subumit_button = driver.find_element_by_css_selector('#next_button')
        subumit_button.click()
        print('已经成功提交了{}次问卷'.format(int(times) + int(1)))
        # 延迟问卷结果提交时间，以免间隔时间太短而无法提交
        time.sleep(4)
        driver.quit()
