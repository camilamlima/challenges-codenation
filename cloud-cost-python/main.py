
PRICE_FILE = 0.00000040
PRICE_FUNCTION = 0.0000002
PRICE_EXECUTION = 0.0002080
TIME_IN_EXECUTION = 3.0
COUNT_FUNCTION = 2.0

YEAR = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

class CloudCost():
    def lambda_execution(self):
        return PRICE_FUNCTION + ( TIME_IN_EXECUTION * PRICE_EXECUTION)
        
    def app_execution(self, execution_times):
        _price = COUNT_FUNCTION * self.lambda_execution()
        _price += PRICE_FILE
        return _price*execution_times

    def month(self, execution_times, month_of_year):
        return self.app_execution(execution_times) * YEAR[month_of_year]
    
    def year(self, execution_times):
        
        result = []
        for month in YEAR.keys():
            result.append(
                self.month(execution_times, month)
                )
        return result
