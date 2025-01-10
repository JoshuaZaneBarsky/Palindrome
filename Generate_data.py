import random

class Generate_data:

    def generate_palindrome(self, n):
        data = []
        for i in range(n//2):
            data.append(random.randint(0,1))
        if n%2 == 0:
            half = len(data)
            for i in range(half-1, -1, -1):
                data.append(data[i])
        else:
            half = len(data)
            data.append(random.randint(0,1))
            for i in range(half-1, -1, -1):
                data.append(data[i])
        return data

    # This generates random numbers on a list.
    # Since random numbers can generate palindromes, here we adjusted the center bits to force a non palindrome.
    # ex. For an even number k: n_1, n_2, n_3, ..., b, 1-b, ..., n_(k-2), n_(k-1), n_k.   (for b in {0,1}. for n,k in N.) 
    # ex. For an odd number k: n_1, n_2, n_3, ..., b, r, 1-b, ..., n_(k-2), n_(k-1), n_k.  (for b,r in {0,1}. for n,k in N.)
    def generate_non_palindrome(self, n):
        data = []
        for i in range((n//2)-1): # go up to just before half
            data.append(random.randint(0,1))
        if n%2 == 0:
            b = random.randint(0,1)
            data.append(b)
            data.append(1-b)
            half = len(data)
            for i in range(half-1, -1, -1):
                data.append(random.randint(0,1))
        else:
            half = len(data)
            b = random.randint(0,1)
            data.append(b)
            data.append(random.randint(0,1))
            data.append(1-b)
            for i in range(half-1, -1, -1):
                data.append(random.randint(0,1))
        return data