class Person():
    def __init__(self,name,age):
        self.__name=name
        self.__age =age
    def getName(self):
         return self.__name
    
    def getAge(self):
         return self.__age
     
class Student(Person):
   
    def __init__(self,name,age,grade,subjects={}):
        super().__init__(name,age)
        self.__grade = grade
        self.__subjects= subjects
    
    def getNAME(self):
        name = super().getName()
        return name
    def getAGE(self):
        age = super().getAge()
        return age
   
    
    def getGrade(self):
        return self.__grade
    def setGrade(self,newGrade):
        self.__grade=newGrade
        return self.__grade
    
    def getSubjects(self):
        return self.__subjects
    def setSubjects(self,newSub):
        self.__subjects=newSub
        return self.__subjects
    
    def enroll(self, newClass):
        self.__subjects.update(newClass)
        return self.__subjects
    
    def display(self):
        
        return print(f"""                     Name: {self.getNAME()}
                     Age: {self.getAGE()}
                     Grade: {self.__grade}
                     Classes: {self.__subjects}""")
        
        
class Teacher(Person):
    def __init__(self,name,age,classes=[],students={}):
        super().__init__(name,age)
        self.__classes=classes
        self.__students = students
    
    def getNAME(self):
        name = super().getName()
        return name
    def getAGE(self):
        age = super().getAge()
        return age
          
    def getClasses(self):
        return self.__classes
    def setClasses(self,newClass):
        self.__classes=newClass
        return self.__classes
    
    def getStudents(self):
        return self.__students
    def setStudents(self,new):
        self.__students=new
        return self.__students
   
    
    def addStudent(self,new_students):
        return self.__students.update(new_students)
    
    def display(self):
        return print(f"""                     Name: {self.getNAME()}
                     Age: {self.getAGE()}
                     Students: {self.__students}
                     Classes: {self.__classes}""")
        
    def assign(self,eleve):
        student_name = list(eleve.keys())[0]
        if student_name not in self.__students:
            return print("Action is impossible student is not defined")        
        else :
            self.__students.update(eleve)
            return print(f"Updated students: {self.__students}") 
        
        
class Courses():
    def __init__(self):
      
        self.__courses = {
            'arabic': ['teacher', []],
            'french': ['teacher', []],
            'english': ['teacher', []],
            'science': ['teacher', []],
            'history': ['teacher', []],
            'physics': ['teacher', []]
        }
    def enrollStudent(self,name,course):
       if course not in self.__courses:
           return print('Action impossibe there is no such course')
       else:
           self.__courses[course][1].extend(name)
           return print(f"{name} was(were) enrolled successfully in the {course} class")
       
    def enrollTeacher(self,name,course):
       if course not in self.__courses:
           return print('Action impossibe there is no such course')
       else:
           self.__courses[course][0]=name
           return print(f"{name} was asseigned successfully to the {course} class")
    
    def display(self):
        return print(self.__courses)
       
       
       
       
       
courses = Courses()
courses.enrollStudent(['Alice','layla','hiba'], 'english')
courses.enrollTeacher('Bob', 'english')
courses.display()
   
 
 
 
 
 
 
 
 
   
object1= Teacher('maria',30)
object1.setClasses(['math','history'])
object1.addStudent({'layla':['good',56],'maha':['bad',3]})
(object1.assign({'layla':['bad',67]}))
(object1.assign({'hiba':['bad',78]}))
            
            
            
   
        

    

