from pydantic import BaseModel, computed_field


class Employee(BaseModel):
    name: str
    salary: int
    bonus: int

    @computed_field
    @property
    def total_salary(self) -> int:
        return self.salary + self.bonus


emp = Employee(
    name="Kunal",
    salary=50000,
    bonus=10000
)

print(emp)
print(emp.total_salary)