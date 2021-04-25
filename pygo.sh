#!/bin/bash
#pygo.sh -- Make all scripts in current dir and subdir executable


find $PWD -maxdepth 3 -type f -name "*.py" -print0 | xargs -0 grep -LH '#!/usr/bin/env python3'| xargs sed -i '1i #!/usr/bin/env python3'; 
find $PWD -maxdepth 3 -type f -name "*.py" -exec chmod +x {} \; 


