import user_inputs


class NonRGP:
    """ Non-RGP : Low Tension Service for Commercial and Industrial Purpose """

    def __init__(self):
        user_inputs_obj = user_inputs.UserInput()
        self.unit = user_inputs_obj.user_input_units()
        self.months = user_inputs_obj.user_input_months()
        self.energy_charge_per_unit = 4.60
        self.fixed_charge_less_than_5 = 70
        self.fixed_charge_between_5_and_15 = 90
        self.energy_charges = 0
        self.fixed_charges = 0
        self.total_charge = 0

    def total_charges(self, energy_charge_per_unit, month, fixed_charges):
        """ To calculate Total Charges for Non RGP. """
        self.energy_charges = self.unit * energy_charge_per_unit
        self.fixed_charges = self.unit * month * fixed_charges
        self.total_charge = self.energy_charges + self.fixed_charges
        print("Energy Charges: ₹", self.energy_charges)
        print("Fixed Charges: ₹", f"{self.fixed_charges:.2f} ")
        print("Total Charges: ₹", f"{self.total_charge:.2f} ")

    def non_rgp(self):
        if self.unit <= 5:
            self.fixed_charges = self.fixed_charge_less_than_5
        elif 5 < self.unit <= 15:
            self.fixed_charges = self.fixed_charge_between_5_and_15
        print("\nNon RGP: Low Tension Service for Commercial and Industrial Purpose")
        self.total_charges(self.energy_charge_per_unit, self.months, self.fixed_charges)
