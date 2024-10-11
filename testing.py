FILEPATH = r'FunctionLink\textFiles\requirements-3nfr-80fr.txt'
requirements = open(FILEPATH, 'r')

content = []
non_func_req = set()
func_req = set()
for line in requirements:  # Corrected the variable name
    # Strip whitespace and check if the line contains a colon
    if ':' in line:
       
        line = line.lower()
        # Split the line at the first colon and take the part after it, then removes the '.'s
        words = line.split(':', 1)[1].strip().replace('.', '')
        content.append(words)
        if line[:3] == 'nfr':
            non_func_req.add(words)
        elif line[:2] == 'fr':
            func_req.add(words)
            
print('Func Req:')      
for x in func_req:
    print(x)
print('NON func Req:')      
for x in non_func_req:
    print(x)