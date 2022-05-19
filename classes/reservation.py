class Reservation:
    def __init__(self,fseats,sseats):
        self.fseats=fseats
        self.sseats=sseats
        
    def print(self):
        print('\n 1.first class:Rs100 \n 2.second class:Rs 50 \n')
    
    def reserve(self):
        choice=int(input('select the class(option num)'))
        if choice==1:
            n=int(input("enter number of seats"))
            self.fseats=self.fseats-n
            print('>>>>>booking conformed<<<<<<<')
        elif choice==2:
             n=int(input("enter number of seats"))
             self.sseats=self.sseats-n
             print('>>>>>booking conformed<<<<<<<')
        else:
            print('wrong input')
    def available(self):
        print(' available seats are:')
        print('first clsss :'+str(self.fseats))
        print('second class :'+str(self.sseats))

def main():
    r=Reservation(10,10)
    r.print()
    r.available()
    r.reserve()
    r.available()

if __name__=='__main__':
    main()