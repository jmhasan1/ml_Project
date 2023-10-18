import sys
# import logging
def error_message_details(error , error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    # details about exception will be stored in error_tab
    error_message = "Error occured in Python script name [{0}] line number [{1}] error message [{2}] ".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message , error_detail = error_detail)

    
    def __str__(self) :
        return self.error_message
    

# code below was written to test 

# if __name__=="__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divided by zero")
#         raise CustomException(e , sys)
        