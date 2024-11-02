'''calculate factorial for a given number using memoziation principle and provide the result. This is mainly to avoid reptative loops and to resue existing results as factorial depdends 0n previous series result .
Also memoziation helps for faster execution since result are referred from cache and specially it helps for faster factorial calculation rather then repetitive if else statements.. we are using __call__ method refere dict as cache here

But there various cache techniques are there which can be referred here: https://www.pythoncontent.com/memoization-in-python/ 
addtional ref: https://stackoverflow.com/questions/18939731/why-memoization-can-speed-up-factorial-in-python-even-if-there-is-no-repeated-co 

Below program is referenc from :  https://stackoverflow.com/questions/5824881/python-call-special-method-practical-example/5825081 
'''

class Factorial(object):    
    def __init__(self):
        self.cache={}       
    def __call__(self, n):        
             if n not in (self.cache):
                  if n == 0:
                      self.cache[n]=1                      
                  else:
                      self.cache[n]=n*self.__call__(n-1)                       
             return(self.cache[n])

calfac=Factorial()
for n in range(0, 5):
    print("{}! = {}". format(n, calfac(n)))

'''
Also __call__ method is useful specially to implement API's.. example:  https://stackoverflow.com/questions/5824881/python-call-special-method-practical-example 

I find it useful because it allows me to create APIs that are easy to use (you have some callable object that requires some specific arguments), and are easy to implement because you can use Object Oriented practices.

The following is code I wrote yesterday that makes a version of the hashlib.foo methods that hash entire files rather than strings:

# filehash.py
import hashlib


class Hasher(object):
    """
    A wrapper around the hashlib hash algorithms that allows an entire file to
    be hashed in a chunked manner.
    """
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def __call__(self, file):
        hash = self.algorithm()
        with open(file, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), ''):
                hash.update(chunk)
        return hash.hexdigest()


md5    = Hasher(hashlib.md5)
sha1   = Hasher(hashlib.sha1)
sha224 = Hasher(hashlib.sha224)
sha256 = Hasher(hashlib.sha256)
sha384 = Hasher(hashlib.sha384)
sha512 = Hasher(hashlib.sha512)
'''