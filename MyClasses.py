class SubfieldsInAI:
    def Subfields():
        subfields_list = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Porcessing"]
        print("Sub-fields in AI are:")
        for i in subfields_list:
            print(i)

class OddEven:
    def OddEven():
        num = int(input("Enter a number: "))
        if (num%2==0):
            print(num," is Even number")
        else:
            print(num," is Odd number")

class EligibilityForMarriage:
    def Eligible():
        gender = input("Your Gender:")
        age = int(input("Your Age:"))
        if (gender=="Male"):
            if(age>=30):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        if (gender=="Female"):
            if(age>=27):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")

class FindPercentage:
    def percentage():
        subjects = []
        for i in range(5):
            subjects.append(int(input(f"Subject{i+1}= ")))
        print("Total :", sum(subjects))
        print("Percentage:", round((sum(subjects)/500)*100,2))

class triangle:
    def triangle():
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",round((Height*Breadth)/2,2))
        Height1 = int(input("Height1:"))
        Height2 = int(input("Height2:"))
        Breadth = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",Height1+Height2+Breadth)
        