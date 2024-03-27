# WhatsOpt command line memo 

_(updated: 12/07/2023, wop version : 2.5.0)_

## 1. Basics

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

### Get connection status and currently pulled analysis
``` bash
wop status
``` 

### List available analyses getting their id, name and creation date
```bash
wop list
```

## 2. Code generation from Analysis (pulling from WhatsOpt server)

### Generate code from an analysis with id #_42_ (which becomes the "reference analysis")
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

### Change reference analysis from which the code is updated to use analysis with id #_43_
```bash
wop update --analysis-id 43
```

## 3. Analysis creation from code (pushing to WhatsOpt server)

### Import an analysis used from an OpenMDAO problem used in _analysis.py_
```bash
wop push program.py
```

### Import an OpenMDAO component _MyComponentClass_ in _component.py_
```bash
wop push -c MyComponentClass component.py
```

### Copy and get ownership of analysis named _mda_ with id #_42_
```bash
wop pull 42
wop push mda.py  # -> create new analysis 43
wop update --analysis-id 43
```

## 4. Export/Import

### Export standalone XDSM page for an analysis in WhatsOpt
```bash
wop show 
```

### Export standalone XDSM page from any OpenMDAO problem 
```bash
wop show -f openmdao_problem.py
```

### Export analysis #_42_ to json format in mda.json
```bash
wop pull --json 42 > mda.json
```

### Import analysis #_42_ from json format
```bash
wop push --json mda.json
```

### Export project #_7_ to json format in mda.json
```bash
wop pull --json -p 7 > project.json
```

### Import project #_7_ from json format
```bash
wop push --json project.json
```

## 5. Packaging (wop 2.5.0+)

Following commands expect code being pulled using _package mode_ which is the default in wop >= 2.5.0
  * wop < 2.5.0 : wop pull --package 42
  * wop >= 2.5.0: wop pull 42

### Building the package of the current analysis

```bash
wop build
```

### Building and publishing the package of the current analysis on the WhatsOpt server (a.k.a WopStore)

```bash
wop publish
```

### Fetching discipline implementations of the packaged analysis #_42_ within the current analysis code 

```bash
wop fetch 42
```

### Merging disciplines of the analysis #_42_ within the current analysis

```bash
wop merge 42
```

### Pulling disciplines of the analysis #_42_ within the current analysis (equivalent to merge + fetch)

```bash
wop pull 42
```

## 6. Post-processing results

### Just printing tables of results

```bash
wop upload -n <analysis>_doe.sqlite
wop upload -n <analysis>_mdo.sqlite
```

### Plotting results on WhatsOpt server

```bash
wop upload <analysis>_doe.sqlite
wop upload <analysis>_mdo.sqlite
```

### Convert analysis sqlite file to csv file
```bash
wop convert analysis_doe.sqlite
```
### Creating fake analysis from external csv data (useful to plot the data with WhatsOpt)
```bash
wop push --outvar-count <nb of outputs> data.csv
```

