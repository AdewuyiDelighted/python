from employee.InvalidHourOfWork import InvalidHourOfWork


class Employee:
    hourly_rate = 10

    def __init__(self, emp_id, emp_name, emp_department):
        self._emp_id = emp_id
        self._emp_name = emp_name
        self._emp_department = emp_department
        self._number_of_hours_worked = 0

    def set_emp_id(self, emp_id):
        self._emp_id = emp_id

    def get_emp_id(self, ):
        return self._emp_id

    def set_emp_name(self, emp_name):
        self._emp_name = emp_name

    def get_emp_name(self):
        return self._emp_name

    def set_emp_department(self, emp_department):
        self._emp_department = emp_department

    def get_emp_department(self):
        return self._emp_department

    def __str__(self):
        return """
        Employee id : {id}
        Employee name :{name}
        Employee department:{department}
        """.format(id=self._emp_id, name=self._emp_name, department=self._emp_department)


def get_hourly_rate(self):
    return Employee.hourly_rate


def calculate_emp_salary(self, hour: int):
    if 0 < hour <= 200:
        return Employee.hourly_rate * hour
    else:
        raise InvalidHourOfWork("Invalid hours of works")
