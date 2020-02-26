import collections
import re

token = {
    'NUM': r'\d+(\.\d*)?',
    'VAR': r'[A-Za-z_]+',
    'ADD': r'\+',
    'SUB': r'-',
    'MUL': r'\*'
    }

Token = collections.namedtuple('Token', ['type', 'value'])
token_pattern = re.compile('|'.join(f'(?P<{name}>{pattern})'
                                    for name, pattern in token.items()))
expression_pattern = re.compile(
    f'({token["ADD"]}|{token["SUB"]})?({token["NUM"]}|{token["VAR"]})'
    f'(({token["ADD"]}|{token["SUB"]}|{token["MUL"]})'
    f'({token["NUM"]}|{token["VAR"]}))*')
variable_pattern = re.compile(token['VAR'])
space_pattern = re.compile(r'\s')


def get_token(expression):
    scanner = token_pattern.scanner(expression)
    for match in iter(scanner.search, None):
        token = Token(match.lastgroup, match.group())
        yield token


class ExpressionCalculator:
    '''
    Recursive descent parser
    '''
    def __new__(cls, expression, variables={}):
        if not expression_pattern.fullmatch(
                space_pattern.sub('', expression)) or \
                variable_pattern.findall(expression) - variables.keys():
            return False
        return super().__new__(cls)

    def __init__(self, expression, variables={}):
        self._tokens = get_token(expression)
        self._current_token, self._next_token = None, None
        self._variables = variables

    def calc(self):
        self._next()
        return self._get_add_sub_expr()

    def _next(self):
        self._current_token, self._next_token = self._next_token, \
            next(self._tokens, None)

    def _check(self, token_type):
        if self._next_token and self._next_token.type == token_type:
            self._next()
            return True
        else:
            return False

    def _get_atom_expr(self):
        '''
        atom_expr ::= num | var
        '''
        if self._check('NUM'):
            return float(self._current_token.value)
        elif self._check('VAR'):
            return self._variables[self._current_token.value]
        return 0

    def _get_mul_expr(self):
        '''
        mul_expr ::= mul_expr '+' add_sub_expr |
            mul_expr '-' add_sub_expr |
            mul_expr
        '''
        left = self._get_atom_expr()
        while self._check('MUL'):
            right = self._get_atom_expr()
            left *= right
        return left

    def _get_add_sub_expr(self):
        '''
        add_sub_expr ::= atom_expr '*' mul_expr | atom_expr
        '''
        left = self._get_mul_expr()
        while self._check('ADD') or self._check('SUB'):
            current_token_type = self._current_token.type
            right = self._get_mul_expr()
            if current_token_type == 'ADD':
                left += right
            else:
                left -= right
        return left
