# Grading program
# [your name]
# 15/10/2025
# T Level

# Enter the users mark
def enterMark():
    try:
        mark = int(input('Enter a mark: '))
        return mark
    
    except Exception as e:
        print("Error occurred:", e )

# validate the mark is between 0 - 360
def validateMark(mark):
    while (mark < 0 or mark >360):
        mark = int(input('Wrong, enter a mark again: '))
    return mark

# translates the users mark into a grade
def translate(mark):
    try:
        if (mark >= 324):
            grade = 'A*'
        elif (mark >= 288):
            grade = 'A'
        elif (mark >= 252):
            grade = 'B'
        elif (mark >= 216):
            grade = 'C'
        elif (mark >= 180):
            grade = 'D'
        elif (mark >= 144):
            grade = 'E'
        else:
            grade = 'U'
        return grade
          
    except Exception as e:
        print("Error occurred:", e )

# outputs the final grade
def outputGrade(grade):
    print(f"The grade is {grade}")
    
# [comment]
def main():
    try:
        mark = enterMark()
        mark = validateMark(mark)
        grade = translate(mark)
        outputGrade(grade)
        
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()
