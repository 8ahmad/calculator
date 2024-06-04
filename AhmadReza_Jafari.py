def main():
 
  # دریافت دو عدد از کاربر
  num1 = float(input("Enter Number 1 : "))
  num2 = float(input("Enter Number 2 :  "))

  # دریافت نوع عمل از کاربر
  operator = input("OP : (+,_,*,/) ")

  # محاسبه نتیجه براساس نوع عمل انتخابی
  if operator == "+":
    result = num1 + num2
  elif operator == "-":
    result = num1 - num2
  elif operator == "*":
    result = num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("EROOR")
      return
    else:
      result = num1 / num2
  else:
    print("ERROR")
    return

  # نمایش نتیجه
  print(f"{num1} {operator} {num2} = {result}")

# اجرای تابع اصلی
if __name__ == "__main__":
  main()
