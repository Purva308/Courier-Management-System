from util.db_conn_util import DBConnUtil
from entity.employee import Employee
from exception.InvalidEmployeeIdException import InvalidEmployeeIdException
from dao.icourieradminservice import ICourierAdminService

class CourierAdminServiceImpl(ICourierAdminService):
    def __init__(self):
        self.connection=DBConnUtil.get_connection()

    def add_courier_staff(self,employee_obj):
        cursor=None
        try:
            cursor=self.connection.cursor()
            insert_query="""
            INSERT INTO Employees(EmployeeID,Name,Email,ContactNumber,Role,Salary)
            
            """