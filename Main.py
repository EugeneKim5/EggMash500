print("Hello Human Beings, Please Enter your age: ")
Age = int(input())
if Age < 18:
    print("You can not create an Account under the Rule of SEC")
    print(f"The Current information we have are: {Age}")
elif Age > 18:
    Name = input("Enter Your Name: ")
    print(f"The Current information we have are: {Name}, {Age}")

print("chicken")