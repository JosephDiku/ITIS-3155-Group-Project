from sandwiches import Sandwich
from typing import Dict

class sandwich_db:
    def __init__(self):
        self.data: Dict[int, Sandwich] = {}

    def get_sandwich(self, id: int) -> Sandwich:
        return self.data.get(id)

    def add_sandwich(self, sandwich: Sandwich) -> Sandwich:
        #check if the sandwich id already exists
        if sandwich.id in self.data:
            raise ValueError("Sandwich with this ID already exists")
        #add the new sandwich to the database
        self.data[sandwich.id] = sandwich
        return sandwich

db = sandwich_db()

db.data = {
    1: Sandwich(id=1, sandwich_name="Turkey", price=2.75, calories=275, ingredients=""),
    2: Sandwich(id=2, sandwich_name="Ham", price=2.75, calories=250, ingredients=""),
    3: Sandwich(id=3, sandwich_name="Ruben", price=3.00, calories=350, ingredients=""),
    4: Sandwich(id=4, sandwich_name="Philly", price=4.00, calories=600, ingredients=""),
    5: Sandwich(id=5, sandwich_name="Bologna", price=2.75, calories=225, ingredients=""),
    6: Sandwich(id=6, sandwich_name="PB&J", price=2.50, calories=200, ingredients=""),
}