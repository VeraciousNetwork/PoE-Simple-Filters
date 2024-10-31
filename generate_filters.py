#!/usr/bin/env python3

from pprint import pprint
import glob
import os
import re

for f_name in glob.glob('*.filter'):
	print('Processing %s' % f_name)
	includes = []
	with open(f_name, 'r') as f_handle:
		for line in f_handle.readlines():
			if re.match(r'^#[a-z_0-9]+$', line):
				inc = line.strip()[1:]
				if os.path.exists(os.path.join('filters', inc + '.inc')):
					includes.append(inc)
				else:
					print('WARNING: %s.inc not located within filters' % inc)
	
	if len(includes) == 0:
		print('WARNING: %s does not contain any include directives' % f_name)
	else:
		print('Generating %s with %d includes' % (f_name, len(includes)))
		with open(f_name, 'w') as f_write:
			f_write.write('# Included directives:\n')
			f_write.write('#\n#' + '\n#'.join(includes) + '\n')
			f_write.write('#\n# Everything below is dynamically generated, DO NOT EDIT MANUALLY\n\n')
			
			for inc in includes:
				inc_path = os.path.join('filters', inc + '.inc')
				f_write.write('# BEGIN include from %s\n' % inc_path)
				with open(inc_path, 'r') as inc_read:
					f_write.write(inc_read.read())
				f_write.write('\n# END include\n\n')

