import sys

from user_inputs import UserInput
from exceptions import InvalidUnitException, InvalidInputException


class HTMD:
    """ HTMD-1 : High Tension Maximum Demand """

    def __init__(self):
        self.next_remaining = 0
        user_inputs_obj = UserInput()
        self.unit = user_inputs_obj.user_input_units()
        self.max_demand = user_inputs_obj.user_input_max_demand()
        self.contract_demand = user_inputs_obj.user_input_contract_demand()
        self.contract_demand_85_percent = 0
        self.power_factor = user_inputs_obj.user_input_power_factor()
        self.months = 1
        self.htmd_billing_demand_constant = 100
        self.highest_billing_demand = 0.0
        self.first_400_unit = 0
        self.remaining_unit = 0
        self.first_400_unit_charges = 4.55
        self.remaining_unit_charges = 4.45
        self.excess_demand_charges = 350
        self.remaining_billing = 0
        self.next_remaining_billing = 0
        self.difference = 0
        self.billing_demand_to_1000 = 260
        self.billing_demand_above_1000 = 335
        self.billing_demand_to_300 = 0.8
        self.billing_demand_above_300 = 1

        self.energy_unit_htmd2_charges = 4.10
        self.energy_unit_htmd3_charges = 7.05
        self.energy_unit_htmd4_charges = 3.55
        self.fixed_unit_charges = 225
        self.excess_demand_charges = 285
        self.tou_unit_charges = 0.6
        self.next_remaining = 0
        self.remaining_billing = 0
        self.next_remaining_billing = 0
        self.difference = 0
        self.power_factor_above95_charges = 0.0027
        self.power_factor_90to95_charges = 0.0015
        self.power_factor_below90_charges = 0.03
        self.power_factor_charges = 0
        self.charges = 0
        self.tou_charges = 0
        self.night_time = 1
        self.night_time_charge = 0.30
        self.energy_charges = 0
        self.fixed_charges = 0
        self.total_charge = 0

    def billing_demand(self, max_demand, contract_demand, billing_demand_constant):
        self.highest_billing_demand = max(max_demand, contract_demand, billing_demand_constant)
        return float(self.highest_billing_demand)

    def energy_charges_htmd(self, units, charges):
        self.energy_charges = units * charges

    def fixed_charge(self, fixed_unit_charges, highest_billing_demand, months):
        self.fixed_charges = fixed_unit_charges * highest_billing_demand * months

    def tou_charge(self, units, charges):
        self.tou_charges = units * charges

    def power_factor_charge(self, power_factor, units):
        if power_factor <= 90:
            self.difference = 90 - power_factor
            self.power_factor_charges = self.difference * self.power_factor_below90_charges * units
        elif 90 <= power_factor <= 95:
            self.difference = power_factor - 90
            self.power_factor_charges = self.difference * self.power_factor_90to95_charges * units
        elif power_factor > 90:
            self.difference = 90 - power_factor
            self.power_factor_charges = self.difference * self.power_factor_above95_charges * units

    def total_htmd_charges(self, energy_charges, fixed_charges, power_factor, tou, night_time_charge):
        """  Tariff for HTMD-1 : High Tension Maximum Demand. """
        # if len(power_factor_and_other_charges) == 1:
        #     power_factor = power_factor_and_other_charges[0]
        #     self.total_charge = energy_charges + fixed_charges + power_factor
        # elif len(power_factor_and_other_charges) == 2:
        #     power_factor, tou = power_factor_and_other_charges
        self.night_time = night_time_charge * self.unit
        self.total_charge = energy_charges + fixed_charges + power_factor + tou + self.night_time
        print("Energy Charges: ₹", energy_charges)
        print("Fixed Charges: ₹", fixed_charges)
        print("Power Factor Charges: ₹", power_factor)
        print("Time of Use Charges: ₹", tou)
        print("Total Charges: ₹", self.total_charge)


class HTMD_1(HTMD):
    """ HTMD-1 : High Tension Maximum Demand """
    def __init__(self):
        super().__init__()

    def energy_charges_htmd_1(self, units, highest_billing_demand):
        if highest_billing_demand <= 50:
            self.energy_charges = units * 4.65
        elif highest_billing_demand > 50:
            self.energy_charges = units * 4.80

    def first_400_kw_charge(self, units, charges):
        if units > 400:
            self.first_400_unit = 400 * charges
            self.remaining_billing = units - 400
        else:
            self.first_400_unit = units * charges
            self.remaining_billing = self.highest_billing_demand - units
        print("400: ", self.first_400_unit, self.remaining_billing)

    def reaming_kw_charges(self, units, charges):
        if units:
            self.remaining_unit = units * charges
            self.next_remaining = self.next_remaining_billing - units
        print("remain: ", self.remaining_unit, self.next_remaining)

    def fixed_charge_htmd1(self, billing_demand_kw):

        if billing_demand_kw <= 1000:
            self.fixed_charges = self.billing_demand_to_1000 * billing_demand_kw
        elif billing_demand_kw > 1000:
            self.fixed_charges = self.billing_demand_above_1000 * billing_demand_kw

    def tou_charge_htmd1(self, highest_billing_demand, units):

        if highest_billing_demand <= 300:
            self.charges = self.billing_demand_to_300
        elif highest_billing_demand > 300:
            self.charges = self.billing_demand_above_300
        self.tou_charges = units * self.charges

    def htmd_1(self):
        try:
            if self.unit >= 100:
                self.contract_demand_85_percent = self.contract_demand * 0.85
                self.billing_demand(self.max_demand, self.contract_demand_85_percent, self.htmd_billing_demand_constant)
                self.first_400_kw_charge(self.unit, self.first_400_unit_charges)
                self.reaming_kw_charges(self.remaining_billing, self.remaining_unit_charges)
                self.energy_charges_htmd_1(self.unit, self.highest_billing_demand)
                self.fixed_charge_htmd1(self.highest_billing_demand)
                self.power_factor_charge(self.power_factor, self.unit)
                self.tou_charge_htmd1(self.highest_billing_demand, self.unit)
                print("\nHTMD-1 : High Tension Maximum Demand")
                self.total_htmd_charges(self.energy_charges, self.fixed_charges, self.power_factor_charges,
                                        self.tou_charges, self.night_time_charge)
            else:
                raise InvalidUnitException
        except InvalidUnitException:
            print("Unit must be 100KW and above!")


