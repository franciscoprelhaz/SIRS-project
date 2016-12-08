class AuctionItem:
    def increment(self):
        self.price += 10

    def __init__(self, name, initial_price):
        self.name = name
        self.price = initial_price

example_item1 = AuctionItem('Telemovel', 100)
example_item2 = AuctionItem('Computador', 500)

itemList = [example_item1, example_item2]