from unittest import TestCase

from employee.InvalidHourOfWork import InvalidHourOfWork
from employee.employe import Employee, calculate_emp_salary


class TestEmployee(TestCase):
    def test_user_can_view_detail(self):
        employees = Employee(1,"debo","Tech team")
        employees.set_emp_id(1)
        employees.set_emp_name("Debo")
        employees.set_emp_department("Tech team")
        self.assertEqual("Tech team",employees.get_emp_department())
        self.assertEqual(50,calculate_emp_salary(self,5))
        print(employees)

    def test_user_can_view_detail_employee2(self):
        employees = Employee(2,"Deborah","Tech team")
        employees.set_emp_id(2)
        employees.set_emp_name("Deborah")
        employees.set_emp_department("Tech team")
        self.assertEqual("Tech team",employees.get_emp_department())
        with self.assertRaises(InvalidHourOfWork):
            calculate_emp_salary(self,500)
        print(employees)





