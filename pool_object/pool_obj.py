from selenium import webdriver


class DriversPool:

    def __init__(self):

        self.driverpool = [Driver() for _ in range(2)]

    def get_driver(self):
        try:
            if len(self.driverpool) >= 2:
                return self.driverpool.pop(0)
            else:
                self.driverpool.append(Driver())
                return self.driverpool.pop(0)
        finally:
            if len(self.driverpool) == 0:
                self.driverpool.append(Driver())

    def store_driver(self, obj):
        if len(self.driverpool) >= 2:
            obj.__del__()
        else:
            self.driverpool.append(obj)

    def fin(self):
        for x in self.driverpool:
            x.close()
            x.quit()


class Driver:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe', chrome_options=options)
        self.driver.get('about:blank')

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
