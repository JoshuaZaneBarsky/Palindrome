from Palindrome import Palindrome
from Generate_data import Generate_data
# for testing
from Batch_test import Batch_test

# Check a palindrome
palindrome_check = Palindrome()
gen = Generate_data()
pal = gen.generate_palindrome(7)
palindrome_check.is_palindrome(pal)

# Check a non palindrome
#palindrome_check = Palindrome()
#gen = Generate_data()
#non_pal = gen.generate_non_palindrome(7)
#palindrome_check.is_palindrome(non_pal)

# For testing is_palindrome with a palindrome:
#testing_mode = True
#num_of_tests = 10000
#palindrome_testing = Palindrome(testing_mode)
#gen = Generate_data()
#bt = Batch_test(palindrome_testing, gen)
#bt.test_pal(num_of_tests)

# For testing is_palindrome with a non palindrome:
#testing_mode = True
#num_of_tests = 10000
#palindrome_testing = Palindrome(testing_mode)
#gen = Generate_data()
#bt = Batch_test(palindrome_testing, gen)
#bt.test_non_pal(num_of_tests)
