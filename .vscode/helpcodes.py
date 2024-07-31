#HOME ERROR
# $env:HOME = $env:USERPROFILE

# python -m megapose.scripts.run_inference_on_example barbecue-sauce --run-inference  
#os.environ['MKL_NUM_THREADS'] = '6'  # Adjust based on the number of CPU cores you have
#os.environ['OMP_NUM_THREADS'] = '6'

import torch
print(torch.cuda.is_available)