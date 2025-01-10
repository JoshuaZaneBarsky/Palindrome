class Batch_test:

    global P, G # objects to test

    def __init__(self, P_in, G_in):
        global G, P
        P = P_in
        G = G_in

    def test_pal(self, num_checks, len_data = 5):
        error = False
        global G, P

        for i in range(num_checks):
            pal = G.generate_palindrome(len_data)
            if P.is_palindrome(pal) == 0: # found a non palindrome where palindromes should exist
                error = True
                break
            print('[|' * (i//(num_checks//100)), end="")
            remaining = (num_checks//100)-(i//(num_checks//100))
            print(' ' * remaining * ']')

        if error:
            print("Error: a palindrome was found.")
        else:
            print("No errors.")

    def test_non_pal(self, num_checks, len_data = 5):
        error = False
        global G, P

        for i in range(num_checks):
            non_pal = G.generate_non_palindrome(len_data)
            if P.is_palindrome(non_pal) == 1: # found a palindrome where non should exist
                error = True
                break
            print('[|' * (i//(num_checks//100)), end="")
            remaining = (num_checks//100)-(i//(num_checks//100))
            print(' ' * remaining * ']')

        if error:
            print("Error: a non palindrome was found.")
        else:
            print("No errors.")