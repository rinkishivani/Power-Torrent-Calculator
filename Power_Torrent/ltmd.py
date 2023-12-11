from user_inputs import UserInput
from exceptions import InvalidUnitException


class LTMD:
    """ LTMD parent class """

    def __init__(self):
        user_inputs_obj = UserInput()
        self.unit = user_inputs_obj.user_input_units()
        self.months = user_inputs_obj.user_input_months()
        self.max_demand = user_inputs_obj.user_input_max_demand()
        self.contract_demand = user_inputs_obj.user_input_contract_demand()
        self.contract_demand_85_percent = 0
        self.power_factor = user_inputs_obj.user_input_power_factor()
        self.ltmd_billing_demand_constant = 6
        self.highest_billing_demand = 0.0
        self.first_50_unit = 0
        self.next_30_unit = 0
        self.remaining_unit = 0
        self.first_50_unit_charges_ltmd1 = 150
        self.next_30_unit_charges_ltmd1 = 185
        self.remaining_unit_charges_ltmd1 = 245
        self.excess_demand_charges_ltmd1 = 350
        self.remaining_billing = 0
        self.next_remaining_billing = 0
        self.difference = 0
        self.next_remaining = 0
        self.first_50_unit_charges_ltmd2 = 175
        self.next_30_unit_charges_ltmd2 = 230
        self.remaining_unit_charges_ltmd2 = 300
        self.excess_demand_charges_ltmd2 = 425
        self.billing_upto50_charges_ltmd1 = 4.65
        self.billing_above50_charges_ltmd1 = 4.80
        self.billing_upto50_charges_ltmd2 = 4.80
        self.billing_above50_charges_ltmd2 = 5.00

        self.power_factor_above95_charges = 0.0027
        self.power_factor_90to95_charges = 0.0015
        self.power_factor_below90_charges = 0.03
        self.charges = 0
        self.power_factor_charges = 0
        self.energy_charges = 0
        self.fixed_charges = 0
        self.total_charge = 0

    def billing_demand(self, max_demand, contract_demand, billing_demand_constant):
        self.highest_billing_demand = max(max_demand, contract_demand, billing_demand_constant)
        return float(self.highest_billing_demand)

    def energy_charges_ltmd(self, units, highest_billing_demand, less_than_50, above_50):
        if highest_billing_demand <= 50:
            self.charges = less_than_50
        elif highest_billing_demand > 50:
            self.charges = above_50
        self.energy_charges = units * self.charges

    def first_50_kw_charge(self, month, billing_demand_kw, charges):
        if billing_demand_kw > 50:
            self.first_50_unit = 50 * month * charges
            self.remaining_billing = billing_demand_kw - 50
        else:
            self.first_50_unit = month * billing_demand_kw * charges
            self.remaining_billing = self.highest_billing_demand - billing_demand_kw

    def next_30_kw_charge(self, month, billing_demand_kw, charges):
        if billing_demand_kw > 30:
            self.next_30_unit = 30 * month * charges
            self.next_remaining_billing = billing_demand_kw - 30
        else:
            self.next_30_unit = month * billing_demand_kw * charges
            self.next_remaining_billing = self.remaining_billing - billing_demand_kw

    def reaming_kw_charges(self, month, billing_demand_kw, charges):
        if billing_demand_kw:
            self.remaining_unit = month * billing_demand_kw * charges
            self.next_remaining = self.next_remaining_billing - billing_demand_kw

    def fixed_charge(self, month, billing_demand_kw, first_50_unit, next_30_unit, remaining_unit, charges):

        if self.highest_billing_demand > self.contract_demand:
            self.fixed_charges = charges * month * billing_demand_kw
        else:
            self.fixed_charges = first_50_unit + next_30_unit + remaining_unit

    def power_factor_charge(self, power_factor):
        if power_factor <= 90:
            self.difference = 90 - power_factor
            self.power_factor_charges = self.difference * self.power_factor_below90_charges
        elif 90 <= power_factor <= 95:
            self.difference = power_factor - 90
            self.power_factor_charges = self.difference * self.power_factor_90to95_charges
        elif power_factor > 90:
            self.difference = 90 - power_factor
            self.power_factor_charges = self.difference * self.power_factor_above95_charges

    def total_lmtd_charges(self, energy_charges, fixed_charges, power_factor_charge):
        """  Tariff for LTMD-1 : Low Tension Maximum Demand for Residential Purpose. """
        self.total_charge = energy_charges + fixed_charges + power_factor_charge
        print("Energy Charges: ₹", energy_charges)
        print("Fixed Charges: ₹", fixed_charges)
        print("Total Charges: ₹", self.total_charge)


class LTMD_1(LTMD):

    def __init__(self):
        super().__init__()

    def ltmd_1(self):
        try:
            if self.unit > 15:
                self.contract_demand_85_percent = self.contract_demand * 0.85
                self.billing_demand(self.max_demand, self.contract_demand_85_percent, self.ltmd_billing_demand_constant)
                self.first_50_kw_charge(self.months, self.highest_billing_demand, self.first_50_unit_charges_ltmd1)
                self.next_30_kw_charge(self.months, self.remaining_billing, self.next_30_unit_charges_ltmd1)
                self.reaming_kw_charges(self.months, self.next_remaining_billing, self.remaining_unit_charges_ltmd1)
                self.energy_charges_ltmd(self.unit, self.highest_billing_demand, self.billing_upto50_charges_ltmd1,
                                         self.billing_above50_charges_ltmd1)
                self.fixed_charge(self.months, self.highest_billing_demand, self.first_50_unit, self.next_30_unit,
                                  self.remaining_unit, self.excess_demand_charges_ltmd1)
                self.power_factor_charge(self.power_factor)
                print("\nLTMD-1 : Low Tension Maximum Demand for Residential Purpose")
                self.total_lmtd_charges(self.energy_charges, self.fixed_charges, self.power_factor_charges)
            else:
                raise InvalidUnitException
        except InvalidUnitException:
            print("Unit must be above 15KW!")


class LTMD_2(LTMD):

    def __init__(self):
        super().__init__()

    def ltmd_2(self):
        try:
            if self.unit > 15:
                self.contract_demand_85_percent = self.contract_demand * 0.85
                self.billing_demand(self.max_demand, self.contract_demand_85_percent, self.ltmd_billing_demand_constant)
                self.first_50_kw_charge(self.months, self.highest_billing_demand, self.first_50_unit_charges_ltmd2)
                self.next_30_kw_charge(self.months, self.remaining_billing, self.next_30_unit_charges_ltmd2)
                self.reaming_kw_charges(self.months, self.next_remaining_billing, self.remaining_unit_charges_ltmd2)
                self.energy_charges_ltmd(self.unit, self.highest_billing_demand, self.billing_upto50_charges_ltmd2, self.billing_above50_charges_ltmd2)
                self.fixed_charge(self.months, self.highest_billing_demand, self.first_50_unit, self.next_30_unit,
                                  self.remaining_unit, self.excess_demand_charges_ltmd2)
                self.power_factor_charge(self.power_factor)
                print("\nLTMD-2 : Low Tension Maximum Demand for other than residential purpose")
                self.total_lmtd_charges(self.energy_charges, self.fixed_charges, self.power_factor_charges)
            else:
                raise InvalidUnitException
        except InvalidUnitException:
            print("Unit must be above 15KW!")

