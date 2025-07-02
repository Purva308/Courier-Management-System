from entity.couriercompanycollection import CourierCompanyCollection

class CourierUserServiceCollectionImpl:
    def __init__(self,company_obj):
        self.company_obj=company_obj

    def place_order(self,courier_obj):
        self.company_obj.courier_details.append(courier_obj)
        return courier_obj.tracking_number

    def get_order_status(self,tracking_number):
        for c in self.company_obj.courier_details:
            if c.tracking_number == tracking_number:
                return c.status
        return "Tracking number is not found"

    def cancel_order(self,tracking_number):
        for c in self.company_obj.courier_details:
            if c.tracking_number == tracking_number:
                if c.status.lower()!="In Transit or Pending Pickup":
                    return False
                c.status="Cancelled"
                return True
        return False

    def get_assigned_order(self,employee_id):
        return[c for c in self.company_obj.courier_details if c.employee_id == employee_id]