class HTMD_2(HTMD):
    """ HTMD-2 : High Tension Water and Sewage Pumping Stations run by AMC. """

    def __init__(self):
        super().__init__()
        user_inputs_obj = UserInput()
        self.months = user_inputs_obj.user_input_months()

    def htmd_2(self):
        self.contract_demand_85_percent = self.contract_demand * 0.85
        self.billing_demand(self.max_demand, self.contract_demand_85_percent, self.htmd_billing_demand_constant)
        self.energy_charges_htmd(self.unit, self.energy_unit_htmd2_charges)
        self.fixed_charge(self.fixed_unit_charges, self.highest_billing_demand, self.months)
        self.power_factor_charge(self.power_factor, self.unit)
        self.tou_charge(self.unit, self.tou_unit_charges)
        print("\nHTMD-1 : High Tension Maximum Demand")
        self.total_htmd_charges(self.energy_charges, self.fixed_charges, self.power_factor_charges,
                                self.tou_charges, self.night_time_charge)


class HTMD_3(HTMD):
    """ HTMD-3 : High Tension Maximum Demand Temporary Supply. """

    def __init__(self):
        super().__init__()
        user_inputs_obj = UserInput()
        self.days = user_inputs_obj.user_input_days()
        self.night_time_charge = 0

    def fixed_charge_htmd3(self, billing_demand, contract_demand, days):
        if billing_demand <= contract_demand:
            self.fixed_charges = 25 * billing_demand * days
        elif billing_demand > contract_demand:
            self.fixed_charges = 30 * billing_demand * days

    def htmd_3(self):
        self.contract_demand_85_percent = self.contract_demand * 0.85
        self.billing_demand(self.max_demand, self.contract_demand_85_percent, self.htmd_billing_demand_constant)
        self.energy_charges_htmd(self.unit, self.energy_unit_htmd3_charges)
        self.fixed_charge_htmd3(self.highest_billing_demand, self.contract_demand, self.days)
        self.power_factor_charge(self.power_factor, self.unit)
        self.tou_charge(self.unit, self.tou_unit_charges)
        print("\nHTMD-3 : High Tension Maximum Demand Temporary Supply")
        self.total_htmd_charges(self.energy_charges, self.fixed_charges, self.power_factor_charges,
                                self.tou_charges, self.night_time_charge)


class HTMD_Metro_Traction(HTMD):
    """ HTMD Metro Traction. """

    def __init__(self):
        super().__init__()
        user_inputs_obj = UserInput()
        self.months = user_inputs_obj.user_input_months()

    def fixed_charge_metro_traction(self, billing_demand, contract_demand, months):
        if billing_demand <= contract_demand:
            self.fixed_charges = 335 * billing_demand * months
        elif billing_demand > contract_demand:
            self.fixed_charges = 385 * billing_demand * months

    def power_factor_charge_metro_traction(self, power_factor, units):
        if power_factor <= 90:
            self.difference = 90 - power_factor
            self.power_factor_charges = self.difference * self.power_factor_below90_charges * units
        elif 90 <= power_factor <= 95:
            self.difference = power_factor - 90
            self.power_factor_charges = -abs(self.difference * self.power_factor_90to95_charges * units)
        elif power_factor > 90:
            self.difference = 90 - power_factor
            self.power_factor_charges = -abs(self.difference * self.power_factor_above95_charges * units)

    def htmd_metro_traction(self):
        self.contract_demand_85_percent = self.contract_demand * 0.85
        self.billing_demand(self.max_demand, self.contract_demand_85_percent, self.htmd_billing_demand_constant)
        self.energy_charges_htmd(self.unit, self.energy_unit_htmd4_charges)
        self.fixed_charge_metro_traction(self.highest_billing_demand, self.contract_demand, self.months)
        self.power_factor_charge_metro_traction(self.power_factor, self.unit)
        self.tou_charge(self.unit, self.tou_unit_charges)
        print("\nHTMD: Metro Traction")
        self.total_htmd_charges(self.energy_charges, self.fixed_charges, self.power_factor_charges,
                                self.tou_charges, self.night_time_charge)
