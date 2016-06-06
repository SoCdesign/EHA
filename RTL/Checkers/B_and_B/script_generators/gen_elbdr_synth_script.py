# copyright 2016 Siavoosh Payandeh Azad and Behrad Niazmand


def gen_elbdr_checker_top(checker_id):

    name_string = ""
    for i in checker_id:
        name_string += str(i)+"_"
    #print name_string[:len(name_string)-1]
    elbdr_synth_script = open("synthesis_scripts/ELBDR_with_checkers_"+name_string[:len(name_string)-1]+"_synthesis.script", 'w')

    elbdr_synth_script.write("/* Bus Naming variables */\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("bus_naming_style = \"%s<%d>\"\n")
    elbdr_synth_script.write("bus_dimension_separator_style = \"><\"\n")
    elbdr_synth_script.write("bus_range_separator_style = \":\" \n")
    elbdr_synth_script.write("bus_extraction_style = \"%s<%d:%d>\"\n")
    elbdr_synth_script.write(" \n")
    elbdr_synth_script.write("/* Power and Ground variables */\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("edifin_ground_net_name = \"gnd!\"\n")
    elbdr_synth_script.write("edifin_ground_net_property_name = \"\"\n")
    elbdr_synth_script.write("edifin_ground_net_property_value = \"\"\n")
    elbdr_synth_script.write("edifout_ground_name = \"gnd\"\n")
    elbdr_synth_script.write("edifout_ground_net_name = \"gnd!\"\n")
    elbdr_synth_script.write("edifout_ground_net_property_name = \"\"\n")
    elbdr_synth_script.write("edifout_ground_net_property_value = \"\"\n")
    elbdr_synth_script.write("edifout_ground_pin_name = \"gnd!\"\n")
    elbdr_synth_script.write("edifin_power_net_name = \"vdd!\"\n")
    elbdr_synth_script.write("edifin_power_net_property_name = \"\"\n")
    elbdr_synth_script.write("edifin_power_net_property_value = \"\"\n")
    elbdr_synth_script.write("edifout_power_name = \"vdd\"\n")
    elbdr_synth_script.write("edifout_power_net_name = \"vdd!\"\n")
    elbdr_synth_script.write("edifout_power_net_property_name = \"\"\n")
    elbdr_synth_script.write("edifout_power_net_property_value = \"\"\n")
    elbdr_synth_script.write("edifout_power_pin_name = \"vdd!\"\n")
    elbdr_synth_script.write("edifout_power_and_ground_representation = \"net\"\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("/* Net to Port Connection variables */\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("edifin_autoconnect_ports = \"true\"\n")
    elbdr_synth_script.write("compile_fix_multiple_port_nets = \"true\"\n")
    elbdr_synth_script.write("single_group_per_sheet = \"true\"\n")
    elbdr_synth_script.write("use_port_name_for_oscs = \"false\"\n")
    elbdr_synth_script.write("write_name_nets_same_as_ports = \"true\"\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("/* Output variables */\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("edifout_netlist_only = \"true\"\n")
    elbdr_synth_script.write("edifout_instantiate_ports = \"true\"\n")
    elbdr_synth_script.write("edifout_pin_name_propery_name = \"pinName\"\n")
    elbdr_synth_script.write(" \n")
    elbdr_synth_script.write("/* Important! */\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("edifout_numerical_array_members = \"true\" \n")
    elbdr_synth_script.write("edifout_no_array = \"false\"\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("/********************************************/\n")
    elbdr_synth_script.write("/*  Now starts the synthesis:               */\n")
    elbdr_synth_script.write("/********************************************/\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("/* ================================================= */\n")
    elbdr_synth_script.write("/* Don't use the following cells!!                   */\n")
    elbdr_synth_script.write("/* ================================================= */\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("set_dont_use { class/EO, class/EN, class/EOP, class/ENP, class/EO3, class/EN3, "
                             "class/EO3P, class/EN3P, class/EOI, class/ENI, class/FD1S, class/FD2S, class/FD4S, "
                             "class/IVDA, class/IVDAP, class/B2I, class/B2IP, class/B3I, class/B3IP, class/AO4P, "
                             "class/NR*, class/EO1P, class/ND*}\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("analyze -format vhdl ELBDR_pseudo.vhd\n")
    elbdr_synth_script.write("analyze -format vhdl elbdr_checker"+name_string[:len(name_string)-1]+".vhd\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("analyze -format vhdl elbdr_checker"+name_string[:len(name_string)-1]+"_top.vhd\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("elaborate ELBDR_with_checkers_top -update\n")
    elbdr_synth_script.write("current_design = ELBDR_with_checkers_top\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("link\n")
    elbdr_synth_script.write("compile\n")
    elbdr_synth_script.write("\n")
    elbdr_synth_script.write("write -format edif -hierarchy -output ELBDR_with_checkers_top.edif\n")
    elbdr_synth_script.write("report_area > area"+name_string[:len(name_string)-1]+".txt\n")
    elbdr_synth_script.write("exit\n")

    elbdr_synth_script.close()