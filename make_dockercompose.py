import os
import yaml
from pathlib import Path
from datetime import datetime

N_THREADS = 8

DOCKER_COMPOSE_HEADER = '''\
version: '3.2'
services:
'''

SERVICE_TEMPLATE = '''
  {tool_lower}:
    stdin_open: true 
    tty: true
    build:
      context: ./
      dockerfile: Dockerfiles/{tool}/Dockerfile
    volumes:
      - type: bind
        source: ./results	
        target: /{tool}/results
      - type: bind
        source: ./input_data	
        target: /{tool}/input_data
    command:
      - /bin/bash 
      - -c
      - |        
'''

COMMAND_TEMPLATE = '        {{ time {COMMAND} {LOG} 2>&1 ; }} 2> {TIMING}\n'

COMMANDS = {
	'GraphAligner': 'GraphAligner -g {GRAPH} -f {READS} -a {OUTPUT} -x vg -t {THREADS}',
	'astarix': 'release/astarix align-optimal -a astar-seeds -g {GRAPH} -q {READS} -t {THREADS} --fixed_trie_depth 1 --seeds_len 10 -G 1 -v 1 -o {OUT_DIR}',
	'gwfa': './gwf-test {GRAPH} {READS}',
	'SGA': './apps/sga_example {GRAPH} {READS}',
	'V-ALIGN': './valign -g {GRAPH} -v {INDEX} -x {READS} -o {OUTPUT}',
	'vg': {
		'autoindex': 'vg autoindex --workflow giraffe -g {GRAPH} -p {OUTPUT}',
		'giraffe': 'vg giraffe -Z {INDEX} -m {MINIMIZERS} -d {DIST} -f {READS} -t {THREADS} -o gaf',
		'map': 'vg map -F {READS} -x {XG_INDEX} -g {GCSA_INDEX} --gaf'
	}, 
}

