class CourierCompanyCollection:
    def __init__(self, company_name):
        self.company_name = company_name
        self.courier_details = []
        self.employee_details = []
        self.location_details = []

    def __str__(self):
        return f"CourierCompanyCollection({self.company_name})"