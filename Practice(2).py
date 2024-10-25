class Book():
    def __init__(self,title,author,status='available'):
        self.__title = title
        self.__author=author
        self.__status=status
        
    def getTitle(self):
        return self.__title
    
    def setTitle(self,x):
        self.__title=x
        
    def getStatus(self):
        return self.__status
    
    def setStatus(self,s):
        self.__status=s
        
        
class Library():
    novels ={'book1':['corrupt', 'penelope douglas'],
             'book2':['hideaway', 'penelope douglas'],
             'book2':['kill switch', 'penelope douglas'],
             'book3':['conclave', 'penelope douglas'],
             'book4':['nightfall', 'penelope douglas'],
             'book5':['firenight', 'penelope douglas']}
    
    def getBooks(self):
        return self.__books
    
    def addBooks(self,x,y):
        Library.novels[x]=y
        return f'We added {x}to the lbrary'

oject1=Library()
oject1.addBooks('book6', ['punk57', 'penelope douglas'])