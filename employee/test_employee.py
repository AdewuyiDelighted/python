from unittest import TestCase

from employee.InvalidHourOfWork import InvalidHourOfWork
from employee.employDepartment import EmployeeRole
from employee.employe import Employee, calculate_emp_salary


class TestEmployee(TestCase):
    def test_user_can_view_detail(self):
        employees = Employee(1,"debo",EmployeeRole.MEDIATEAM)
        employees.set_emp_id(1)
        employees.set_emp_name("Debo")
        employees.set_emp_department(EmployeeRole.TECHTEAM)
        self.assertEqual(EmployeeRole.TECHTEAM,employees.get_emp_department())
        self.assertEqual(50,calculate_emp_salary(self,5))
        print(employees)

    def test_user_can_view_detail_employee2(self):
        employees = Employee(2,"Deborah","Tech team")
        employees.set_emp_id(2)
        employees.set_emp_name("Deborah")
        employees.set_emp_department(EmployeeRole.ACCOUNTING)
        self.assertEqual(EmployeeRole.ACCOUNTING,employees.get_emp_department())
        with self.assertRaises(InvalidHourOfWork):
            calculate_emp_salary(self,500)
        print(employees)





