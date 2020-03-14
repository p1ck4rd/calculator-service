import calculator


def test_num_expr():
    exp_calc = calculator.ExpressionCalculator('42')
    assert exp_calc.calc() == 42.0


def test_neg_num_expr():
    exp_calc = calculator.ExpressionCalculator('-42')
    assert exp_calc.calc() == -42.0


def test_float_num_expr():
    exp_calc = calculator.ExpressionCalculator('42.23')
    assert exp_calc.calc() == 42.23


def test_var_expr():
    exp_calc = calculator.ExpressionCalculator('x', {'x': 42})
    assert exp_calc.calc() == 42.0


def test_neg_var_expr():
    exp_calc = calculator.ExpressionCalculator('-x', {'x': 42})
    assert exp_calc.calc() == -42.0


def test_missing_var_expr():
    assert calculator.ExpressionCalculator('x') is False


def test_more_var_expr():
    exp_calc = calculator.ExpressionCalculator('42', {'x': 23})
    assert exp_calc.calc() == 42.0


def test_expr_with_spaces():
    exp_calc = calculator.ExpressionCalculator(' 42 ')
    assert exp_calc.calc() == 42.0


def test_add_expr():
    exp_calc = calculator.ExpressionCalculator('x+y', {'x': 42, 'y': 23})
    assert exp_calc.calc() == 65.0


def test_sub_expr():
    exp_calc = calculator.ExpressionCalculator('x-y', {'x': 42, 'y': 23})
    assert exp_calc.calc() == 19.0


def test_mul_expr():
    exp_calc = calculator.ExpressionCalculator('x*y', {'x': 42, 'y': 4})
    assert exp_calc.calc() == 168.0


def test_div_expr():
    expr_calc = calculator.ExpressionCalculator('x/y', {'x': 42, 'y': 4})
    assert expr_calc.calc() == 10.5


def test_add_mul_expr():
    exp_calc = calculator.ExpressionCalculator('x+y*z', {
        'x': 42,
        'y': 23,
        'z': 4
    })
    assert exp_calc.calc() == 134.0


def test_mul_add_expr():
    exp_calc = calculator.ExpressionCalculator('x*y+z', {
        'x': 4,
        'y': 23,
        'z': 42
    })
    assert exp_calc.calc() == 134.0


def test_invalid_expr():
    assert calculator.ExpressionCalculator('x.y', {'x': 42, 'y': 23}) is False
