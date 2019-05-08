from operator import itemgetter

Sales_Goal = 500.00


class SellersRancking:
    def best_seller(self, sellers):
        best_seller = self.rancking_list(sellers)
        return best_seller[:1]
            
    def rancking_list(self, sellers):
        sellers.sort(reverse=True, key=lambda x: x['value'])
        return list(map(itemgetter('name'), sellers))

    def best_seller_store(self, sellers, store):
        best_seller_store = list(filter(lambda x: x['store'] == store, sellers))
        return self.best_seller(best_seller_store)

    def sales_goals(self, sellers):
        sales_goals = list(filter(lambda x: x['value'] < Sales_Goal, sellers))
        sales_goals.sort(key=itemgetter('value'))
        return list(map(itemgetter('name'), sales_goals))
