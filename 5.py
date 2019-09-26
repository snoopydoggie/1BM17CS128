class CallDetail:
    def _init_(self):
        self.caller = None
        self.receiver = None
        self.ctype = None
        self.duration=None
    def input_values(self,l):
        self.caller=l[0]
        self.receiver=l[1]
        self.ctype=l[2]
        self.duration=l[3]
    def print_one(self):
        print("Call Details:")
        print("Caller: ",self.caller)
        print("Receiver: ",self.receiver)
        print("Type: ",self.ctype)
        print("Duration",self.duration)
class Util:
    list_of_call_objects=[]
    def _init_(self):
        self.list_of_call_objects=None
    def parse_customer(self,list_of_call_string):
        for i in list_of_call_string:
            l=i.split(",")
            ob=CallDetail()
            ob.input_values(l)
            self.list_of_call_objects.append(ob)
    def print_all(self):
        for i in self.list_of_call_objects:
            i.print_one()


c='y'
l1=[]
while(c=='y'):
    print("Enter call details")
    s1=""
    s1=s1+raw_input("Enter no of caller")+","
    s1=s1+raw_input("Enter the no of receiver")+","
    s1=s1+raw_input("Enter the type of call")+","
    s1=s1+raw_input("Enter the duration of call")+","
    l1.append(s1)
    c=raw_input("Enter y to continue else enter n")
ob1=Util()
ob1.parse_customer(l1)
ob1.print_all()
                        
