# Python Program for simple OTP generator
# ver 2

import random as r

print("4 digit OTP Generator")
print()
print("generate otp? y/n")

answer = input()
if answer == "y" :
  def otpgen() :
    otp = ""
    for i in range(4):
      otp+=str(r.randint(1,9))
    print("Your OTP is: ")
    print(otp)

  otpgen()
else :
  print("ok")
