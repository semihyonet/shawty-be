from beanie import Document


class CounterModel(Document):
    name: str
    counter: int
