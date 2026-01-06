
# Calculations for Ammonium Nitrogen in cheese samples (2.3)

# We are going to use the following equation:
# ammonium_N=(1.40*C*(V_sample-V_0))/sample_mass

# Where:
# C = concentration of HCl [mol/L]
# V_blank = volume of titrant used for blank [mL]
# V_sample = volume of titrant used for sample [mL]
# sample_mass = mass of the cheese sample [g]

C=0.10
V_blank_1=0.11
V_blank_2=0.04
V_sample_1=4.13
V_sample_2=5.20
sample_mass_1=2.5740
sample_mass_2=2.5782

ammonium_N_1=(1.40*C*(V_sample_1-V_blank_1))/sample_mass_1
ammonium_N_2=(1.40*C*(V_sample_2-V_blank_2))/sample_mass_2


print(f"Ammonium Nitrogen for sample 1: {ammonium_N_1:.4f} N% (w/w)")
print(f"Ammonium Nitrogen for sample 2: {ammonium_N_2:.4f} N% (w/w)")
