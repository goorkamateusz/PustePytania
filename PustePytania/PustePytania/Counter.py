
class Counter:
    """ Counter of process statistics """
    def __init__(self):
        self.screen = 0
        self.skip   = 0
        self.exam   = 0
        self.msg    = 0
        self.reapeted = 0

    def limit_of_exam(self, exam_num_max = 0):
        """ Limit of exam"""
        if exam_num_max == 0:
            return False
        else:
            return self.exam >= exam_num_max

    def __iadd__(self, oth):
        """ += operator """
        self.screen   += oth.screen
        self.skip     += oth.skip
        self.exam     += oth.exam
        self.msg      += oth.msg
        self.reapeted += oth.reapeted
        return self
