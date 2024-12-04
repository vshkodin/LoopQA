class Dashboard:
    def __init__(self, page, base_url: str):
        self.page = page
        self.base_url =  base_url

    def navigate_by_text(self, text):
        self.page.locator(f'button:has-text("{text}")').click()

    def verify_task_in_column(self,task, column):
        column_locator = self.page.locator(f"div:has(h2:has-text('{column}'))")
        task_locator = column_locator.locator(f"h3:has-text('{task}')")
        assert task_locator.is_visible(), f"Task '{task}' is not present in the '{column}' column."
        return task_locator

    def verify_tags_in_task(self, webelem, tags):
        # Go to the parent of the task locator
        parent_locator = webelem.locator("..")
        # Locate all children of the parent
        child_elements = parent_locator.locator("*")
        # Count the number of children
        count = child_elements.count()
        # Collect the texts of all child elements
        texts = []
        for i in range(count):
            texts.append(child_elements.nth(i).text_content())
        for tag in tags:
            assert tag in texts