from compressors.reciprocating.model import CompressorModel

if __name__ == "__main__":

    parameters = {  'bore diameter' : 0.780,
                    'stroke' : 0.33,
                    'connecting rod length' : 1.25,
                    'rod diameter' : 0.135,
                    'pressure ratio' : 1.90788804,
                    'clearance (HE)' : 15.8,
                    'clearance (CE)' : 18.39,
                    'TDC crank angle 1' : 0,
                    'rotational speed' : 360,
                    'capacity' : 100,
                    'acting label' : 0,
                    'pressure at suction' : 19.65,
                    'temperature at suction' : 45,
                    'pressure unit' : "bar",
                    'temperature unit' : "°C",
                    'isentropic exponent' : 1.400,
                    'molar mass' : 2.01568 }

    compressor = CompressorModel(parameters)
    compressor.set_fluid_properties_and_update_state(   parameters['isentropic exponent'],
                                                        parameters['molar mass']   )

    compressor.number_of_cylinders = 1
    compressor.number_points = 2000

    compressor.plot_PV_diagram_both_ends()

    # rho_suc = cylinder.rho_suc
    # compressor.plot_rod_pressure_load_frequency(6)
    # compressor.plot_PV_diagram_head_end()

    # mass_in = compressor.get_in_mass_flow()
    # mass_out = compressor.get_out_mass_flow()
    # total_mass = compressor.total_mass_flow()
    # print(mass_in, mass_out, 200*(mass_in-mass_out)/(mass_in+mass_out))
    # print(total_mass)

    # cap = cap/100
    # res_cap = compressor.process_capacity(capacity=cap)
    # print(res_cap)

    # mass_flow_full_capacity = -np.mean(compressor.process_sum_of_volumetric_flow_rate('in_flow', capacity=1))*rho_suc
    # partial_flow = -np.mean(compressor.process_sum_of_volumetric_flow_rate('in_flow', capacity=res_cap))*rho_suc
    # print((partial_flow/mass_flow_full_capacity)*100)