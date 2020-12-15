class Bonus:
    rulesPercentDiscount = [
        {"max": 1000, "min": 0, "discount": 10},
        {"max": 1500, "min": 1000, "discount": 15},
        {"max": 100000, "min": 1500, "discount": 20}
    ]

    def getPercentBonus(self, value):
        item = [x["discount"] for x in self.rulesPercentDiscount if value >= x["min"] and value <= x["max"]]
        return item[0]

    def getGroupToCalcPercente(self, order):
        return str(order['date'].year) + "_" + str(order['date'].month)