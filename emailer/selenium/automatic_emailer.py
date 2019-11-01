def send_email(name, email, subject, message, cc=[]):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.actions import key_actions, key_input
    from selenium.webdriver.common.action_chains import ActionChains
    import time

    driver_path = r'C:\Users\Charlie\Google Drive\data science\class files\Data Analysis with Python\Selenium Practice/chromedriver.exe'
    staff = {
        'LukeLin': "luke.lin@nycdatascience.com",
        'SimonZhong':"xiangwei.zhong@nycdatascience.com"
    }


    def open_gmail(drv):
        # Open and Login
        drv = webdriver.Chrome(driver_path)
        drv.set_window_size(700, 1000)
        drv.get('https://gmail.com')
        ActionChains(drv) \
            .pause(0.5) \
            .send_keys('charles.cohen@nycdatascience.com') \
            .pause(0.5) \
            .send_keys(Keys.ENTER) \
            .perform()
        time.sleep(1)
        ActionChains(drv) \
            .pause(0.5) \
            .send_keys('masterunitylegion') \
            .pause(0.5) \
            .send_keys(Keys.ENTER) \
            .perform()


    def reset_to_inbox(drv):
        ActionChains(drv).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('d').key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()


    def write_email(drv, name, email, subject, message, cc=[]):
        time.sleep(2)
        def ctrl_shift(key, modA, modB=None):
            return ActionChains(drv) \
                .key_down(modA).key_down(modB) \
                .pause(0.5) \
                .send_keys(key) \
                .pause(0.5) \
                .key_up(modA).key_up(modB) \
                .perform()
        
        
        body = drv.find_element_by_tag_name('body')
        
        #Open Compose Box
        ActionChains(drv).send_keys('c').perform()
        
        #Add To Contact
        ActionChains(drv).send_keys(email).perform()
        
        #Add CC Contact
        if cc != []:
            ctrl_shift('c', Keys.CONTROL, Keys.SHIFT)
            for contact in cc:
                ActionChains(drv).send_keys(contact).send_keys(' ').perform()
        
        #Add Subject
        ActionChains(drv).send_keys(Keys.TAB).pause(0.5).perform()
        ActionChains(drv).send_keys(Keys.TAB).pause(0.5).perform()
        ActionChains(drv).send_keys(subject).pause(0.5).perform()
        
        #Add Message
        ActionChains(drv).send_keys(Keys.TAB).pause(0.5).perform()
        ActionChains(drv).send_keys(message).pause(0.5).perform()

        #Send Message
        #ctrl_shift('', Keys.CONTROL, Keys.ENTER)
        
        print(f'Email to: {email} sent successfully!!')



