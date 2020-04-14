\ENCODING=ISO-8859-1
\Problem name: 

Minimize
 cost: ACALD#0 + ACALD_rev#1 + ACALDt#2 + ACALDt_rev#3 + ACKr#4 + ACKr_rev#5
       + ACONTa#6 + ACONTa_rev#7 + ACONTb#8 + ACONTb_rev#9 + ACt2r#10
       + ACt2r_rev#11 + ADK1#12 + ADK1_rev#13 + AKGDH#14 + AKGt2r#15
       + AKGt2r_rev#16 + ALCD2x#17 + ALCD2x_rev#18 + ATPM#19 + ATPS4r#20
       + ATPS4r_rev#21 + BIOMASS_Ecoli_core_w_GAM#22 + CO2t#23 + CO2t_rev#24
       + CS#25 + CYTBD#26 + D_LACt2#27 + D_LACt2_rev#28 + _ENO#29 + _ENO_rev#30
       + _ETOHt2r#31 + _ETOHt2r_rev#32 + _EX_ac_e#33 + _EX_acald_e#34
       + _EX_akg_e#35 + _EX_co2_e#36 + _EX_co2_e_rev#37 + _EX_etoh_e#38
       + _EX_for_e#39 + _EX_fru_e#40 + _EX_fum_e#41 + _EX_glc__D_e#42
       + _EX_glc__D_e_rev#43 + _EX_gln__L_e#44 + _EX_glu__L_e#45 + _EX_h_e#46
       + _EX_h_e_rev#47 + _EX_h2o_e#48 + _EX_h2o_e_rev#49 + _EX_lac__D_e#50
       + _EX_mal__L_e#51 + _EX_nh4_e#52 + _EX_nh4_e_rev#53 + _EX_o2_e#54
       + _EX_o2_e_rev#55 + _EX_pi_e#56 + _EX_pi_e_rev#57 + _EX_pyr_e#58
       + _EX_succ_e#59 + FBA#60 + FBA_rev#61 + FBP#62 + FORt2#63 + FORt#64
       + FRD7#65 + FRUpts2#66 + FUM#67 + FUM_rev#68 + FUMt2_2#69 + G6PDH2r#70
       + G6PDH2r_rev#71 + GAPD#72 + GAPD_rev#73 + GLCpts#74 + GLNS#75
       + GLNabc#76 + GLUDy#77 + GLUDy_rev#78 + GLUN#79 + GLUSy#80 + GLUt2r#81
       + GLUt2r_rev#82 + GND#83 + H2Ot#84 + H2Ot_rev#85 + ICDHyr#86
       + ICDHyr_rev#87 + ICL#88 + LDH_D#89 + LDH_D_rev#90 + MALS#91
       + MALt2_2#92 + MDH#93 + MDH_rev#94 + ME1#95 + ME2#96 + NADH16#97
       + NADTRHD#98 + NH4t#99 + NH4t_rev#100 + O2t#101 + O2t_rev#102 + PDH#103
       + PFK#104 + PFL#105 + PGI#106 + PGI_rev#107 + PGK#108 + PGK_rev#109
       + PGL#110 + PGM#111 + PGM_rev#112 + PIt2r#113 + PIt2r_rev#114 + PPC#115
       + PPCK#116 + PPS#117 + PTAr#118 + PTAr_rev#119 + PYK#120 + PYRt2#121
       + PYRt2_rev#122 + RPE#123 + RPE_rev#124 + RPI#125 + RPI_rev#126
       + SUCCt2_2#127 + SUCCt3#128 + SUCDi#129 + SUCOAS#130 + SUCOAS_rev#131
       + TALA#132 + TALA_rev#133 + THD2#134 + TKT1#135 + TKT1_rev#136
       + TKT2#137 + TKT2_rev#138 + TPI#139 + TPI_rev#140
