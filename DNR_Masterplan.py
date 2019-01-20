
import re

import os
import math
########### Functions ##############

def machine_num_decider():

    File_Name = r"..\Path_PlanFileNumber_Sku.txt"
    input_list = []
    with open(File_Name, "r") as feeder:
        for line in feeder.readlines():
            input_list.append(line)

    return int(input_list[1].rstrip("\n"))
    # if sku == "bel30":
    #     machine_num = 20
    #     return machine_num
    # if sku == "belacct":
    #     machine_num = 20
    #     return machine_num
    # else:
    #     pass

def Path_return():

    File_Name = r"..\Path_PlanFileNumber_Sku.txt"
    input_list = []
    with open(File_Name, "r") as feeder:
        for line in feeder.readlines():
            input_list.append(line)

    return input_list[0].rstrip("\n")

def Sku_return():

    File_Name = r"..\Path_PlanFileNumber_Sku.txt"
    input_list = []
    with open(File_Name, "r") as feeder:
        for line in feeder.readlines():
            input_list.append(line)

    return input_list[2].rstrip("\n")
def return_testcase_name (ScriptPath):
    script_path_formatted = ScriptPath.rstrip('\n')
    try:
        with open(r'{}'.format(script_path_formatted), 'r', encoding='utf-8', errors='ignore')as tfile:
            for line in tfile:
                if (("[-]" or "[+]") and "testcase") in line: # and ("//testcase" or "// testcase") not in line:
                    if "[-]" in line:
                        test_case_name = line.replace("[-] testcase","").strip().split(" ")[0]
                        return test_case_name
                    if "[+]" in line:
                        test_case_name = line.replace("[+] testcase","").strip().split(" ")[0]
                        return test_case_name
    except:
        print("Could not find the Test Case Name in test script {}".format(ScriptPath))

def return_script_full_path(scriptName):

    latest_Masterplan_file = r"..\MasterplanFinal.txt"
    scriptName_with_ext = scriptName+".t"
    Script_name_Match = True
    with open(latest_Masterplan_file, 'r', encoding='utf-8', errors='ignore')as MPfile:
        for line in MPfile:
            line_small = line.lower()
            if scriptName_with_ext.lower() in line_small:
                if "[ ]" in line:
                    script_full_path = line.split(" ")[-1]
                    return script_full_path
                else:
                    return line_small
            else:
                Script_name_Match = False

    if Script_name_Match == False:
        raise ValueError("Cound not find the path for script name {}".format(scriptName))


def return_ScriptName_Count(scriptName):
    scrpt_name_list = []
    with open(r'{}'.format(scriptName), 'r', encoding='utf-8', errors='ignore')as ScriptNamesFile:
        for script_name in ScriptNamesFile:
            scrpt_name_list.append(script_name)
        return scrpt_name_list




def write_to_planfiles(planfile_name,scriptName): # Remove the parameter and activate master plan file to write a complete master plan file
    Script_Name_File = "Script_Name.txt"
    #Master_plan_file_all = "Masterplan_Output.pln"

    with open(r'{}'.format(planfile_name), 'a', encoding='utf-8', errors='ignore')as MP_OP_File:
        #with open(scriptName, 'r', encoding='utf-8', errors='ignore')as SNFile: # This line need to take the names form plan_file_creator function
        #for script_Name in SNFile:  # Remove this for loop as this will loop with in planfile creator
        complete_script_path = return_script_full_path(r'{}'.format(scriptName).strip())
        test_case_name = return_testcase_name(r'{}'.format(complete_script_path))
        MP_OP_File.write("[-] {}\n".format(test_case_name))
        MP_OP_File.write("\t[ ] script: {}".format(complete_script_path))
        MP_OP_File.write("\t[ ] testcase: {}\n".format(test_case_name))
        MP_OP_File.write("\n")


def plan_file_creator():
    Script_Name_File = r"..\Script_Name.txt"

    machine_num = machine_num_decider()
    Sku = Sku_return()
    Path = Path_return()


    final_path= Path+'\{}'.format(Sku)
    if not os.path.exists(final_path):
        os.makedirs(final_path)


    All_script_name_list = return_ScriptName_Count(Script_Name_File)

    total_script_count = len(All_script_name_list)

    if total_script_count > machine_num:
        scripts_per_machine_floored = int(math.floor(total_script_count / machine_num))
    else:
        scripts_per_machine_floored = int(math.ceil(total_script_count / machine_num))
    extra_script_after_floor = total_script_count - (machine_num * scripts_per_machine_floored)
    left_machines = (total_script_count-extra_script_after_floor)
    total_machines = machine_num

    for mn in range(0,machine_num):

        sub_plan_file_name = 'plan_{}.pln'.format(mn + 1)
        complete_path_plan_file = final_path + r'\{}'.format(sub_plan_file_name)

        starting_file = (mn * scripts_per_machine_floored)
        ending_file = (mn * scripts_per_machine_floored) + scripts_per_machine_floored


        for sn in range(starting_file,ending_file):
            script_name = All_script_name_list[sn]
            sn_remove_n = script_name.rstrip('\n')
            write_to_planfiles(complete_path_plan_file,sn_remove_n)


    for mn in range(0, extra_script_after_floor):
        #print("Entering second for loop")
        sub_plan_file_name = 'plan_{}.pln'.format(mn + 1)
        complete_path_plan_file = final_path + r'\{}'.format(sub_plan_file_name)

        starting_file = (total_machines * scripts_per_machine_floored)
        ending_file = total_script_count


        rem_script_loc = starting_file + mn
        script_name = All_script_name_list[rem_script_loc]
        sn_remove_n = script_name.rstrip('\n')
        write_to_planfiles(complete_path_plan_file, sn_remove_n)



















# Testing Zone
#script_path = return_script_full_path("BatchEnterTransactions_10.t")
# testcase_Name = return_testcase_name(r"c:\qap\silkscripts\accountant\dataexchange\data_verification\dataverification_lists_customer_edit_001.t")
# print(testcase_Name)

# print(script_path)
#
# Script_Name_File = "Script_Name.txt"
# Master_Plan_File = "Masterplan.pln"


# Info Zone
# [-] AccountantsCopy_qbx_qba_CheckTransactions
# 	[ ] script: TC_01_AccountantsCopy_qbx_qba_CheckTransactions.t
# 	[ ] testcase: TC_01_AccountantsCopy_qbx_qba_CheckTransactions


#return_ScriptName_Count_test = return_ScriptName_Count("Script_Name.txt")
# print(return_ScriptName_Count_test)
# print(len(return_ScriptName_Count_test))

plan_file_creator()
