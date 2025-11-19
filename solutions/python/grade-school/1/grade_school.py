class School:
    def __init__(self):
        self._db = {}           
        self._added_results = [] 

    def add_student(self, name, grade):
        for g in self._db.values():
            if name in g:
                self._added_results.append(False)
                return False

        if grade not in self._db:
            self._db[grade] = []

        self._db[grade].append(name)
        self._added_results.append(True)
        return True

    def added(self):
        return self._added_results

    def roster(self):
        result = []
        for grade in sorted(self._db.keys()):
            result.extend(sorted(self._db[grade]))
        return result

    def grade(self, grade_number):
        if grade_number in self._db:
            return sorted(self._db[grade_number])
        return []
