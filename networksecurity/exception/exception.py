import sys

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message
        _,_,exc_tb = error_detail.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "ERROR occured in python script name [{0}] line number [{1}] error message [{2}]".format(self.filename, self.lineno, self.error_message)
        

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        raise NertworkSecurityException(e, sys)