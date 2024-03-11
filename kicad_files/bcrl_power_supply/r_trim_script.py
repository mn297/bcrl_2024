def compute_rtrim_pdq10_q48_s5(Vo_desired):
    # Replace the following values with actual measurements or desired values
    Vr = 2.5  # Reference voltage
    R1 = 2320  # Resistance in ohms
    R2 = 2320  # Resistance in ohms
    R3 = 0  # Resistance in ohms
    Vo_nom = 5  # Nominal output voltage
    Rt = 8200  # Trim resistor in ohms

    # Calculate trim resistors
    rtrim_up = ((Vr * R1 * (R2 + R3)) / ((Vo_desired - Vo_nom) * R2)) - Rt
    rtrim_down = R1 * ((Vr * R1) / ((Vo_nom - Vo_desired) * R2) - 1) - Rt
    print(f"pdq10_q48_s5 For Vo = {Vo_desired}V:")
    print(f"    R_trim_up = {rtrim_up} Ω")
    print(f"    R_trim_down = {rtrim_down} Ω")


compute_rtrim_pdq10_q48_s5(5.5)
compute_rtrim_pdq10_q48_s5(4.5)


def compute_rtrim_pqc50(Vnom, Vout):
    delta_percent = abs(((Vnom - Vout) / Vnom) * 100)

    rtrim_up = (
        ((5.11 * Vnom * (100 + delta_percent)) / (1.225 * delta_percent))
        - (511 / delta_percent)
        - 10.22
    )
    rtrim_down = (511 / delta_percent) - 10.22
    # print(f"delta_percent: {delta_percent}%")
    print(f"pqc50 For Vo = {Vout}V:")
    print(f"    Rtrim Up: {rtrim_up * 1000} Ω")
    print(f"    Rtrim Down: {rtrim_down * 1000} Ω")


# Replace these with your actual values
Vnom = 5.0  # Nominal voltage
Vout_up = 8  # Desired output voltage
compute_rtrim_pqc50(Vnom, Vout_up)
