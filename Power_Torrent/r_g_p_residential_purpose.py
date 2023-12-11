import user_inputs


class ResidentialPurpose:
    """ RGP : Residential Purpose (Up to & Including 15 KW) """

    def __init__(self):
        user_inputs_obj = user_inputs.UserInput()
        self.unit = user_inputs_obj.user_input_units()
        self.months = user_inputs_obj.user_input_months()
        self.phase = user_inputs_obj.user_input_phase()
        self.energy_charges = 0
        self.fixed_charges = 0
        self.first_fifty_units = 0
        self.next_one_fifty_units = 0
        self.remaining_units = 0
        self.single_phase_charge = 25
        self.three_phase_charge = 65

        self.rgp_first_fifty_units_charge = 3.20
        self.bpl_first_fifty_units_charge = 1.50
        self.next_one_fifty_units_charge = 3.95
        self.remaining_units_charge = 5.00
        self.bpl_fixed_charges = 5.00

        self.total_charge = 0

    def first_fifty_unit(self, units, first_fifty_unit_charge):
        """ To calculate first 50 units of energy charges. """
        if units >= 50:
            self.first_fifty_units = 50 * first_fifty_unit_charge
            self.unit = units - 50
        else:
            self.first_fifty_units = units * first_fifty_unit_charge
            self.unit = self.unit - units

    def next_one_fifty_unit(self, units, next_fifty_unit_charge):
        """ To calculate first 150 units of energy charges. """
        if units >= 150:
            self.next_one_fifty_units = 150 * next_fifty_unit_charge
            self.unit = units - 150
        else:
            self.next_one_fifty_units = units * next_fifty_unit_charge
            self.unit = self.unit - units

    def remaining_unit(self, units, remaining_unit_charge):
        """ To calculate remaining units of energy charge. """
        if units:
            self.remaining_units = units * remaining_unit_charge
            self.unit = self.unit - units

    def total_charges(self, first_fifty_units_charges, next_one_fifty_units_charges,
                      remaining_units_charges, months, phase_charges):
        """ To calculate Total Charges for Residential Purpose. """
        self.energy_charges = (first_fifty_units_charges +
                               next_one_fifty_units_charges + remaining_units_charges)
        self.fixed_charges = months * phase_charges
        self.total_charge = self.energy_charges + self.fixed_charges
        print("Energy Charges: ₹", self.energy_charges)
        print("Fixed Charges: ₹", self.fixed_charges)
        print("Total Charges: ₹", self.total_charge)

    def rgp(self):
        """ Tariff for RGP : Residential General Purpose. """
        print("1: ", self.unit)
        self.first_fifty_unit(self.unit, self.rgp_first_fifty_units_charge)
        print("1: ", self.unit)
        self.next_one_fifty_unit(self.unit, self.next_one_fifty_units_charge)
        print(self.unit)
        self.remaining_unit(self.unit, self.remaining_units_charge)
        print(self.unit)
        print("\nRGP: Residential General Purpose")
        if self.phase == "s":
            self.fixed_charges = self.single_phase_charge
        elif self.phase == "t":
            self.fixed_charges = self.three_phase_charge
        self.total_charges(self.first_fifty_units, self.next_one_fifty_units,
                           self.remaining_units, self.months,
                           self.fixed_charges)

    def bpl(self):
        """ Tariff for BPL : Below Poverty Line. """
        self.first_fifty_unit(self.unit, self.bpl_first_fifty_units_charge)
        self.next_one_fifty_unit(self.unit, self.next_one_fifty_units_charge)
        self.remaining_unit(self.unit, self.remaining_units_charge)
        print("\nBPL: Below Poverty Line")
        self.total_charges(self.first_fifty_units, self.next_one_fifty_units,
                           self.remaining_units, self.months,
                           self.bpl_fixed_charges)


# rp = ResidentialPurpose()
# rp.rgp()
# rp.bpl()
