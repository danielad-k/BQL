import re

class QueryConstruct:

    def __init__(self, dataset, dimension, measures, dimensionOptions, filter, count, offset):
        self.dataset = dataset
        self.dimension = dimension
        self.measures = measures
        self.dimensionOptions = dimensionOptions
        self.filter = filter
        self.count = count
        self.offset = offset

    def q_joiner(func):
        def func_wrapper(query):
            output_fcn = "query=" + re.sub("\s", "", str(query))
            return output_fcn.replace("'", '"')

        return func_wrapper

    @q_joiner
    def query(self):
        query = {"dataset": self.dataset,
                 "dimension": self.dimension,
                 "measures": self.measures,
                 "dimensionOptions": self.dimensionOptions,
                 "filter": self.filter,
                 "count": self.count,
                 "offset": self.offset
                 }
        print(query)
        return query

    def __repr__(self):
        return str(self.__dict__)
