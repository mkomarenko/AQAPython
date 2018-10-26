from src.pages.base_page import BasePage


class LogoutPage(BasePage):
    def at_page(self):
        return "Logout - Hillel IT School JIRA" in self.driver.title
