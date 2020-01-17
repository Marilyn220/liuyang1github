class Home:
    def __init__(self, area, home_info, address):
        self.area = area
        self.home_info = home_info
        self.address = address
        self.left_area = area
        self.contain_items = []


    def __str__(self):
        msg = "房子的总面积是：%d,可用面积是：%d, 户型是：%s,地址是：%s" % (self.area, self.left_area, self.home_info, self.address)
        msg += "当前房子里的物品有%s"%(str(self.contain_items))
        return msg


    def add_item(self, item):
        self.left_area -= item.get_area()
        self.contain_items.append(item.get_name)



class Bed:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s占用的面积是:%d" % (self.name, self.area)

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name


fangzi = Home(100, "三室一厅", "北京市朝阳区酒仙桥52号")
print(fangzi)

bed1 = Bed("席梦思", 10)
print(bed1)

fangzi.add_item(bed1)

bed2 = Bed("三人床", 8)
print(bed2)
fangzi.add_item(bed2)
print(fangzi)
