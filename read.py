import os
import glob

print("Listing root directory")
print(glob.glob("/*"))
print("------")
print("Listing /etc directory")
print("------")
print(glob.glob("/etc/*"))
