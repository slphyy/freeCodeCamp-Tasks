class Category:
    def __init__(self, name): ## método de inicialização
        self.name = name
        self.ledger = [] ## definindo as instâncias de nome e registro

    def deposit(self, amount, description=''): ## definindo descrição como string vazia no padrã
        self.ledger.append({'amount': amount, 'description': description}) ## fazendo "depósito usando append de um dicionário"

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount): ## verificando na função saque, se o valor sacado não condizer com os fundos, da False 
            return False
        self.ledger.append({'amount': -amount, 'description': description}) ## caso funcione, adiciona o valor negativo e retorna True
        return True

    def get_balance(self):
        balance = 0 ## define o saldo como 0
        for item in self.ledger: ## vai interando os pares valor-chave na liste
            balance += item['amount'] ## e adiciona o valor da chave amount no saldo
        return balance ## e retorno o valor

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {category.name}') ## saca uma X quantidade, usando o método withdraw e deposita em outra conta usando o método deposit
        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance() ## retorna o valor usando o método get_balance e retorna

    def __str__(self): 
        # Title: the category name centered in 30 characters, padded with *
        result = self.name.center(30, '*') + '\n'

        # One line per transaction
        for item in self.ledger:
            # Keep only the first 23 characters of the description
            description = item['description'][:23]
            # Description aligned left (23 wide), amount aligned right (7 wide, 2 decimals)
            result += f"{description:<23}{item['amount']:>7.2f}\n"

        # Last line: the current balance, with no newline at the end
        result += f'Total: {self.get_balance():.2f}'

        # Return the finished text so print() can display it
        return result 


def create_spend_chart(categories):
    # Total spent by each category (one number per category, in the same order)
    spent = []
    for category in categories:
        total = 0
        # Look at every transaction of this category
        for item in category.ledger:
            # Only withdrawals count (they are negative), so flip the sign to add them up
            if item['amount'] < 0:
                total += -item['amount']
        spent.append(total)

    # Total spent across all categories (the 100% reference)
    all_spent = sum(spent)
    # Each category's share, rounded DOWN to a multiple of 10 (27% becomes 20)
    percentages = [int(s * 10 // all_spent) * 10 for s in spent]

    # First line of the chart: the title
    lines = ['Percentage spent by category']

    # One row per level, counting down: 100, 90, ... 0
    for level in range(100, -1, -10):
        # Row label: the level right-aligned in 3 characters, then the | axis
        row = f'{level:>3}|'
        for p in percentages:
            # Draw a bar piece if this category reaches this level, otherwise leave blank space
            row += ' o ' if p >= level else '   '
        # Extra space so the row ends 2 spaces after the last bar
        row += ' '
        lines.append(row)

    # Horizontal line: 3 dashes per category plus 1, starting under the | axis
    lines.append('    ' + '-' * (3 * len(categories) + 1))

    # The longest name decides how many rows are needed for the vertical names
    longest = max(len(c.name) for c in categories)
    # One row per letter position: first letters, then second letters, and so on
    for i in range(longest):
        # Start with 4 spaces so the letters line up under the bars
        row = '    '
        for c in categories:
            # Show this category's i-th letter, or blank space if its name is already finished
            row += f' {c.name[i]} ' if i < len(c.name) else '   '
        # Extra space so every row has the same length
        row += ' '
        lines.append(row)

    # Join all lines with newlines between them (none at the very end) and return the chart
    return '\n'.join(lines)