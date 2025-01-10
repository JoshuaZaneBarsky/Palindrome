from Palindrome import Palindrome
from Generate_data import Generate_data
# for testing
from Batch_test import Batch_test

palindrome_check = Palindrome()
gen = Generate_data()

pal = gen.generate_palindrome(7)
palindrome_check.is_palindrome(pal)



#for testing
#bt = Batch_test(palindrome_check, gen)
#bt.test_pal(10000)
