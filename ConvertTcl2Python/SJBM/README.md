ConvertingParFlowTclScript2Python_SJBM

convert SJBM tcl script to python

## Prerequisites
ParFlow installed w/ CLM
pftools installed



## Step 0: Clean up Tcl Script (optional)

Review your ParFlow Tcl script. Clear out any unnecessary lines of code. This will help avoid some potential problems when converting your script

This is a good time to clear out any historical code that's no longer in use. When the file is converted, unrecognized code will be commented out 

Keeping code in your tcl script, prior to converting, that is commented out, may make it more difficult to evaluate which lines of code need to be corrected after converting.

## Step 1: Convert ParFlow Tcl Script to Python

A command line function `parflow.cli.tcl2py` is available to convert your tcl script to python

Example usage to convert SJBM tcl script:
`python3 -m parflow.cli.tcl2py -i 20210521_CV.WY2017.OG.BL.tcl`

## Step 2: Review your converted script

You'll need to update any tcl code not related to the tcl parflow tools

For example, within the SJBM tcl script is a for loop that distributes the meterological forcing data to the desired processor topography

### Original Tcl code:
```tcl
set forcDir "/glade/scratch/lmthatch/SJBM_Scaling/00_Input/01_NLDAS/1km/WY2017_OG/"
if { $NLDASdist == 1} {
    pfset ComputationalGrid.NZ              240
    set name NLDAS
    set var [list "APCP" "DLWR" "DSWR" "Press" "SPFH" "Temp" "UGRD" "VGRD"]
    puts "Distributing forcing files"
    for {set counter 0} {$counter <= $runlength} {incr counter 240} {
        set counter2 [expr $counter + 239]
        foreach v $var {
            set filename [format "%s/%s.%s.%06d_to_%06d.pfb" $forcDir $name $v $counter $counter2]
            puts $filename
            pfdist $filename
        }
    }
}
puts "setting up domain and run parameters"
puts " "

```


the `parflow.cli.tcl2py` function can convert some elements, but comments out more complex code, like loops or functions

### Pythong Code after conversion 
```python
forcDir = "/glade/scratch/lmthatch/SJBM_Scaling/00_Input/01_NLDAS/1km/WY2017_OG/"
# if { $NLDASdist == 1} {
#     pfset ComputationalGrid.NZ              240 
#     set name NLDAS
#     set var [list "APCP" "DLWR" "DSWR" "Press" "SPFH" "Temp" "UGRD" "VGRD"]
#     #set var [list "Temp"]
#     puts "Distributing forcing files"
#     for {set counter 2161} {$counter <=2400} {incr counter 240} {
#         set counter2 [expr $counter + 239]
#         foreach v $var {
#             set filename [format "%s/%s.%s.%06d_to_%06d.pfb" $forcDir $name $v $counter $counter2]
#             puts $filename
#             pfdist $filename
#         }
#     }
# }
# puts "setting up domain and run parameters"
# puts " "
```

the `parflow.cli.tcl2py` function was able to reformat the syntax for setting variable e.g. `set forcfDir` to `forcDir = `

You will need to manually convert the remaining code by hand

### Corrected Python code:
```python
forcDir "/glade/scratch/lmthatch/SJBM_Scaling/00_Input/01_NLDAS/1km/WY2017_OG/"
if NLDASdist == 1:
    20210521_CV.WY2017.OG.BL.ComputationalGrid.NZ              240
    name = "NLDAS"
    var = ["APCP", "DLWR", "DSWR", "Press", "SPFH", "Temp", "UGRD", "VGRD"]
    print("Distributing forcing files")
    for counter in range(0,runLength,240):
        counter2 = counter + 239
        for v in var:
            filename = "%s/%s.%s.%06d_to_%06d.pfb" $forcDir $name $v $counter $counter2]
            print(filename)
            pfdist $filename
        }
    }
}
puts "setting up domain and run parameters"
puts " "



```




# running ParFlow

