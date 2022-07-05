# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 13:32:19 2022

@author: frank
"""

config = {
"model_name" : 'WBmodel2_toy_model',
"train_data" : 'D:/File_X/PHD/AILAB/ASPECT_class/data/wholebrain_CT_pytorch_dataset_ASPECTSCrop_DS',
"valid_data" : 'D:/File_X/PHD/AILAB/ASPECT_class/data/wholebrain_CT_pytorch_testing_dataset_ASPECTSCrop_DS',
'pre_align': False,
'skull_strip': False,
"use_pretrained": False,
'half_precision': False,
"z_crop": False,
"logdir": 'cpts',
"trained_model" : 'vol_checkpoint_WBmodel_ndSE_SEres7altBN_1ch_alt_20220505_2319.pt',
"restart": False,
"freeze_enc": False,
"trained_swa_model": None,
"scheduler": 'ExponentialLR', 
"cyclic_epochs":  1,
"cyclic_mult":  2,
"seed" :  0,
"num_class" :  2,
"epoch" :  1,
"es_patience" :  300,
"batch_size" :  3,
"loss_beta" :  0.999,
"aug_Rrange" :  15,
"aug_Trange" :  0.02,
'aug_hflip': False, 
'aug_vflip': False, 
"batch_per_update" :  1,
 "num_test_aug" :  1,
'test_aug_agg': 'mean', 
"Learning_rate" :  5e-4,
"lr_gamma" :  0.977,
"momentum" :  0.9,
"weight_decay" :  5e-9,
"class_threshold" :  0.5,
'use_SWA_model': False, 
'no_SWA_scheduler': False, 
'epoch_per_SWA': 1,
'batch_per_SWA': 0, 
'optimizer': 'Adam',
'swa_scheduler': 'SWALR',
'swa_lr': 5e-5, 
'lr_min': 1e-6, 
'SWA_start_epoch': 175, 
'lossfun': 'BinaryFocalLoss_2',
'output_CAM': True
        
    }

import yaml

with open('store_file.yaml', 'w') as file:
    documents = yaml.dump(config, file)
    
with open('store_file.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    param_dict = yaml.load(file, Loader=yaml.FullLoader)

    print(param_dict)
    
    
# def write_yaml():
#     with open('data.yaml', encoding= 'utf-8', mode = 'w') as f:
#         try:
#             yaml.dump(data = config, stream = f, allow_unicode=True)
#         except Exception as e:
#             print(e)
            
# write_yaml()     

    
# def read_yaml(path):
#     file = open(path, 'r', encoding='utf-8')
#     string = file.read()
#     dict = yaml.safe_load(string)

#     return dict

# read_yaml('data.yaml')