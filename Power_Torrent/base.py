class TorrentPower:

    def __init__(self):
        self.category_keys = ["1. RGP", "2. GPL",
                              "3. Non-RGP : Low Tension Service for Commercial and Industrial Purpose",
                              "4. LTP(AG) Agricultural Services",
                              "5. LTMD-1 : Low Tension Maximum Demand for Residential Purpose",
                              "6. LTMD-2 : Low Tension Maximum Demand for other than residential purpose",
                              "7. SL : Low Tension Tension Street Light Service",
                              "8. LEV : LT- Electric Vehicle Charging Stations",
                              "9. TMP : Low Tension Temporary Supply",
                              "10. HTMD-1 : High Tension Maximum Demand",
                              "11. HTMD-2 : High Tension Water and Sewage Pumping Stations run by AMC",
                              "12. HTMD-3 : High Tension Maximum Demand Temporary Supply",
                              "13. EV: HT- Electric Vehicle Charging Stations",
                              "14. HTMD - Metro Traction"]
        print("Category List -> ")
        for category in self.category_keys:
            print(category)
        self.input_category = input("Select a category (Sr. number) for calculating Tariff: ")
        self.user_selected_category = ""
        self.sub_category = ""

    def select_category(self):
        self.input_category = int(self.input_category)
        self.user_selected_category = self.category_keys[self.input_category - 1]
        print("selected category: ", self.user_selected_category)
        self.user_selected_category = self.user_selected_category.split(".")

        if "1" == self.user_selected_category[0]:
            print(self.user_selected_category)
            from r_g_p_residential_purpose import ResidentialPurpose
            rp_obj = ResidentialPurpose()
            self.sub_category = input("Enter sub category form residential purpose 1 for rgp and 2 for bpl: ")
            if self.sub_category == "1":
                rp_obj.rgp()
            elif self.sub_category == "2":
                rp_obj.bpl()
        elif "2" == self.user_selected_category[0]:
            from g_l_p import GeneralLightningPurpose
            glp_obj = GeneralLightningPurpose()
            glp_obj.glp()
        elif "3" == self.user_selected_category[0]:
            from non_r_g_p import NonRGP
            non_rgp_obj = NonRGP()
            non_rgp_obj.non_rgp()
        elif "4" == self.user_selected_category[0]:
            from l_t_p_agriculture_service import LTPAgricultureService
            ltp_ag_obj = LTPAgricultureService()
            ltp_ag_obj.ltp_agriculture_service()
        elif "5" == self.user_selected_category[0]:
            from ltmd import LTMD_1
            ltmd1_obj = LTMD_1()
            ltmd1_obj.ltmd_1()
            # from l_t_m_d_1 import LTMD_1
            # l_t_m_d_1_obj = LTMD_1()
            # l_t_m_d_1_obj.ltmd_1()
        elif "6" == self.user_selected_category[0]:
            from ltmd import LTMD_2
            ltmd2_obj = LTMD_2()
            ltmd2_obj.ltmd_2()
            # from l_t_m_d_2 import LTMD_2
            # l_t_m_d_2_obj = LTMD_2()
            # l_t_m_d_2_obj.ltmd_2()
        elif "7" == self.user_selected_category[0]:
            from s_l import StreetLightService
            s_l_obj = StreetLightService()
            s_l_obj.sl()
        elif "8" == self.user_selected_category[0]:
            from lev_lt import ElectricVehicleChargingStations
            lev_lt_obj = ElectricVehicleChargingStations()
            lev_lt_obj.lev_lt()
        elif "9" == self.user_selected_category[0]:
            from t_m_p import LowTensionTemporarySupply
            t_m_p_obj = LowTensionTemporarySupply()
            t_m_p_obj.tmp()
        elif "10" == self.user_selected_category[0]:
            from htmd import HTMD_1
            htmd_1_obj = HTMD_1()
            htmd_1_obj.htmd_1()
        elif "11" in self.user_selected_category[0]:
            from htmd import HTMD_2
            htmd_2_obj = HTMD_2()
            htmd_2_obj.htmd_2()
        elif "12" in self.user_selected_category[0]:
            from htmd import HTMD_3
            htmd_3_obj = HTMD_3()
            htmd_3_obj.htmd_3()
        elif "13" in self.user_selected_category[0]:
            from ev_ht import EV_HT
            ev_ht_obj = EV_HT()
            ev_ht_obj.ev_ht()
        elif "14" in self.user_selected_category[0]:
            from htmd import HTMD_Metro_Traction
            htmd_4_obj = HTMD_Metro_Traction()
            htmd_4_obj.htmd_metro_traction()


tp_obj = TorrentPower()
tp_obj.select_category()
