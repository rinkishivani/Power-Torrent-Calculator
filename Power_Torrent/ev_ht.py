from user_inputs import UserInput
from exceptions import InvalidUnitException, InvalidInputException


class EV_HT:
    """ EV: HT- Electric Vehicle Charging Stations. """

    def __init__(self):
        self.next_remaining = 0
        user_inputs_obj = UserInput()
        self.unit = user_inputs_obj.user_input_units()
        self.months = user_inputs_obj.user_input_months()
        self.max_demand = user_inputs_obj.user_input_max_demand()
        self.contract_demand = user_inputs_obj.user_input_contract_demand()
        self.contract_demand_85_percent = 0
        self.billing_demand_constant = 100
        self.highest_billing_demand = 0.0
        self.energy_unit_charges = 4.10
        self.billing_demand_to_contract_demand = 25
        self.billing_demand_excess_contract_demand = 50
        self.charges = 0
        self.demand_charges = 0
        self.energy_charges = 0
        self.total_charge = 0

    def billing_demand(self, max_demand, contract_demand, billing_demand_constant):
        self.highest_billing_demand = max(max_demand, contract_demand, billing_demand_constant)
        return float(self.highest_billing_demand)

    def energy_charges_ev_ht(self, units, charges):
        self.energy_charges = units * charges

    def demand_charges_ev_ht(self, billing_demand, contract_demand, months):
        if billing_demand <= contract_demand:
            self.charges = self.billing_demand_to_contract_demand
        elif billing_demand > contract_demand:
            self.charges = self.billing_demand_excess_contract_demand
        self.demand_charges = self.charges * billing_demand * months

    def total_ev_ht_charges(self, energy_charges, demand_charges):
        """  Tariff for EV: HT- Electric Vehicle Charging Stations. """
        self.total_charge = energy_charges + demand_charges
        print(f"Energy Charges: ₹ {energy_charges:.2f}")
        print("Demand Charges: ₹", demand_charges)
        print("Total Charges: ₹", self.total_charge)

    def ev_ht(self):
        self.contract_demand_85_percent = self.contract_demand * 0.85
        self.billing_demand(self.max_demand, self.contract_demand_85_percent, self.billing_demand_constant)
        self.energy_charges_ev_ht(self.unit, self.energy_unit_charges)
        self.demand_charges_ev_ht(self.highest_billing_demand, self.contract_demand, self.months)
        print("\nEV: HT- Electric Vehicle Charging Stations")
        self.total_ev_ht_charges(self.energy_charges, self.demand_charges)
