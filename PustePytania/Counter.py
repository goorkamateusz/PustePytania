""" Counter of data """

class Counter:
    """ Counter of data """
    def __init__(self):
        self.screen = 0
        self.skip   = 0
        self.exam   = 0
        self.msg    = 0

    def limit_of_exam(self, exam_num_max = 0):
        """ Limit of exam"""
        if exam_num_max == 0:
            return False
        else:
            return self.exam >= exam_num_max
