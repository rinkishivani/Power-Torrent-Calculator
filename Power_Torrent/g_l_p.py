import user_inputs


class GeneralLightningPurpose:
    """ GLP : For Hospitals, Schools & Religious Purpose. """

    def __init__(self):
        user_inputs_obj = user_inputs.UserInput()
        self.unit = user_inputs_obj.user_input_units()
        self.months = user_inputs_obj.user_input_months()
        self.phase = user_inputs_obj.user_input_phase()
        self.first_two_hund_unit_charge = 4.10
        self.remaining_unit_charge = 4.80
        self.single_phase_charge = 30
        self.three_phase_charge = 70
        self.first_two_hund_units = 0
        self.remaining_units = 0
        self.energy_charges = 0
        self.fixed_charges = 0
        self.total_charge = 0

    def first_two_hund_unit(self, units, first_two_hund_unit_charge):
        """ To calculate first 50 units of energy charges. """
        if units >= 200:
            self.first_two_hund_units = 200 * first_two_hund_unit_charge
            self.unit = units - 200
        else:
            self.first_two_hund_units = units + first_two_hund_unit_charge

    def remaining(self, units, remaining_unit_charge):
        """ To calculate remaining energy charges. """
        self.remaining_units = units * remaining_unit_charge

    def total_charges(self, first_two_hund_units_charges, remaining_units_charges, months, phase_charges):
        """ To calculate Total Charges for General Lightning Purpose. """
        self.energy_charges = first_two_hund_units_charges + remaining_units_charges
        self.fixed_charges = months * phase_charges
        self.total_charge = self.energy_charges + self.fixed_charges
        print("Energy Charges: ₹", self.energy_charges)
        print("Fixed Charges: ₹", self.fixed_charges)
        print("Total Charges: ₹", self.total_charge)

    def glp(self):
        self.first_two_hund_unit(self.unit, self.first_two_hund_unit_charge)
        self.remaining(self.unit, self.remaining_unit_charge)
        if self.phase == "s":
            self.fixed_charges = self.single_phase_charge
        else:
            self.fixed_charges = self.three_phase_charge
        print("\nGLP: General Lightning Purpose")
        self.total_charges(self.first_two_hund_units, self.remaining_units, self.months, self.fixed_charges)
