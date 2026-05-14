
import os
ph = (os.path.abspath('src/templates/olt_onu_status.template'))
print(os.system(f'cat {ph}'))
