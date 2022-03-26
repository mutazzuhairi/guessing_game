

class Utility(object):
    @staticmethod
    def check_is_guessing_input_valid(input_, upper, lower):
        try:
            int(input_)
        except ValueError:
            return False
        else:
            if lower <= int(input_) <= upper:
                return True
            else:
                return False
