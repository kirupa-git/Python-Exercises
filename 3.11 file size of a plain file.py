import os

kk = os.stat("A Tale of Two Citie")
print(kk)
ll = kk.st_size
print(ll)