def main():
	
	# Open the tools_config.yml file and read tools' configuration
	with open('tools_config.yml', 'r') as file:
		config = yaml.safe_load(file)

	# Retrieve the alignments to be executed from INPUT_DATA/TEST
	DATA_FOLDER = os.path.join('./', 'input_data', 'TEST')
	ALIGNMENTS = [f for f in os.listdir(DATA_FOLDER)]

	# Set the results (output) folder
	RESULTS = os.path.join('./', 'results')
	# Create a folder for the current experiments (named with timestamp)
	date = datetime.now()
	date_str = date.strftime("%Y_%m_%d_%H_%M_%S")
	OUTPUT_DIR = os.path.join(RESULTS, date_str)
	try:
		os.makedirs(OUTPUT_DIR)
	except OSError as e:
		raise

	# Open the output file docker-compose.yml, and write the header
	file_tmp = open('docker-compose.yml', 'w')
	file_tmp.write(DOCKER_COMPOSE_HEADER)

	# Here we iteratively populate the docker-compose.yml
	# For each tool
	for tool in config:
		# initialize service and command for the specific tool
		service_tmp = SERVICE_TEMPLATE.format(tool_lower=tool.lower(), tool=tool)
		command_tmp = COMMANDS[tool]

		# create the results subfolder for the specific tool
		RESULTS_DIR = os.path.join(OUTPUT_DIR, tool)
		try:
			os.makedirs(RESULTS_DIR)
		except OSError as e:
			raise

		# write the service on docker-compose.yml
		file_tmp.write(service_tmp)

		# for each alignment experiment, add the respective command to docker-compose.yml
		for al in ALIGNMENTS:
			# create the results subfolder for the specific tool
			RESULTS_SUBDIR = os.path.join(RESULTS_DIR, al)
			try:
				os.makedirs(RESULTS_SUBDIR)
			except OSError as e:
				raise
			# retrieve the relative path of input data
			dir_tmp = os.path.join(DATA_FOLDER, al)
			graph = [f for f in os.listdir(os.path.join(dir_tmp, 'GRAPH')) if f.endswith('.gfa')][0]
			graph_path = os.path.join(dir_tmp,'GRAPH', graph)
			reads = [f for f in os.listdir(os.path.join(dir_tmp, 'READS')) if 
				(f.lower().endswith('.fa') or f.lower().endswith('.fq') or 
				f.lower().endswith('.fasta') or f.lower().endswith('fastq'))][0]
			reads_path = os.path.join(dir_tmp, 'READS', reads)
			# set the output files' names and relative paths
			output_name = graph.split('.gfa')[0] + '_alignments.gaf'
			timing_name = graph.split('.gfa')[0] + '_time.log'
			output_path = os.path.join(RESULTS_SUBDIR, output_name)
			timing_path = os.path.join(RESULTS_SUBDIR, timing_name)

			# add the command related to the alignment experiment
			# we need specific cases for each tool, it can't be more standardized
			if tool == 'GraphAligner':
				command = command_tmp.format(GRAPH=graph_path, 
												READS=reads_path,
												OUTPUT=output_path,
												THREADS=N_THREADS)
				command = COMMAND_TEMPLATE.format(COMMAND=command,
													LOG='> /dev/null',
													TIMING=timing_path)
				file_tmp.write(command)

			elif tool == 'astarix':
				command = command_tmp.format(GRAPH=graph_path, 
												READS=reads_path,
												OUT_DIR=RESULTS_SUBDIR,
												THREADS=1) # Currently, AStarix works only with 1 thread
				command = COMMAND_TEMPLATE.format(COMMAND=command,
													LOG='> ' + output_path.split('.gaf')[0] + '.log',
													TIMING=timing_path)
				file_tmp.write(command)

			elif tool == 'gwfa':
				command = command_tmp.format(GRAPH=graph_path,
				 								READS=reads_path)
				command = COMMAND_TEMPLATE.format(COMMAND=command,
				      								LOG='> ' + output_path.split('.gaf')[0] + '.log',
													TIMING=timing_path)
				file_tmp.write(command)
			
			elif tool == 'SGA':
				command = command_tmp.format(GRAPH=graph_path,
				 								READS=reads_path)
				command = COMMAND_TEMPLATE.format(COMMAND=command,
				      								LOG='> ' + output_path.split('.gaf')[0] + '.log',
													TIMING=timing_path)
				file_tmp.write(command)

			elif tool == 'V-ALIGN':
				txt_reads_path = '.'.join(reads_path.split('.')[:-1]) + '.txt'
				convert_cmd = f'        python3 fasta_to_txt.py {reads_path}\n'
				index_cmd = f'        utils/genfvs {graph_path} > /dev/null\n'
				index_path = graph_path + '.fvs'
				command = command_tmp.format(GRAPH=graph_path,
				 								INDEX=index_path,
												READS=txt_reads_path,
												OUTPUT=output_path.split('.gaf')[0] + '.log')
				command = COMMAND_TEMPLATE.format(COMMAND=command,
													LOG='> /dev/null',
													TIMING=timing_path)
				dot_graph_path = graph_path.split('.gfa')[0] + '.visual.dot'									
				rm_command = f'        rm {dot_graph_path} {txt_reads_path} {index_path}\n'
				file_tmp.write(convert_cmd + index_cmd + command + rm_command)

			elif tool == 'vg':
				out_name = output_path.split('_alignments.gaf')[0]
				index_command = command_tmp['autoindex'].format(GRAPH=graph_path,
					      									OUTPUT=out_name)
				timing_path_index = timing_path.split('_')
				timing_path_index.insert(-1, 'index')
				timing_path_index = '_'.join(timing_path_index)
				index_command = COMMAND_TEMPLATE.format(COMMAND=index_command,
				      										LOG='> /dev/null',
															TIMING=timing_path_index)
				command = command_tmp['giraffe'].format(INDEX=out_name+'.giraffe.gbz',
					    									MINIMIZERS=out_name+'.min',
															DIST=out_name+'.dist',
															READS=reads_path,
															THREADS=N_THREADS)
				command = COMMAND_TEMPLATE.format(COMMAND=command,
				      								LOG='> ' + output_path,
													TIMING=timing_path)
				file_tmp.write(index_command + command)
	
	# Print a success message
	print('\nSuccessfully created docker-compose.yml for the following experiments:')
	for al in ALIGNMENTS:
		print(f'\t{al}')
	print()

				
if __name__ == '__main__':
	main()