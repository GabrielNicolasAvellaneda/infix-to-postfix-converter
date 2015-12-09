import unittest

def infix_to_postfix(infix_expression):
    result = ""
    for token in infix_expression.split():
        result += token 
    return result

class InfixToPostfixConverterTest(unittest.TestCase):
    
    def test_expression_of_one_term(self):
        result = infix_to_postfix("1")
        self.assertEqual("1", result)
        result = infix_to_postfix("100")
        self.assertEqual("100", result)

if __name__ == "__main__":
    unittest.main()