Subject To
 c1:  ACALD#0 - ACALD_rev#1 - 3.7478 BIOMASS_Ecoli_core_w_GAM#22 - CS#25
      - MALS#91 + PDH#103 + PFL#105 - PTAr#118 + PTAr_rev#119  = 0
 c2:  - ACALD#0 + ACALD_rev#1 + ACALDt#2 - ACALDt_rev#3 + ALCD2x#17
      - ALCD2x_rev#18  = 0
 c3:  - ACALD#0 + ACALD_rev#1 - AKGDH#14 + 3.7478 BIOMASS_Ecoli_core_w_GAM#22
      + CS#25 + MALS#91 - PDH#103 - PFL#105 + PTAr#118 - PTAr_rev#119
      - SUCOAS#130 + SUCOAS_rev#131  = 0
 c4:  ACALD#0 - ACALD_rev#1 + ACt2r#10 - ACt2r_rev#11 + AKGt2r#15
      - AKGt2r_rev#16 + ALCD2x#17 - ALCD2x_rev#18 + ATPM#19 + 3 ATPS4r#20
      - 3 ATPS4r_rev#21 + 59.81 BIOMASS_Ecoli_core_w_GAM#22 + CS#25
      - 2 CYTBD#26 + D_LACt2#27 - D_LACt2_rev#28 + _ETOHt2r#31
      - _ETOHt2r_rev#32 + FORt2#63 + 2 FUMt2_2#69 + G6PDH2r#70 - G6PDH2r_rev#71
      + GAPD#72 - GAPD_rev#73 + GLNS#75 + GLNabc#76 + GLUDy#77 - GLUDy_rev#78
      - GLUSy#80 + GLUt2r#81 - GLUt2r_rev#82 + LDH_D#89 - LDH_D_rev#90
      + MALS#91 + 2 MALt2_2#92 + MDH#93 - MDH_rev#94 - 4 NADH16#97 + PFK#104
      + PGL#110 + PIt2r#113 - PIt2r_rev#114 + PPC#115 + 2 PPS#117 - PYK#120
      + PYRt2#121 - PYRt2_rev#122 + 2 SUCCt2_2#127 + SUCCt3#128 + 2 THD2#134
       = 0
 c5:  - ACALD#0 + ACALD_rev#1 - AKGDH#14 - ALCD2x#17 + ALCD2x_rev#18
      - 3.547 BIOMASS_Ecoli_core_w_GAM#22 - GAPD#72 + GAPD_rev#73 - LDH_D#89
      + LDH_D_rev#90 - MDH#93 + MDH_rev#94 - ME1#95 + NADH16#97 - NADTRHD#98
      - PDH#103 + THD2#134  = 0
 c6:  ACALD#0 - ACALD_rev#1 + AKGDH#14 + ALCD2x#17 - ALCD2x_rev#18
      + 3.547 BIOMASS_Ecoli_core_w_GAM#22 + GAPD#72 - GAPD_rev#73 + LDH_D#89
      - LDH_D_rev#90 + MDH#93 - MDH_rev#94 + ME1#95 - NADH16#97 + NADTRHD#98
      + PDH#103 - THD2#134  = 0
 c7:  - ACALDt#2 + ACALDt_rev#3 - _EX_acald_e#34  = 0
 c8:  - ACKr#4 + ACKr_rev#5 + ACt2r#10 - ACt2r_rev#11  = 0
 c9:  ACKr#4 - ACKr_rev#5 + PTAr#118 - PTAr_rev#119  = 0
 c10: - ACKr#4 + ACKr_rev#5 - ADK1#12 + ADK1_rev#13 - ATPM#19 + ATPS4r#20
      - ATPS4r_rev#21 - 59.81 BIOMASS_Ecoli_core_w_GAM#22 - GLNS#75 - GLNabc#76
      - PFK#104 - PGK#108 + PGK_rev#109 - PPCK#116 - PPS#117 + PYK#120
      - SUCOAS#130 + SUCOAS_rev#131  = 0
 c11: ACKr#4 - ACKr_rev#5 + 2 ADK1#12 - 2 ADK1_rev#13 + ATPM#19 - ATPS4r#20
      + ATPS4r_rev#21 + 59.81 BIOMASS_Ecoli_core_w_GAM#22 + GLNS#75 + GLNabc#76
      + PFK#104 + PGK#108 - PGK_rev#109 + PPCK#116 - PYK#120 + SUCOAS#130
      - SUCOAS_rev#131  = 0
 c12: ACONTa#6 - ACONTa_rev#7 - ACONTb#8 + ACONTb_rev#9 - ATPM#19 + ATPS4r#20
      - ATPS4r_rev#21 - 59.81 BIOMASS_Ecoli_core_w_GAM#22 - CS#25 + CYTBD#26
      + _ENO#29 - _ENO_rev#30 - FBP#62 - FUM#67 + FUM_rev#68 - GLNabc#76
      - GLUDy#77 + GLUDy_rev#78 - GLUN#79 + H2Ot#84 - H2Ot_rev#85 - MALS#91
      - PGL#110 - PPC#115 - PPS#117  = 0
 c13: - ACONTa#6 + ACONTa_rev#7 + CS#25  = 0
 c14: ACONTa#6 - ACONTa_rev#7 - ACONTb#8 + ACONTb_rev#9  = 0
 c15: ACONTb#8 - ACONTb_rev#9 - ICDHyr#86 + ICDHyr_rev#87 - ICL#88  = 0
 c16: - ACt2r#10 + ACt2r_rev#11 - AKGt2r#15 + AKGt2r_rev#16 - 4 ATPS4r#20
      + 4 ATPS4r_rev#21 + 2 CYTBD#26 - D_LACt2#27 + D_LACt2_rev#28
      - _ETOHt2r#31 + _ETOHt2r_rev#32 - _EX_h_e#46 + _EX_h_e_rev#47 - FORt2#63
      - 2 FUMt2_2#69 - GLUt2r#81 + GLUt2r_rev#82 - 2 MALt2_2#92 + 3 NADH16#97
      - PIt2r#113 + PIt2r_rev#114 - PYRt2#121 + PYRt2_rev#122 - 2 SUCCt2_2#127
      - SUCCt3#128 - 2 THD2#134  = 0
 c17: - ACt2r#10 + ACt2r_rev#11 - _EX_ac_e#33  = 0
 c18: - ADK1#12 + ADK1_rev#13 + PPS#117  = 0
 c19: - AKGDH#14 + AKGt2r#15 - AKGt2r_rev#16
      + 4.1182 BIOMASS_Ecoli_core_w_GAM#22 + GLUDy#77 - GLUDy_rev#78 - GLUSy#80
      + ICDHyr#86 - ICDHyr_rev#87  = 0
 c20: AKGDH#14 + SUCOAS#130 - SUCOAS_rev#131  = 0
 c21: AKGDH#14 + CO2t#23 - CO2t_rev#24 + GND#83 + ICDHyr#86 - ICDHyr_rev#87
      + ME1#95 + ME2#96 + PDH#103 - PPC#115 + PPCK#116  = 0
 c22: - AKGt2r#15 + AKGt2r_rev#16 - _EX_akg_e#35  = 0
 c23: - ALCD2x#17 + ALCD2x_rev#18 + _ETOHt2r#31 - _ETOHt2r_rev#32  = 0
 c24: ATPM#19 - ATPS4r#20 + ATPS4r_rev#21 + 59.81 BIOMASS_Ecoli_core_w_GAM#22
      + FBP#62 - GAPD#72 + GAPD_rev#73 + GLNS#75 + GLNabc#76 + PIt2r#113
      - PIt2r_rev#114 + PPC#115 + PPS#117 - PTAr#118 + PTAr_rev#119
      + SUCOAS#130 - SUCOAS_rev#131  = 0
 c25: - 4.9414 BIOMASS_Ecoli_core_w_GAM#22 - GLNS#75 - GLUDy#77 + GLUDy_rev#78
      + GLUN#79 + 2 GLUSy#80 + GLUt2r#81 - GLUt2r_rev#82  = 0
 c26: - 0.129 BIOMASS_Ecoli_core_w_GAM#22 + FBA#60 - FBA_rev#61 - GAPD#72
      + GAPD_rev#73 - TALA#132 + TALA_rev#133 + TKT1#135 - TKT1_rev#136
      + TKT2#137 - TKT2_rev#138 + TPI#139 - TPI_rev#140  = 0
 c27: - 0.361 BIOMASS_Ecoli_core_w_GAM#22 + TALA#132 - TALA_rev#133 - TKT2#137
      + TKT2_rev#138  = 0
 c28: - 0.8977 BIOMASS_Ecoli_core_w_GAM#22 - RPI#125 + RPI_rev#126 - TKT1#135
      + TKT1_rev#136  = 0
 c29: - 0.0709 BIOMASS_Ecoli_core_w_GAM#22 + FBP#62 + FRUpts2#66 - PFK#104
      + PGI#106 - PGI_rev#107 + TALA#132 - TALA_rev#133 + TKT2#137
      - TKT2_rev#138  = 0
 c30: - 2.8328 BIOMASS_Ecoli_core_w_GAM#22 + FRUpts2#66 + GLCpts#74 + LDH_D#89
      - LDH_D_rev#90 + ME1#95 + ME2#96 - PDH#103 - PFL#105 - PPS#117 + PYK#120
      + PYRt2#121 - PYRt2_rev#122  = 0
 c31: - 0.205 BIOMASS_Ecoli_core_w_GAM#22 - G6PDH2r#70 + G6PDH2r_rev#71
      + GLCpts#74 - PGI#106 + PGI_rev#107  = 0
 c32: - 1.7867 BIOMASS_Ecoli_core_w_GAM#22 - CS#25 + MDH#93 - MDH_rev#94
      + PPC#115 - PPCK#116  = 0
 c33: - 1.496 BIOMASS_Ecoli_core_w_GAM#22 - PGK#108 + PGK_rev#109 + PGM#111
      - PGM_rev#112  = 0
 c34: - 0.5191 BIOMASS_Ecoli_core_w_GAM#22 + _ENO#29 - _ENO_rev#30 - FRUpts2#66
      - GLCpts#74 - PPC#115 + PPCK#116 + PPS#117 - PYK#120  = 0
 c35: - 0.2557 BIOMASS_Ecoli_core_w_GAM#22 + GLNS#75 + GLNabc#76 - GLUN#79
      - GLUSy#80  = 0
 c36: 13.0279 BIOMASS_Ecoli_core_w_GAM#22 - G6PDH2r#70 + G6PDH2r_rev#71
      - GLUDy#77 + GLUDy_rev#78 + GLUSy#80 - GND#83 - ICDHyr#86 + ICDHyr_rev#87
      - ME2#96 + NADTRHD#98 - THD2#134  = 0
 c37: - 13.0279 BIOMASS_Ecoli_core_w_GAM#22 + G6PDH2r#70 - G6PDH2r_rev#71
      + GLUDy#77 - GLUDy_rev#78 - GLUSy#80 + GND#83 + ICDHyr#86 - ICDHyr_rev#87
      + ME2#96 - NADTRHD#98 + THD2#134  = 0
 c38: - CO2t#23 + CO2t_rev#24 - _EX_co2_e#36 + _EX_co2_e_rev#37  = 0
 c39: - 0.5 CYTBD#26 + O2t#101 - O2t_rev#102  = 0
 c40: - CYTBD#26 - FRD7#65 + NADH16#97 + SUCDi#129  = 0
 c41: CYTBD#26 + FRD7#65 - NADH16#97 - SUCDi#129  = 0
 c42: - D_LACt2#27 + D_LACt2_rev#28 - _EX_lac__D_e#50  = 0
 c43: D_LACt2#27 - D_LACt2_rev#28 - LDH_D#89 + LDH_D_rev#90  = 0
 c44: - _ENO#29 + _ENO_rev#30 - PGM#111 + PGM_rev#112  = 0
 c45: - _ETOHt2r#31 + _ETOHt2r_rev#32 - _EX_etoh_e#38  = 0
 c46: - _EX_for_e#39 - FORt2#63 - FORt#64  = 0
 c47: - _EX_fru_e#40 - FRUpts2#66  = 0
 c48: - _EX_fum_e#41 - FUMt2_2#69  = 0
 c49: - _EX_glc__D_e#42 + _EX_glc__D_e_rev#43 - GLCpts#74  = 0
 c50: - _EX_gln__L_e#44 - GLNabc#76  = 0
 c51: - _EX_glu__L_e#45 - GLUt2r#81 + GLUt2r_rev#82  = 0
 c52: - _EX_h2o_e#48 + _EX_h2o_e_rev#49 - H2Ot#84 + H2Ot_rev#85  = 0
 c53: - _EX_mal__L_e#51 - MALt2_2#92  = 0
 c54: - _EX_nh4_e#52 + _EX_nh4_e_rev#53 - NH4t#99 + NH4t_rev#100  = 0
 c55: - _EX_o2_e#54 + _EX_o2_e_rev#55 - O2t#101 + O2t_rev#102  = 0
 c56: - _EX_pi_e#56 + _EX_pi_e_rev#57 - PIt2r#113 + PIt2r_rev#114  = 0
 c57: - _EX_pyr_e#58 - PYRt2#121 + PYRt2_rev#122  = 0
 c58: - _EX_succ_e#59 - SUCCt2_2#127 + SUCCt3#128  = 0
 c59: FBA#60 - FBA_rev#61 - TPI#139 + TPI_rev#140  = 0
 c60: - FBA#60 + FBA_rev#61 - FBP#62 + PFK#104  = 0
 c61: FORt2#63 + FORt#64 + PFL#105  = 0
 c62: FRD7#65 + ICL#88 + SUCCt2_2#127 - SUCCt3#128 - SUCDi#129 - SUCOAS#130
      + SUCOAS_rev#131  = 0
 c63: - FRD7#65 - FUM#67 + FUM_rev#68 + FUMt2_2#69 + SUCDi#129  = 0
 c64: FUM#67 - FUM_rev#68 + MALS#91 + MALt2_2#92 - MDH#93 + MDH_rev#94 - ME1#95
      - ME2#96  = 0
 c65: G6PDH2r#70 - G6PDH2r_rev#71 - PGL#110  = 0
 c66: GAPD#72 - GAPD_rev#73 + PGK#108 - PGK_rev#109  = 0
 c67: - GLNS#75 + GLUDy#77 - GLUDy_rev#78 + GLUN#79 + NH4t#99 - NH4t_rev#100
       = 0
 c68: - GND#83 + PGL#110  = 0
 c69: GND#83 - RPE#123 + RPE_rev#124 + RPI#125 - RPI_rev#126  = 0
 c70: ICL#88 - MALS#91  = 0
 c71: RPE#123 - RPE_rev#124 - TKT1#135 + TKT1_rev#136 - TKT2#137 + TKT2_rev#138
       = 0
 c72: - TALA#132 + TALA_rev#133 + TKT1#135 - TKT1_rev#136  = 0
 r1:  ACALD#0  = 1
End
