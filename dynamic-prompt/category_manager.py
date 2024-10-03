import json
from typing import List, Callable, Dict

class CategoryStorage:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> Dict[str, List[str]]:
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save(self, categories: Dict[str, List[str]]) -> None:
        with open(self.file_path, 'w') as f:
            json.dump(categories, f, indent=2)

class ObserverManager:
    def __init__(self):
        self.observers: List[Callable[[], None]] = []

    def add_observer(self, observer: Callable[[], None]) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Callable[[], None]) -> None:
        self.observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer()

class CategoryManager:
    _instance = None

    def __new__(cls, file_path: str):
        if cls._instance is None:
            cls._instance = super(CategoryManager, cls).__new__(cls)
            cls._instance.storage = CategoryStorage(file_path)
            cls._instance.observer_manager = ObserverManager()
            cls._instance.categories = cls._instance.storage.load()
        return cls._instance

    def create_category(self, category_name: str) -> bool:
        if category_name not in self.categories:
            self.categories[category_name] = []
            self._save_changes()
            return True
        return False

    def add_item(self, category_name: str, item: str) -> bool:
        if category_name in self.categories:
            if item not in self.categories[category_name]:
                self.categories[category_name].append(item)
                self._save_changes()
                return True
            else:
                raise ValueError(f"Item '{item}' already exists in category '{category_name}'")
        return False

    def remove_item(self, category_name: str, item: str) -> bool:
        if category_name in self.categories and item in self.categories[category_name]:
            self.categories[category_name].remove(item)
            self._save_changes()
            return True
        return False

    def delete_category(self, category_name: str) -> bool:
        if category_name in self.categories:
            del self.categories[category_name]
            self._save_changes()
            return True
        return False

    def get_category(self, category_name: str) -> List[str]:
        return self.categories.get(category_name, [])

    def get_all_categories(self) -> List[str]:
        return list(self.categories.keys())

    def _save_changes(self) -> None:
        self.storage.save(self.categories)
        self.observer_manager.notify_observers()

    def add_observer(self, observer: Callable[[], None]) -> None:
        self.observer_manager.add_observer(observer)

    def remove_observer(self, observer: Callable[[], None]) -> None:
        self.observer_manager.remove_observer(observer)
