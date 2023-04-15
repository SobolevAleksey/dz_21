class Request():
    def __init__(self, all_storages, request):
        self.all_atorages = all_storages
        data = request.split()
        self.where = data[4]
        self.to = data[6]
        self.amount = data[1]
        self.product = data[2]



req = Request(['str', 'prt'], 'Доставить 3 печеньки из склад в магазин')
print(req.to)
