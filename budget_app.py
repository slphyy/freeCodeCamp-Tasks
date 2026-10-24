class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        result = self.name.center(30, '*') + '\n'
        for item in self.ledger:
            description = item['description'][:23]
            result += f"{description:<23}{item['amount']:>7.2f}\n"
        result += f'Total: {self.get_balance():.2f}'
        return result


def create_spend_chart(categories):
    spent = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total += -item['amount']
        spent.append(total)

    all_spent = sum(spent)
    percentages = [int(s * 10 // all_spent) * 10 for s in spent]

    lines = ['Percentage spent by category']
    for level in range(100, -1, -10):
        row = f'{level:>3}|'
        for p in percentages:
            row += ' o ' if p >= level else '   '
        row += ' '
        lines.append(row)

    lines.append('    ' + '-' * (3 * len(categories) + 1))

    longest = max(len(c.name) for c in categories)
    for i in range(longest):
        row = '    '
        for c in categories:
            row += f' {c.name[i]} ' if i < len(c.name) else '   '
        row += ' '
        lines.append(row)

    return '\n'.join(lines)