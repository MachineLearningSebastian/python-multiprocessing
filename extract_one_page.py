import subprocess

subprocess.call(['mutool', 'draw', '-G1.1', '-c', 'g',
                    '-i', '-P', '-r120', '-o', 'extracted/' + '26.png', 
                    "pdf/Edgar_Allan_Poe.pdf", str(26)])                                                                       