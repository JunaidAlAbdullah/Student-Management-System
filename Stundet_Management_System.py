class StudentDatabase:
    student_list = []
    
    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)
    
    @classmethod
    def find_student_by_id(cls, student_id):
        for student in cls.student_list:
            if student.get_student_id() == student_id:
                return student
        return None
    
    @classmethod
    def view_all_students(cls):
        if not cls.student_list:
            print('No students in the database.')
            return
        
        print('\n--- Student List ---')
        for student in cls.student_list:
            student.view_student_info()
            print('-------------------------------------')

class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)
    
    def get_student_id(self):
        return self.__student_id
    
    def get_name(self):
        return self.__name
    
    def get_department(self):
        return self.__department
    
    def is_student_enrolled(self):
        return self.__is_enrolled
    
    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f'Student {self.__name} has been enrolled successfully.')
        else:
            print(f'Student {self.__name} is already enrolled.')
    
    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f'Student {self.__name} has been dropped successfully.')
        else:
            print(f'Student {self.__name} is not availabe.')
    
    def view_student_info(self):
        if self.__is_enrolled is True:
            enrollment_status = 'Enrolled'
        else:
            enrollment_status = 'Not Enrolled'

        print(f'ID: {self.__student_id}')
        print(f'Name: {self.__name}')
        print(f'Department: {self.__department}')
        print(f'Status: {enrollment_status}')

def main():

    student1 = Student('01', 'Junaid Abdullah', 'Computer Science', False)
    student2 = Student('02', 'Tahmidur Rahman', 'Electrical Engineering', False)
    student3 = Student('03', 'Ashrafur Rahman', 'Business Administration', False)
    student4 = Student('04', 'Tahmid Al Islam', "Pharmacy", False)
    
    while True:
        print('\n=== Student Management System ===')
        print('1. View All Students')
        print('2. Enroll Student')
        print('3. Drop Student')
        print('4. Exit')
        

        choice = input('Enter your choice (1-4): ')

        if choice.isdigit():
                choice = int(choice)
                
                if choice == 1:
                    StudentDatabase.view_all_students()
                
                elif choice == 2:
                    student_id = input('Enter Student ID to enroll: ')
                    student = StudentDatabase.find_student_by_id(student_id)
                    if student:
                        student.enroll_student()
                    else:
                        print("Error: Student ID not found.")
                
                elif choice == 3:
                    student_id = input('Enter Student ID to drop: ')
                    student = StudentDatabase.find_student_by_id(student_id)
                    if student:
                        student.drop_student()
                    else:
                        print('Student ID not found.')
                
                elif choice == 4:
                    print('Exiting the Student Management System. Sayonara Tata Goodbye!')
                    break
                
                else:
                    print('Invalid choice. Please enter a number between 1 & 4.')
        
        else:
            print('Invalid choice. Please enter a number.')

main()