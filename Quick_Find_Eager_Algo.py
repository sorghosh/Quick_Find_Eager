####inspired by princeton university

class Quick_Find_Eager:
    def __init__(self,n):
        self.id = [i for i in range(0,n)]
    
    def union(self,i,j):
        frst_element = self.id[i]
        scnd_element = self.id[j]
        for row,value in enumerate (self.id):
            if value == frst_element:
                self.id[row] = scnd_element
    def connected(self,i,j):
        return self.id[i] == self.id[j]

    def print_result(self):
        print self.id


obj = Quick_Find_Eager(10)
obj.print_result()
obj.union(4,3)
obj.print_result()

obj.union(3,8)
obj.print_result()


obj.union(6,5)
obj.print_result()

obj.union(9,4)
obj.print_result()

obj.union(2,1)
obj.print_result()

obj.union(5,0)
obj.print_result()

obj.union(7,2)
obj.print_result()

obj.union(6,1)
obj.print_result()

obj.union(7,3)
obj.print_result()




