class K:
    def __init__(self, self_roll_no, marks1, marks2, marks3, marks4):
        self.roll_no = self_roll_no
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.marks4 = marks4

    def calc(self):
        self.totalmarks = self.marks1 + self.marks2 + self.marks3 + self.marks4
        self.percentage = (self.totalmarks / 400) * 100

    def display(self):
        print("Roll no. - ", self.roll_no)
        print("Marks are: ", self.marks1, self.marks2, self.marks3, self.marks4)
        print("Total marks obtained: ", self.totalmarks)
        print("Percentage of the student is ", self.percentage)

piyush_kj(17, 50, 69, 55, 80)
piyush.calc()
piyush.display()