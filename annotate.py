import os
import settings
import pandas as pd

with open(os.path.join(settings.PROCESSED_DIR, "alldata.txt"), 'r') as f:
for i, line in enumerate(f):  #skip header
            if i == 0:
            
