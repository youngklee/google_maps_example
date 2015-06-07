class ResultSet(object):
    
    def __init__(self):
        self._result_list = []

    def add(self, row):
        self._result_list.append(row)

    def add_many(self, rows):
        map(self.add_result, rows)

    def clear_results(self):
        self._result_list = []

    def get_iter(self):
        return iter(self._result_list)

class ResultRow(dict):
    pass
