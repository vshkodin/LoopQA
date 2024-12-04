class Auth:
    def __init__(self, page, base_url: str, username: str, password: str ):
        self.page = page
        self.username = username
        self.password = password
        self.base_url = base_url
        # locators
        self.field_username = '[id="username"]'
        self.field_password = '[id="password"]'
        self.button_submit = '[type="submit"]'
        # locators by text
        self.button_logout = 'Logout'
        self.text = 'Web Application'

    def auth_user(self):
        self.page.goto(self.base_url)
        self.page.fill(self.field_username, self.username)
        self.page.fill(self.field_password, self.password)
        self.page.click(self.button_submit)
        assert  self.page.is_visible("text=Web Application"), "Web Application text is not visible on the page."

    def logout(self):
        self.page.locator(f'text="{self.button_logout}"').click()
        assert self.page.is_visible("text=Project Board Login")
