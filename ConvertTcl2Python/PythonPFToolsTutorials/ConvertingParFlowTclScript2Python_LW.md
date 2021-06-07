ConvertingParFlowTclScript2Python_LW

convert SJBM tcl script to python

# Step 0: Prerequisites
ParFlow installed w/ CLM
pftools installed



# Step 1: Convert ParFlow Tcl Script to Python

Copy the Little Washita test run files to your new run directory. Note your $PF_SRC should be set to your parflow install `src/` folder
```
cp -r $PF_SRC/test/tcl/washita/ ~/RunTest/`
cd ~/RunTest/washita`
```

Convert the tcl document to python. This is made really easy by using the command line function `parflow.cli.tcl2py` 

```
python3 -m parflow.cli.tcl2py -i LW_Test.tcl
```

# Step 2: Review and correct your converted script

Though the `parflow.cli.tcl2py` successfully converts parflow key values and variable sets from tcl to python, other tcl code, specifically more complicated code within loops, is not translated for you. These sections of code are commented out by the `parflow.cli.tcl2py` function and will need to be corrected manually.
<br>

## Import parflow python modules

The tcl code to import the tcl ParFlow tools is commented out in the new converted python script `LW_Test.py`

```tcl
# Import the ParFlow TCL package
# lappend   auto_path $env(PARFLOW_DIR)/bin
# package   require parflow
```

We'll need to import our Python ParFlow Tools instead, add the following code to the top of your file
```python
from parflow import Run
```
<br>

## Corrected Section 1: Creating an Output Directory:

The original tcl script contains script to create and move into a new `Outputs/` folder. You'll need to convert this section to python. 

### Original Tcl code:

```tcl
#-----------------------------------------------------------------------------
# Make a directory for the simulation run, files will be copied to this
# directory for running.
#-----------------------------------------------------------------------------
file mkdir "Outputs"
cd "./Outputs"
pfset     FileVersion    4
```
<br>

### Converted Python code:

```tcl
#-----------------------------------------------------------------------------
# Make a directory for the simulation run, files will be copied to this
# directory for running.
#-----------------------------------------------------------------------------
# file mkdir "Outputs"
# cd "./Outputs"
LW_Test. = 'FileVersion 4'
```

The python parflow tool file system module contains functions to make directories and change directories. Add these to your pftools import as needed `from parflow.tools.fs import mkdir, chdir, get_absolute_path` you can also see what functions are available  [here](https://github.com/parflow/parflow/blob/master/pftools/python/parflow/tools/fs.py).

Additionally, you will no longer need the FileVersion Key, so you can just remove this line
<br>

### Updated Python code:

```python
#-----------------------------------------------------------------------------
# Make a directory for the simulation run, files will be copied to this
# directory for running.
#-----------------------------------------------------------------------------
mkdir "Outputs"
chdir "./Outputs"
```

<br>

## Corrected Section 2: Setting keys with other keys

When using the tcl pftools parflow keys are accessed using the `pfget` function. This isn't required when using the python pftools.

### Original Tcl Code:
```
pfset BCPressure.PatchNames                   [pfget Geom.domain.Patches]
```

### Corrected Python Code:
```
LW_Test.BCPressure.PatchNames = LW_Test.Geom.domain.Patches
```

## Corrected Section 3: Copying Files

The original `LW_Test.tcl` script included code to copy over input files from other directories into your run directory. We'll need to adjust the code here into the python syntax. The python parflow tool file system module contains a function to copy files, so we can update our file system module import at the top of the file to `from parflow.tools.fs import mkdir, chdir, get_absolute_path, cp`

### Original Tcl Code:
```tcl
# ParFlow Inputs
set path "../../parflow_input"
foreach file "LW.slopex LW.slopey IndicatorFile_Gleeson.50z press.init" {
    file copy -force [format "%s/%s.pfb" $path $file] .
}
```

### Corrected Python Code:
```python
# ParFlow Inputs
path = "../../parflow_input"
for file in ["LW.slopex", "LW.slopey", "IndicatorFile_Gleeson.50z", "press.init"]:
     cp(path + '/' + file + '.pfb' , '.')
```


## Corrected Section 4: Distributing Files

### Original Tcl Code:
```tcl
pfdist -nz 1 LW.slopex.pfb
pfdist -nz 1 LW.slopey.pfb

pfdist IndicatorFile_Gleeson.50z.pfb
pfdist press.init.pfb
```

### Corrected Python Code:
```python
dist("LW.slopex.pfb")
dist("LW.slopey.pfb")

dist("IndicatorFile_Gleeson.50z.pfb")
dist("press.init.pfb")
```

## Corrected Section 5: Distribute Forcing:
The original tcl script uses the pfdist function to distribute the NLDAS forcing files. 

```tcl
set path "../../NLDAS"
foreach file "NLDAS.DSWR.000001_to_000024 NLDAS.DLWR.000001_to_000024 NLDAS.APCP.000001_to_000024 NLDAS.Temp.000001_to_000024 NLDAS.UGRD.000001_to_000024 NLDAS.VGRD.000001_to_000024 NLDAS.Press.000001_to_000024 NLDAS.SPFH.000001_to_000024" {
    file copy -force [format "%s/%s.pfb" $path $file] .
    pfdist -nz 24 [format "%s.pfb" $file]
}
```

The new python pftools as a dist function, you'll need to adjust your code for this new syntax.

#### Python code after conversion 

```python
path "../../NLDAS"
for file in ['NLDAS.DSWR.000001_to_000024','NLDAS.DLWR.000001_to_000024','NLDAS.APCP.000001_to_000024','NLDAS.Temp.000001_to_000024','NLDAS.UGRD.000001_to_000024','NLDAS.VGRD.000001_to_000024','NLDAS.Press.000001_to_000024','NLDAS.SPFH.000001_to_000024']:
  cp(path + file + '.pfb', ".")
  LW_Test.dist(file, R=24)
```

The `R=24` within the dist fuction is informing the function that the forcing files are in 24 hour chunks.

## Correction Section 6:

LW_Test.Geom.domain.Perm.TensorValX = 1.0d0

LW_Test.Solver.CLM.MetForcing = 3D

need to add quotes
LW_Test.Solver.CLM.MetForcing = '3D'


Random error - startcount must be an integer
`LW_Test.TimingInfo.StartCount = 0.0`
`LW_Test.TimingInfo.StartCount = 0`


Apparently this key doesn't exist anymore?
`LW_Test.Solver.BinaryOutDir = False`


