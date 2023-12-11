import user_inputs


class StreetLightService:
    """ SL : Low Tension Street Light Service """

    def __init__(self):
        user_inputs_obj = user_inputs.UserInput()
        self.unit = user_inputs_obj.user_input_units()
        self.unit_energy_charges = 4.30
        self.energy_charges = 0
        self.total_charge = 0

    def total_charges(self, units, charges):
        """ To calculate Total Charges for Residential Purpose. """
        self.energy_charges = units * charges
        print("Energy Charges: ₹", self.energy_charges)

    def sl(self):
        """ Tariff for SL : Low Tension Street Light Service. """

        print("\nSL : Low Tension Street Light Service")
        self.total_charges(self.unit, self.unit_energy_charges)
