from playwright.sync_api import sync_playwright, Playwright


class Staff:
    def __init__(self,playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()


    def open_page(self):
        self.page.goto('https://www.staff-clothes.com/devushkam/')
        return

    def login(self):
        self.page.get_by_role("banner").get_by_role("button").nth(1).click()
        self.page.locator("form").filter(has_text="Номер телефонуПароль").get_by_label("Номер телефону").click()
        self.page.locator("form").filter(has_text="Номер телефонуПароль").get_by_label("Номер телефону").fill(
            "+380666105081")
        self.page.locator("form").filter(has_text="Номер телефонуПароль").get_by_label("Пароль").fill(
            "ilona5599")
        self.page.get_by_role("button", name="Вхід").first.click()
        return


    def add_product(self):
        self.page.locator('button#list_banner_btn_2').click()
        self.page.get_by_role("link",
                         name="Жіночий спортивний костюм Staff ne milk oversize Жіночий спортивний костюм").click()
        self.page.get_by_role('button', name='XS').click()
        self.page.locator("#order-btn").click()
        self.page.get_by_role("button", name="Перейти до кошика").first.click()
        return


    def logotype(self):
        self.page.locator(".header__logo-container").click()
        self.page.get_by_role("banner").get_by_role("button").first.click()
        return


    def search(self):
        self.page.locator(".search__input").click()
        self.page.get_by_placeholder("Введіть текст для пошуку").fill("Футболка")
        self.page.get_by_placeholder("Введіть текст для пошуку").press("Enter")
        return


    def go_to_catalog(self):
        self.page.get_by_role("banner").get_by_role("link", name="Взуття").click()
        self.page.get_by_role("link", name="Жіночі черевики Staff ce black").click()
        self.page.get_by_role('button', name='37').click()
        return


    def respond(self):
      self.page.get_by_role('button', name='Завантажити ще').click()
      return


    def navigata(self):
        self.page.get_by_role("button", name="Наявність в магазинах").click()
        return

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()








