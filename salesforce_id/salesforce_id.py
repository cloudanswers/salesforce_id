import base62

class InvalidSalesforceIDError(Exception):
    pass

class SalesforceID:

    def __init__(self, string_val):
        if len(string_val) not in [15, 18]:
            raise InvalidSalesforceIDError('ids must have 15 or 18 digits')
        self.prefix = string_val[:5]
        self.val = base62.decode(string_val[5:15])

    def __str__(self):
        val = base62.encode(self.val)
        while len(self.prefix + val) < 15:
            val = '0' + val
        return self.prefix + val

    def add(self, by):
        newval = SalesforceID(self.__str__())
        newval.val += by
        return newval
