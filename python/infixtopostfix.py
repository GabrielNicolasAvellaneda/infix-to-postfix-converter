import unittest
import string

def infix_to_postfix(infix_expression):
    result = []
    operators_stack = []
    operators = "+-/*"
    for token in infix_expression.split():
        if token in "+-":
            while len(operators_stack) > 0 and operators_stack[-1] in "*/":
                result.append(operators_stack.pop())
            operators_stack.append(token)
        elif token in "*":
            while len(operators_stack) > 0 and operators_stack[-1] in "/":
                result.append(operators_stack.pop())
            operators_stack.append(token)
        elif token in "/":
            operators_stack.append(token)
        else:
            result.append(token)

    while len(operators_stack) > 0:
        result.append(operators_stack.pop())

    return string.join(result, " ")

class InfixToPostfixConverterTest(unittest.TestCase):
    
    def test_expression_of_one_term(self):
        result = infix_to_postfix("1")
        self.assertEqual("1", result)
        result = infix_to_postfix("100")
        self.assertEqual("100", result)

    def test_sum_of_two_numbers(self):
        result = infix_to_postfix("1 + 3")
        self.assertEqual("1 3 +", result)

    def test_sum_of_more_than_two_numbers(self):
        result = infix_to_postfix("1 + 2 + 3 + 4 + 5")
        self.assertEqual("1 2 3 4 5 + + + +", result)

    def test_operator_precedence(self):
        result = infix_to_postfix("2 * 3 + 4")
        self.assertEqual("2 3 * 4 +", result)
        result = infix_to_postfix("2 + 4 * 3 + 5 * 2")
        self.assertEqual("2 4 3 * 5 2 * + +", result)
        result = infix_to_postfix("4 / 2 * 3")
        self.assertEqual("4 2 / 3 *", result)

if __name__ == "__main__":
    unittest.main()
