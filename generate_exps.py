import os
import json

with open('./exps/default2.json', 'r') as f:
    config = json.load(f)

config_combination = {
    "tuned_epoch": [5, 10, 50],
    "init_lr": [0.001, 0.05, 0.1],
    "batch_size": [16, 64, 128],
    "weight_decay": [0.0001, 0.001, 0.01],
    "min_lr": [0.001, 0.01, 0.1],
    "optimizer": ["adam"],
    "vpt_type": ["shallow"],
    "prompt_token_num": [2, 8, 20],
    "loss_function": ["focal_loss"],
    "transforms_mode": ["random"]
}

config_attribute = "transforms_mode"

for item in config_combination[config_attribute]:
    
    config[config_attribute] = item
    
    filename = f"customcil_{config_attribute}"
    
    for key,con in config_combination.items():
        filename +=  f"_{key}_{config[key]}"

    config["name"] = filename

    os.makedirs(f'./exps/generated/{config_attribute}', exist_ok=True) 

    with open(f'./exps/generated/{config_attribute}/{filename}.json', 'w') as f:        
        json.dump(config, f, indent=4)