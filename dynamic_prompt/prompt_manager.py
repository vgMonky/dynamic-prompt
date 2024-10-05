import re
import random
from typing import List
from .category_manager import CategoryManager

class PromptManager:
    def __init__(self, category_manager: CategoryManager):
        self.category_manager = category_manager

    def process_prompt(self, prompt: str) -> str:
        def replace_category(match):
            category = match.group(1)
            items = self.category_manager.get_category(category)
            return random.choice(items) if items else match.group(0)

        pattern = r'\{\{(\w+)\}\}'
        return re.sub(pattern, replace_category, prompt)

    def process_template_prompt(self, template: str) -> str:
        return self.process_prompt(template)
