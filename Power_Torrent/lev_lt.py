import user_inputs


class ElectricVehicleChargingStations:
    """  LEV : LT- Electric Vehicle Charging Stations """

    def __init__(self):
        user_inputs_obj = user_inputs.UserInput()
        self.unit = user_inputs_obj.user_input_units()
        self.months = user_inputs_obj.user_input_months()
        self.installations = user_inputs_obj.user_input_installation()
        self.unit_energy_charges = 4.20
        self.unit_fixed_charges = 25
        self.energy_charges = 0
        self.fixed_charges = 0
        self.total_charge = 0

    def total_charges(self, units, months, energy_charges, fixed_charges, installations):
        """ To calculate Total Charges for Residential Purpose. """
        self.energy_charges = units * energy_charges
        self.fixed_charges = fixed_charges * months * installations
        self.total_charge = self.energy_charges + self.fixed_charges
        print("Energy Charges: ₹", self.energy_charges)
        print("Fixed Charges: ₹", self.fixed_charges)
        print("Total Charges: ₹", self.total_charge)

    def lev_lt(self):
        """ Tariff for LEV : LT- Electric Vehicle Charging Stations. """

        print("\nLEV : LT- Electric Vehicle Charging Stations")
        self.total_charges(self.unit, self.months, self.unit_energy_charges, self.unit_fixed_charges, self.installations)
