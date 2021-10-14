# WhatsOpt command line memo 

_(updated: 14/10/2021, wop version : 1.19.1)_

### wop version
```bash
wop --version
```

### Log in/out to/from WhatOpt server
```bash
wop login <whatsopt server url>
```
```bash
wop logout
```

### Check WhatsOpt and wop versions once logged in
```
wop version
```

### List available analyses getting their id, name and creation date
```bash
wop list
```

### Generate code from an analysis with id _42_ (which becomes the "reference analysis")
```bash
wop pull 42
```

### Update code following a structure change in WhatOpt reference analysis
```bash
wop update
```

### Update code following variable change in WhatOpt reference analysis
```bash
wop update --run-ops
```

### Change reference analysis from which the code is updated to use analysis with id _43_
```bash
wop update --analysis-id 43
```

### Import an analysis used from an OpenMDAO problem used in _analysis.py_
```bash
wop push program.py
```

### Import an OpenMDAO component _MyComponentClass_ in _component.py_
```bash
wop push -c MyComponentClass component.py
```

### Copy and get ownership of analysis named _mda_ with id _42_
```bash
wop pull 42
wop push mda.py  # -> create new analysis 43
wop update --analysis-id 43
```

### Get connection status and currently pulled analysis
``` bash
wop status
``` 

### Export standalone XDSM page for an analysis in WhatsOpt
```bash
wop show 
```

### Export standalone XDSM page from any OpenMDAO problem 
```bash
wop show -f openmdao_problem.py
```

### Export analysis _42_ to json format in mda.json
```bash
wop pull --json 42 > mda.json
```

### Import analysis _42_ from json format
```bash
wop push --json mda.json
```

### Export project _7_ to json format in mda.json
```bash
wop pull --json -p 7 > project.json
```

### Import project _7_ from json format
```bash
wop push --json project.json
```

### Convert analysis sqlite file to csv file
```bash
wop convert analysis_doe.sqlite
```
