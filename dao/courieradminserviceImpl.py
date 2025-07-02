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
            VALUES (%s,%s,%s,%s,%s,%s)
            """
            values=(
                employee_obj.get_employee_id(),
                employee_obj.get_employeeName(),
                employee_obj.get_email(),
                employee_obj.get_contactNumber(),
                employee_obj.get_role(),
                employee_obj.get_salary()
            )
            cursor.execute(insert_query,values)
            self.connection.commit()
            print(f"Courier Employee{employee_obj.get_employeeName()} added Successfully with ID {employee_obj.get_employee_id()}.")
            return employee_obj.get_employee_id()
        except InvalidEmployeeIdException as e:
            print(f"Error:{e}")
            return None
        finally:
            cursor.close()

