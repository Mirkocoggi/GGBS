import os
import sys
import math
import pandas as pd

def main():
    # Read results folder and check it exists
    try:
        RESULTS = sys.argv[1]
    except IndexError as ie:
        raise SystemError("Error: Specify results folder's name\n")
    if not os.path.exists(RESULTS):
        raise SystemError(f"Error: Folder {RESULTS} does not exist\n")
    
    # Read the tools and alignment experiments included in the evaluation
    TOOLS = [f for f in os.listdir(RESULTS)]
    ALIGNMENTS = [f for f in os.listdir(os.path.join(RESULTS,TOOLS[0]))]

    # Initialize results as a dict of dict
    RES_DICT = {x : {a : math.nan for a in ALIGNMENTS} for x in TOOLS}
    
    # Parse the timing results
    for tool in TOOLS:
        tmp_dir = os.path.join(RESULTS,tool)
        for al in ALIGNMENTS:
            exp_dir = os.path.join(tmp_dir,al)
            TIMING_FILES = [f for f in os.listdir(exp_dir) if f.endswith('_time.log')]
            if len(TIMING_FILES) != 0:
                tmp_res = 0.
                for f in TIMING_FILES:
                    tmp_file = os.path.join(exp_dir,f)
                    with open(tmp_file, 'r') as tf:
                        lines = tf.readlines()
                        if lines[0].startswith('\n'):
                            line = lines[1]
                            if 'real' in line:
                                time_str = line.split('\t')[-1]
                                minutes, seconds = time_str.split('m')
                                tmp_res += float(minutes)*60 + float(seconds[:-2]) 
                if tmp_res != 0.:
                    RES_DICT[tool][al] = tmp_res
    
    RES_DICT = pd.DataFrame.from_dict(RES_DICT, orient='index')
    RES_DICT.to_csv(f'{RESULTS}/summary_timing.csv')

    print(f'Summary results about execution time are saved in {RESULTS}/summary_timing.csv')


if __name__ == '__main__':
    main()