class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.total = 0

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.total = self.total + amount

    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False
        self.deposit(-amount, description)
        return True
        
    def get_balance(self):
        return self.total

    def transfer(self, amount, other):
        if not self.withdraw(amount, 'Transfer to %s' % (other.category)):
            return False
        other.deposit(amount, 'Transfer from %s' % (self.category))
        return True
        
    def check_funds(self, amount):
        return amount <= self.total

    def __str__(self):
        descriptionWidth = 23
        width = descriptionWidth + 7
        selfStr = self.category.center(width, "*")
        selfStr = selfStr + ("\n")
        for item in self.ledger:
            amountPart = '%7.2f' % item["amount"]
            descriptionPart = item["description"][0:descriptionWidth].ljust(descriptionWidth, " ")
            selfStr = selfStr + (descriptionPart + amountPart + "\n")
        selfStr = selfStr + ("Total: " + str(self.total))
        return selfStr

    def get_withdraws_total(self):
        withdrawals = list(filter(lambda i: i["amount"] < 0, self.ledger))
        total = 0
        for w in withdrawals:
            total += w["amount"]
        return total

class Chart:
    def __init__(self, categories):
        self.total = 0
        for c in categories:
            self.total += c.get_withdraws_total()
        self.data = []
        for c in categories:
            perc = int(c.get_withdraws_total() * 100 / self.total)
            percRounded = (perc - (perc % 10)) // 10
            self.data.append(
              {
                "category": c.category,
                "percentage": percRounded
              }
            )
        self.maxLabelLength = 0
        for perc in self.data:
            if len(perc["category"]) > self.maxLabelLength:
                self.maxLabelLength = len(perc["category"])

    def _get_bars_with_labels(self):
        dataStr = map(
          lambda d: {
            "category": d["category"].ljust(self.maxLabelLength, " "), "percentage":((d["percentage"] + 1) * "o").rjust(11, " ")
          },
           self.data)
        return map(lambda ds: "%s-%s" % (ds["percentage"], ds["category"]), dataStr)

    def _get_empty_bar(self):
        return (" " * 11) + "-" + (" " * self.maxLabelLength)

    def plot_bar_chart(self):
        title = "Percentage spent by category\n"
        yAxys = ["1           ", "0987654321  ", "00000000000 ", "||||||||||| "]
        yAxys = map(lambda s: s + " " * self.maxLabelLength, yAxys)
        bars_with_labels = self._get_bars_with_labels()

        lines = [*yAxys, self._get_empty_bar()]
        for v in bars_with_labels:
            lines.append(v)
            lines.append(self._get_empty_bar())
            lines.append(self._get_empty_bar())

        chart = title
        for i in range(len(lines[0])):
            for line in lines:
                chart += line[i]
            chart += "\n"
        chart = chart[:-1]

        return chart

def create_spend_chart(categories):
    chart = Chart(categories)
    return chart.plot_bar_chart()