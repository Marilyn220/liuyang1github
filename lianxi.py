class afee():
    def __init__(self):
        self.p = 0
        self.fee = 0

    def number(self, p):
        self.p = p
        print('办卡人数', self.p)
    def set_fee(self,fee):
        self.fee=fee
        print('每人每年办卡的费用', self.fee)
    def sum_fee(self):
        self.sum=self.p*self.fee
        print(self.p,'人一年办卡总费用：',self.sum)
#class person():

#class attend_day():
    #day=0
    def attend(self):
        self.a=0
        if 0 < self.p <= 1:
            self.a = 4 * 12 * 2
            print('一个人一年出席天数：',self.a)
        else:
            self.a = self.p * 4 * 12 * 2
            print(self.p, '个人一年出席天：',self.a)
#class average_fee():
    def person_fee(self):
        self.avg_fee=self.sum/self.a
        print('每人每次健身的费用为：',self.avg_fee)

if __name__=='__main__':
   f=afee()
   f.number(3)
   f.set_fee(5000)
   f.sum_fee()
   f.attend()
   f.person_fee()