class Teaser:
    
    def __init__(self,name,bAtt,bintel,bbud,bhpy,bmatr,gname,gAtt,gintel,gmaintainance,ghpyns,gpintel,gpattr):
        self.name = name
        self.bAtt = bAtt
        self.bintel = bintel
        self.bbud=bbud
        self.bhpy=bhpy
        self.bmatr=bmatr
        self.gname=gname
        self.gAtt=gAtt
        self.gintel=gintel
        self.gmaintainance=gmaintainance
        self.ghpyns=ghpyns
        self.gpintel=gpintel
        self.gpattr=gpattr

    def check(self):
        if(self.gAtt >= self.bmatr and self.bbud >= self.gmaintainance and self.bintel >= self.gpintel and self.bAtt >= self.gpattr):
            return 1
        return 0
         

        
b = input('Enter no: of pairs')
studentlist = []
print('enter details in given sequence:\n boyname:\n')
i = 0
while(i < int(b)):
    studentlist.append(Teaser(input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input()))
    i = i+1
    


   

j=0
while(j < int(b)):
    k = studentlist[j].check()
    if k!=0:
        print(studentlist[j].name+' and '+studentlist[j].gname +' are couples ')
    else:
        print(studentlist[j].gname+' rejected '+studentlist[j].name)
    j=j+1;

        
    

































    
