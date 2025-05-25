# Token class represents the smallest unit of our expression (numbers and operators)
class Token:
    def __init__(self, type_, value):
        self.type = type_    # Type of token (NUMBER, PLUS, MINUS, etc.)
        self.value = value   # Actual value of the token

# Lexer breaks down the input string into tokens
class Lexer:
    def __init__(self, text):
        self.text = text                     # Input string
        self.pos = 0                         # Current position in the text
        self.current_char = self.text[0] if text else None

    def advance(self):
        """Move to the next character in the text"""
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def get_number(self):
        """Get a multi-digit number from the text"""
        number = ''
        while self.current_char and self.current_char.isdigit():
            number += self.current_char
            self.advance()
        return int(number)

    def get_next_token(self):
        """Convert characters into tokens"""
        # Skip spaces
        while self.current_char and self.current_char.isspace():
            self.advance()

        # Return None if we've reached the end
        if not self.current_char:
            return Token('EOF', None)

        # Handle numbers
        if self.current_char.isdigit():
            return Token('NUMBER', self.get_number())

        # Handle operators
        if self.current_char == '+':
            self.advance()
            return Token('PLUS', '+')
        if self.current_char == '-':
            self.advance()
            return Token('MINUS', '-')
        if self.current_char == '*':
            self.advance()
            return Token('MULTIPLY', '*')
        if self.current_char == '/':
            self.advance()
            return Token('DIVIDE', '/')
        if self.current_char == '(':
            self.advance()
            return Token('LPAREN', '(')
        if self.current_char == ')':
            self.advance()
            return Token('RPAREN', ')')

        raise Exception(f'Invalid character: {self.current_char}')

# Parser analyzes the sequence of tokens according to grammar rules
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        """Check if current token matches expected type and advance to next token"""
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f'Expected {token_type} but got {self.current_token.type}')

    def factor(self):
        """Handle numbers, parentheses, and negative numbers"""
        token = self.current_token
        
        # Handle simple numbers
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return token.value
        
        # Handle expressions in parentheses
        if token.type == 'LPAREN':
            self.eat('LPAREN')
            result = self.expr()
            self.eat('RPAREN')
            return result
        
        # Handle negative numbers
        if token.type == 'MINUS':
            self.eat('MINUS')
            return -self.factor()

    def term(self):
        """Handle multiplication and division"""
        result = self.factor()

        # Keep processing * and / operators as long as they appear
        while self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            token = self.current_token
            if token.type == 'MULTIPLY':
                self.eat('MULTIPLY')
                result *= self.factor()
            else:  # DIVIDE
                self.eat('DIVIDE')
                result /= self.factor()

        return result

    def expr(self):
        """Handle addition and subtraction"""
        result = self.term()

        # Keep processing + and - operators as long as they appear
        while self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
                result += self.term()
            else:  # MINUS
                self.eat('MINUS')
                result -= self.term()

        return result

# Main calculator function
def calculate(expression):
    """Calculate the result of a mathematical expression"""
    lexer = Lexer(expression)      # Break expression into tokens
    parser = Parser(lexer)         # Parse the tokens
    return parser.expr()           # Calculate and return the result

# Main program loop
if __name__ == '__main__':
    print('Simple Calculator (type "exit" to quit)')
    print('Examples: "2 + 3 * 4", "(10 - 5) * 3", "-2 + 5"')
    
    while True:
        try:
            # Get input from user
            expression = input('calc> ')
            
            # Check for exit command
            if expression.lower() in ['exit', 'quit']:
                print('Goodbye!')
                break
            
            # Calculate and show result
            result = calculate(expression)
            print(f'Result: {result}')
            
        except Exception as e:
            print(f'Error: {e}')