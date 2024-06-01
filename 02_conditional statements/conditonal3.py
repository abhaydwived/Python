marks=float(input("Enter Marks..."))
if marks>100:
    print("Please,Check your entered marks")
    exit()

if marks>=90:
    print("Grade:A")
elif marks>=80:
    print("Grade:B")
elif marks>=70:
    print("Grade:C")
elif marks>=60:
    print("Grade:D")
elif marks<60:
    print("Grade:F")