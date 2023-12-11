import user_inputs


class LowTensionTemporarySupply:
    """  TMP : Low Tension Temporary Supply """

    def __init__(self):
        user_inputs_obj = user_inputs.UserInput()
        self.unit = user_inputs_obj.user_input_units()
        self.days = user_inputs_obj.user_input_days()
        self.energy_unit_charges = 5.10
        self.fixed_unit_charges = 25
        self.energy_charges = 0
        self.fixed_charges = 0
        self.total_charge = 0

    def total_charges(self, units, days, energy_charges, fixed_charges):
        """ To calculate Total Charges for Low Tension Temporary Supply. """
        self.energy_charges = units * energy_charges
        self.fixed_charges = fixed_charges * units * days
        self.total_charge = self.energy_charges + self.fixed_charges
        print("Energy Charges: ₹", self.energy_charges)
        print("Fixed Charges: ₹", self.fixed_charges)
        print("Total Charges: ₹", self.total_charge)

    def tmp(self):
        """ Tariff for TMP : Low Tension Temporary Supply. """

        print("\nTMP : Low Tension Temporary Supply")
        self.total_charges(self.unit, self.days, self.energy_unit_charges, self.fixed_unit_charges)
