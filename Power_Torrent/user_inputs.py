from exceptions import InvalidMonthException, InvalidPhaseException, InvalidInputException


class UserInput:

    def __init__(self):
        self.user_selected_category = ""
        self.category_name = ""
        self.sub_category = ""
        self.unit = ""
        self.months = ""
        self.PHASE_LIST = ["s", "t"]
        self.phase = ""
        self.max_demand = ""
        self.contract_demand = ""
        self.power_factor = ""
        self.contract_demand_85_percent = ""
        self.billing_demand = 0
        self.ltmd_billing_demand_constant = 6
        self.installations = 0
        self.days = 0

    def user_input_units(self):
        while not self.unit.isdigit():
            try:
                self.unit = input("Enter units: ")
                if not self.unit.isdigit():
                    raise InvalidInputException
                else:
                    self.unit = float(self.unit)
                    break
            except InvalidInputException:
                print("Invalid Input Exception raised. Units must be a number!")
        return self.unit

    def user_input_months(self):
        while True:
            try:
                self.months = input("Enter number of months: ")
                if self.months.isdigit() and (1 <= int(self.months) <= 12):
                    self.months = int(self.months)
                    break
                elif not self.months.strip("-").isdigit():
                    raise InvalidInputException
                elif self.months.strip("-").isdigit():
                    if not (1 <= int(self.months) <= 12):
                        raise InvalidMonthException
            except InvalidInputException:
                print("Invalid Input Exception raised. Months must be a number!")
            except InvalidMonthException:
                print("Invalid Month Exception raised. Months must be a between 1-12!")
        return self.months

    def user_input_phase(self):
        while True:
            try:
                self.phase = input("Enter phase (s) single phase / (t) three phase: ")
                if self.phase not in self.PHASE_LIST:
                    raise InvalidPhaseException
                else:
                    self.phase = self.phase.lower()
                    break
            except InvalidPhaseException:
                print("Invalid Phase Exception raised. Phase must be either 's' or 't'")
        return self.phase

    def user_input_max_demand(self):
        print("Maximum Demand in a month means the highest value of average kW used/consumed by the consumer during "
              "any time block of 30 minutes.")
        while True:
            try:
                self.max_demand = input("Enter Maximum Demand: ")
                if not self.max_demand.isdigit():
                    raise InvalidInputException
                else:
                    self.max_demand = float(self.max_demand)
                    break
            except InvalidInputException:
                print("Invalid Phase Exception raised. Maximum Demand must be a number!")
        return self.max_demand

    def user_input_contract_demand(self):
        print("Contract Demand means the maximum kW for the supply of which TPL has provided facility to the consumer.")
        while True:
            try:
                self.contract_demand = input("Enter Contract Demand: ")
                if not self.contract_demand.isdigit():
                    raise InvalidInputException
                else:
                    self.contract_demand = float(self.contract_demand)
                    break
            except InvalidInputException:
                print("Invalid Phase Exception raised. Contract Demand must be a number!")
        return self.contract_demand

    def user_input_power_factor(self):
        while True:
            try:
                self.power_factor = input("Enter Power Factor (%): ")
                if self.power_factor.isdigit():
                    if 1 <= int(self.power_factor) <= 100:
                        self.power_factor = float(self.power_factor)
                        break
                    else:
                        raise InvalidInputException
                else:
                    raise InvalidInputException
            except InvalidInputException:
                print("Invalid Power Factor Exception raised. Power Factor must be a number between 1-100 (%)")
        return self.power_factor

    def user_input_installation(self):
        while True:
            try:
                self.installations = input("Enter number of installations: ")
                if self.installations.isdigit() and (1 <= int(self.installations) <= 12):
                    self.installations = float(self.installations)
                    break
                elif not self.installations.strip("-").isdigit():
                    raise InvalidInputException
            except InvalidInputException:
                print("Invalid Installation Exception raised. Installation must be a number!")
        return self.installations

    def user_input_days(self):
        while True:
            try:
                self.days = input("Enter number of days: ")
                if self.days.isdigit() and (1 <= int(self.days) <= 12):
                    self.days = int(self.days)
                    break
            except InvalidInputException:
                print("Invalid Input Exception raised. Months must be a number!")
        return self.days
