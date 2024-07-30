import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\admin\\PycharmProjects\\Indiconnect\\Configration\\config.ini")
# config.read(".\\Configration\\config.ini")


class ReadconfigClass:

    @staticmethod
    def getURL():
        URL = config.get('login data', 'URL')
        return URL

    @staticmethod
    def getUsername():
        Username = config.get('login data', 'Username')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'Password')
        return Password

    # @staticmethod
    # def getLogin_button():
    #     login_button = config.get('login data', 'login_button')
    #     return login_button

    @staticmethod
    def getotp():
        read_otp = config.get('login data', 'otp')
        return read_otp

    # @staticmethod
    # def getSbmitButton():
    #     submit_button = config.get('login data', 'submit_button')
    #     return submit_button
    # #
    # # @staticmethod
    # # def getMenuButton():
    # #     MenuButton = config.get('login data', 'MenuButton')
    # #     return MenuButton
    # #
    # # @staticmethod
    # # def getLogoutButton():
    # #     logoutButton = config.get('login data', 'logoutButton')
    # #     return logoutButton
    # #
    # # # @staticmethod
    # # # def getSbmitButton():
    # # #     submit_button = config.get('login data', 'submit_button')
    # # #     return submit_button
