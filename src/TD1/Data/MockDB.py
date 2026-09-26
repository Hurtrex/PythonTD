
from __future__ import annotations
from typing import Optional
from src.TD1.Model import Category

class MockDB:
    _instance: Optional[MockDB] = None

    def __init__(self):
        self.categories = [
            Category(1, "Underweight", 0, 18.5),
            Category(2, "Normal weight", 18.5, 25),
            Category(3, "Overweight", 25, 30)
        ]
        self.categories.append(Category(4, "Obesity", 30, float("inf")))

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MockDB()
        return cls._instance

    @staticmethod
    def get_instance_v2():
        if MockDB._instance is None:
            MockDB._instance = MockDB()
        return MockDB._instance