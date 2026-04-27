print("Hello, this is a simple calculator program")
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
sign = input("Enter operator(+, -, *, /, %): ")
o = sign.strip()

if o == "+":
  print(a,"+","b","=",(a+b))
elif o == "-":
  print(a,"-","b","=",(a-b))
elif o == "*":
  print(a,"*","b","=",(a*b))
elif o == "/":
  print(a,"/","b","=",(a/b))
elif o == "%":
  print(a,"%","b","=",(a%b))
else:
  print("Please enter valid operator!")
