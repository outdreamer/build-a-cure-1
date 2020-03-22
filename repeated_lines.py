import os

repeated_lines = {}

cwd = os.getcwd()
cwd = cwd.replace('find_existing_solutions','')
path = ''.join([cwd, 'docs'])
print('path', path)

for dirname in os.listdir(path):
	print('dirname', dirname)
	full_dirname = ''.join([path, '/', dirname])
	print('full_dirname', full_dirname)
	if os.path.isdir(full_dirname):
		for filename in os.listdir(full_dirname):
			print('filename', filename)
			if '.md' in filename:
				full_filename = ''.join([full_dirname, '/', filename])
				with open(full_filename, 'r') as f:
					lines = f.readlines()
					print('lines length', full_filename, type(lines), len(lines))
					for line in lines:
						line = line.strip().replace('\n', '')
						if len(line) > 0 and '#' not in line:
							if line in repeated_lines:
								if filename not in repeated_lines[line]:
									repeated_lines[line].append(filename)
							else:
								repeated_lines[line] = [filename]
					f.close()
new_repeated_lines = {}
for line in repeated_lines:
	if len(repeated_lines[line]) > 1:
		new_repeated_lines[line] = repeated_lines[line]

print('\n\n\nlength', len(new_repeated_lines.keys()))

for line in new_repeated_lines:
	print(line, new_repeated_lines[line])


''' compile function names '''
import subprocess
cmd = ["""grep -r 'def ' . --include='*.py' >> code_function_names.txt"""]
subprocess.check_output(cmd,shell=True)
