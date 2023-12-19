import numpy as np

def error(real_dict : dict, test_dict : dict, shots : int):
    """
        This function compare two types of dictionaries 
        to compare. 
        Input:
            real_dict : dict ; perfect result.
            test_dict : dict ; noise dict.
            shots : int : number of shots.
        Output: 
            err : int ; error between the dictionaties.
    """
    err = 0
    real_list = list(real_dict.keys())
    test_list = list(test_dict.keys())

    for i in range(0, len(real_list)):

        test_dict.setdefault(real_list[i], 0)
        real_dict.setdefault(test_list[i], 0)
    
    real_list = list(real_dict.keys())
    test_list = list(test_dict.keys())

    for k in range(0, len(real_list)):
        err += np.abs(test_dict[real_list[k]]-real_dict[real_list[k]])
    
    return err/shots