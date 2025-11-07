class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})  

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
        
    def transfer(self, amount, category_name):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_name.category}")
            category_name.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount<=self.get_balance()
        #if amount > self.get_balance():
            #return False
        #return True
    
    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    spent = []
    for category in categories:
        total_withdraw = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spent.append(total_withdraw)

    total_spent = sum(spent)

    percentages = [int((s / total_spent) * 100) // 10 * 10 for s in spent]

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "|"
        for p in percentages:
            chart += " o " if p >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_len = max(len(c.category) for c in categories)
    category_names = [c.category.ljust(max_len) for c in categories]

    for i in range(max_len):
        chart += "     "  
        for category_name in category_names:
            chart += category_name[i] + "  "
        if i < max_len - 1:
            chart += "\n"  
    return chart