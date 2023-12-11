import user_inputs


class LTPAgricultureService:
    """ LTP Agriculture Service (Up to & Including 15 KW) """

    def __init__(self):
        user_inputs_obj = user_inputs.UserInput()
        self.unit = user_inputs_obj.user_input_units()
        self.months = user_inputs_obj.user_input_months()
        self.energy_charge_per_unit = 3.40
        self.minimum_charge_per_bhp = 10
        self.energy_charges = 0
        self.no_of_bhp = 0
        self.minimum_charges = 0
        self.total_charge = 0

    def total_charges(self, energy_charge_per_unit, no_of_bhp, minimum_charge_per_bhp):
        """ To calculate Total Charges for LTP Agriculture Service. """
        self.energy_charges = self.unit * energy_charge_per_unit
        self.minimum_charges = no_of_bhp * minimum_charge_per_bhp
        self.total_charge = self.energy_charges + self.minimum_charges
        print("Energy Charges: ₹", self.energy_charges)
        print("Minimum Charges: ₹", f"{self.minimum_charges:.2f} ")
        print("Total Charges: ₹", f"{self.total_charge:.2f} ")

    def ltp_agriculture_service(self):
        self.no_of_bhp = (self.unit / 0.746)
        print("\nLTP (AG): For Agricultural Purpose")
        self.total_charges(self.energy_charge_per_unit, self.no_of_bhp, self.minimum_charge_per_bhp)
