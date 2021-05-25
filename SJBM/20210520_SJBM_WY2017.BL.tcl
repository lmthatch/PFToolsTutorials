
#------------------------------------------------------------------
# *original version*
# 5-layers vertical
# discretization [jg 5/16/14]
# *Python PFTools Tutorial version
# LThatch 5/21/21
#-------------------------------------------------------------------

set tcl_precision 17

#---------------------------------------------------------
# Import ParFlow TCL package
#---------------------------------------------------------

lappend auto_path $env(PARFLOW_DIR)/bin
package require parflow
namespace import Parflow::*

pfset FileVersion 4

#---------------------------------------------------------
# SJBM User Settings
#---------------------------------------------------------

set oldrunname CV.WY2017to2019.1km.5lay.BL.SU2009_Y17
set runname CV.WY2017.OG.BL

set istep 1

set NLDASdist 0 ;# set to 1 if NLDAS forcing needs to be distributed, 0 if not
set year_restart 1  ;# set to 1 if starting over at a new year (with a new runname)
                    ;# set to 0 if restarting within a year (or same runname)

# Linux GPU Processor Topology

# Cheyenne Run Processor Topology
pfset Process.Topology.P	       18
pfset Process.Topology.Q	       14
pfset Process.Topology.R		1

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------
pfset ComputationalGrid.Lower.X           0.0
pfset ComputationalGrid.Lower.Y           0.0
pfset ComputationalGrid.Lower.Z           0.0

pfset ComputationalGrid.NX                270
pfset ComputationalGrid.NY                220
pfset ComputationalGrid.NZ                5

pfset ComputationalGrid.DX	         	1000.0
pfset ComputationalGrid.DY              1000.0
pfset ComputationalGrid.DZ              100.0

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------
pfset GeomInput.Names                 "domaininput ind_input"

pfset GeomInput.domaininput.GeomName  domain
pfset GeomInput.domaininput.InputType  Box

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------
pfset Geom.domain.Lower.X                        0.0
pfset Geom.domain.Lower.Y                        0.0
pfset Geom.domain.Lower.Z                        0.0

pfset Geom.domain.Upper.X                        270000.0
pfset Geom.domain.Upper.Y                        220000.0

pfset Geom.domain.Upper.Z                        500.0
pfset Geom.domain.Patches             "x-lower x-upper y-lower y-upper z-lower z-upper"

#----------------------------------------------------------------------------
# Start/Stop times
#----------------------------------------------------------------------------

set  nproc [expr [pfget Process.Topology.P]*[pfget Process.Topology.Q]*[pfget Process.Topology.R]]
set runlength 8760

set startcount [expr (int($istep-1))]
set starttime   [expr $istep-1]
set stoptime   $runlength ;#[expr ($runlength -$startcount)]

# Copy final pressure to PFB for restart
set last [expr $istep-1] ;# $final_actual_press_index
if {$year_restart ==1} then {
    set fname_ic [format "%s.out.press.08760.pfb"  $oldrunname]
} else {
    set fname_ic [format "%s.out.press.%05d.pfb" $runname $last]
}
exec cp $fname_ic pfinit.pfb
puts [format "Using %s for initial pressure" $fname_ic]


#-----------------------------------------------------------
# Distribute NLDAS Forcing files
#-----------------------------------------------------------

set forcDir "NLDAS/WY2017/"
if { $NLDASdist == 1} {
    pfset ComputationalGrid.NZ              240
    set name NLDAS
    set var [list "APCP" "DLWR" "DSWR" "Press" "SPFH" "Temp" "UGRD" "VGRD"]
    #set var [list "Temp"]
    puts "Distributing forcing files"
    for {set counter 2161} {$counter <=2400} {incr counter 240} {
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

#-----------------------------------------------------------------------------
# Subsurface Indicator Geometry Input
#-----------------------------------------------------------------------------

pfset ComputationalGrid.NZ             5
pfset GeomInput.ind_input.InputType    IndicatorField
pfset GeomInput.ind_input.GeomNames    "BR Bs Bls Bsi Bsil Bsicl Bl Bsl Bcl Bscl Bsic Bc Bo PR Ps Pls Psi Psil Psicl Pl Psl Pcl Pscl Psic Pc Po SR Ss Sls Ssi Ssil Ssicl Sl VR Vs Vls Vsi Vsil Vsicl Vl Vsl Vcl Vscl Vsic Vc Vo MV"

pfset Geom.ind_input.FileName          "text_ind.270i220j500k.v3.UniqCatAgg_5lay111514.pfb"
pfdist "text_ind.270i220j500k.v3.UniqCatAgg_5lay111514.pfb"

pfset GeomInput.BR.Value     0
pfset GeomInput.Bs.Value     1
pfset GeomInput.Bls.Value     2
pfset GeomInput.Bsi.Value     3
pfset GeomInput.Bsil.Value     4
pfset GeomInput.Bsicl.Value     5
pfset GeomInput.Bl.Value     6
pfset GeomInput.Bsl.Value     7
pfset GeomInput.Bcl.Value     8
pfset GeomInput.Bscl.Value     9
pfset GeomInput.Bsic.Value     10
pfset GeomInput.Bc.Value     11
pfset GeomInput.Bo.Value     12
pfset GeomInput.PR.Value     13
pfset GeomInput.Ps.Value     14
pfset GeomInput.Pls.Value     15
pfset GeomInput.Psi.Value     16
pfset GeomInput.Psil.Value     17
pfset GeomInput.Psicl.Value     18
pfset GeomInput.Pl.Value     19
pfset GeomInput.Psl.Value     20
pfset GeomInput.Pcl.Value     21
pfset GeomInput.Pscl.Value     22
pfset GeomInput.Psic.Value     23
pfset GeomInput.Pc.Value     24
pfset GeomInput.Po.Value     25
pfset GeomInput.SR.Value     26
pfset GeomInput.Ss.Value     27
pfset GeomInput.Sls.Value     28
pfset GeomInput.Ssi.Value     29
pfset GeomInput.Ssil.Value     30
pfset GeomInput.Ssicl.Value     31
pfset GeomInput.Sl.Value     32
pfset GeomInput.VR.Value     33
pfset GeomInput.Vs.Value     34
pfset GeomInput.Vls.Value     35
pfset GeomInput.Vsi.Value     36
pfset GeomInput.Vsil.Value     37
pfset GeomInput.Vsicl.Value     38
pfset GeomInput.Vl.Value     39
pfset GeomInput.Vsl.Value     40
pfset GeomInput.Vcl.Value     41
pfset GeomInput.Vscl.Value     42
pfset GeomInput.Vsic.Value     43
pfset GeomInput.Vc.Value     44
pfset GeomInput.Vo.Value     45
pfset GeomInput.MV.Value     46

#--------------------------------------------
# variable dz assignments
#------------------------------------------
pfset Solver.Nonlinear.VariableDz  True
pfset dzScale.GeomNames            domain
pfset dzScale.Type            nzList
pfset dzScale.nzListNumber       5

# 5 layers, starts at 0 for the bottom to 4 at the top
# layers 0,1,2,3,4 are 498m, 1.0 m, 0.6 m,0.3 m, 0.1 m
pfset Cell.0.dzScale.Value 4.98
pfset Cell.1.dzScale.Value 0.01
pfset Cell.2.dzScale.Value 0.006
pfset Cell.3.dzScale.Value 0.003
pfset Cell.4.dzScale.Value 0.001

#-----------------------------------------------------------------------------
# Perm - Horizontal Values
#-----------------------------------------------------------------------------

pfset Geom.Perm.Names                 "BR Bs Bls Bsi Bsil Bsicl Bl Bsl Bcl Bscl Bsic Bc Bo PR Ps Pls Psi Psil Psicl Pl Psl Pcl Pscl Psic Pc Po SR Ss Sls Ssi Ssil Ssicl Sl VR Vs Vls Vsi Vsil Vsicl Vl Vsl Vcl Vscl Vsic Vc Vo MV"

pfset Geom.BR.Perm.Type			Constant
pfset Geom.BR.Perm.Value			0.0042
pfset Geom.Bs.Perm.Type			Constant
pfset Geom.Bs.Perm.Value			2.9943496
pfset Geom.Bls.Perm.Type			Constant
pfset Geom.Bls.Perm.Value			1.0146179
pfset Geom.Bsi.Perm.Type			Constant
pfset Geom.Bsi.Perm.Value			0.3437973
pfset Geom.Bsil.Perm.Type			Constant
pfset Geom.Bsil.Perm.Value			0.1219839
pfset Geom.Bsicl.Perm.Type			Constant
pfset Geom.Bsicl.Perm.Value			0.0432815
pfset Geom.Bl.Perm.Type			Constant
pfset Geom.Bl.Perm.Value			0.0127733
pfset Geom.Bsl.Perm.Type			Constant
pfset Geom.Bsl.Perm.Value			0.0049694
pfset Geom.Bcl.Perm.Type			Constant
pfset Geom.Bcl.Perm.Value			0.0021198
pfset Geom.Bscl.Perm.Type			Constant
pfset Geom.Bscl.Perm.Value			0.0007697
pfset Geom.Bsic.Perm.Type			Constant
pfset Geom.Bsic.Perm.Value			0.0002549
pfset Geom.Bc.Perm.Type			Constant
pfset Geom.Bc.Perm.Value			0.0000992
pfset Geom.Bo.Perm.Type			Constant
pfset Geom.Bo.Perm.Value			7.5214661
pfset Geom.PR.Perm.Type			Constant
pfset Geom.PR.Perm.Value			0.0003456
pfset Geom.Ps.Perm.Type			Constant
pfset Geom.Ps.Perm.Value			2.9943496
pfset Geom.Pls.Perm.Type			Constant
pfset Geom.Pls.Perm.Value			1.0146179
pfset Geom.Psi.Perm.Type			Constant
pfset Geom.Psi.Perm.Value			0.3437973
pfset Geom.Psil.Perm.Type			Constant
pfset Geom.Psil.Perm.Value			0.1219839
pfset Geom.Psicl.Perm.Type			Constant
pfset Geom.Psicl.Perm.Value			0.0432815
pfset Geom.Pl.Perm.Type			Constant
pfset Geom.Pl.Perm.Value			0.0127733
pfset Geom.Psl.Perm.Type			Constant
pfset Geom.Psl.Perm.Value			0.0049694
pfset Geom.Pcl.Perm.Type			Constant
pfset Geom.Pcl.Perm.Value			0.0021198
pfset Geom.Pscl.Perm.Type			Constant
pfset Geom.Pscl.Perm.Value			0.0007697
pfset Geom.Psic.Perm.Type			Constant
pfset Geom.Psic.Perm.Value			0.0002549
pfset Geom.Pc.Perm.Type			Constant
pfset Geom.Pc.Perm.Value			0.0000992
pfset Geom.Po.Perm.Type			Constant
pfset Geom.Po.Perm.Value			7.5214661
pfset Geom.SR.Perm.Type			Constant
pfset Geom.SR.Perm.Value			0.0000992
pfset Geom.Ss.Perm.Type			Constant
pfset Geom.Ss.Perm.Value			2.9943496
pfset Geom.Sls.Perm.Type			Constant
pfset Geom.Sls.Perm.Value			1.0146179
pfset Geom.Ssi.Perm.Type			Constant
pfset Geom.Ssi.Perm.Value			0.3437973
pfset Geom.Ssil.Perm.Type			Constant
pfset Geom.Ssil.Perm.Value			0.1219839
pfset Geom.Ssicl.Perm.Type			Constant
pfset Geom.Ssicl.Perm.Value			0.0432815
pfset Geom.Sl.Perm.Type			Constant
pfset Geom.Sl.Perm.Value			0.0127733
pfset Geom.VR.Perm.Type			Constant
pfset Geom.VR.Perm.Value			0.0000992
pfset Geom.Vs.Perm.Type			Constant
pfset Geom.Vs.Perm.Value			2.9943496
pfset Geom.Vls.Perm.Type			Constant
pfset Geom.Vls.Perm.Value			1.0146179
pfset Geom.Vsi.Perm.Type			Constant
pfset Geom.Vsi.Perm.Value			0.3437973
pfset Geom.Vsil.Perm.Type			Constant
pfset Geom.Vsil.Perm.Value			0.1219839
pfset Geom.Vsicl.Perm.Type			Constant
pfset Geom.Vsicl.Perm.Value			0.0432815
pfset Geom.Vl.Perm.Type			Constant
pfset Geom.Vl.Perm.Value			0.0127733
pfset Geom.Vsl.Perm.Type			Constant
pfset Geom.Vsl.Perm.Value			0.0049694
pfset Geom.Vcl.Perm.Type			Constant
pfset Geom.Vcl.Perm.Value			0.0021198
pfset Geom.Vscl.Perm.Type			Constant
pfset Geom.Vscl.Perm.Value			0.0007697
pfset Geom.Vsic.Perm.Type			Constant
pfset Geom.Vsic.Perm.Value			0.0002549
pfset Geom.Vc.Perm.Type			Constant
pfset Geom.Vc.Perm.Value			0.0000992
pfset Geom.Vo.Perm.Type			Constant
pfset Geom.Vo.Perm.Value			7.5214661
pfset Geom.MV.Perm.Type                 Constant
pfset Geom.MV.Perm.Value                        0.041667
#-----------------------------------------------------------------------------
# Perm - Tensors
#-----------------------------------------------------------------------------

pfset Perm.TensorType               TensorByGeom

pfset Geom.Perm.TensorByGeom.Names  "BR Bs Bls Bsi Bsil Bsicl Bl Bsl Bcl Bscl Bsic Bc Bo PR Ps Pls Psi Psil Psicl Pl Psl Pcl Pscl Psic Pc Po SR Ss Sls Ssi Ssil Ssicl Sl VR Vs Vls Vsi Vsil Vsicl Vl Vsl Vcl Vscl Vsic Vc Vo MV"

pfset Geom.BR.Perm.TensorValX  1.00
pfset Geom.BR.Perm.TensorValY  1.00
#pfset Geom.BR.Perm.TensorValZ  1.00
pfset Geom.BR.Perm.TensorValZ  0.95833
pfset Geom.Bs.Perm.TensorValX  1.00
pfset Geom.Bs.Perm.TensorValY  1.00
#pfset Geom.Bs.Perm.TensorValZ  1.00
pfset Geom.Bs.Perm.TensorValZ  0.02344
pfset Geom.Bls.Perm.TensorValX  1.00
pfset Geom.Bls.Perm.TensorValY  1.00
#pfset Geom.Bls.Perm.TensorValZ  1.00
pfset Geom.Bls.Perm.TensorValZ  0.03802
pfset Geom.Bsi.Perm.TensorValX  1.00
pfset Geom.Bsi.Perm.TensorValY  1.00
#pfset Geom.Bsi.Perm.TensorValZ  1.00
pfset Geom.Bsi.Perm.TensorValZ  0.06026
pfset Geom.Bsil.Perm.TensorValX  1.00
pfset Geom.Bsil.Perm.TensorValY  1.00
#pfset Geom.Bsil.Perm.TensorValZ  1.00
pfset Geom.Bsil.Perm.TensorValZ 0.08318
pfset Geom.Bsicl.Perm.TensorValX  1.00
pfset Geom.Bsicl.Perm.TensorValY  1.00
#pfset Geom.Bsicl.Perm.TensorValZ  1.00
pfset Geom.Bsicl.Perm.TensorValZ 0.10965
pfset Geom.Bl.Perm.TensorValX  1.00
pfset Geom.Bl.Perm.TensorValY  1.00
#pfset Geom.Bl.Perm.TensorValZ  1.00
pfset Geom.Bl.Perm.TensorValZ 0.12882
pfset Geom.Bsl.Perm.TensorValX  1.00
pfset Geom.Bsl.Perm.TensorValY  1.00
#pfset Geom.Bsl.Perm.TensorValZ  1.00
pfset Geom.Bsl.Perm.TensorValZ 0.13183
pfset Geom.Bcl.Perm.TensorValX  1.00
pfset Geom.Bcl.Perm.TensorValY  1.00
#pfset Geom.Bcl.Perm.TensorValZ  1.00
pfset Geom.Bcl.Perm.TensorValZ 0.11749
pfset Geom.Bscl.Perm.TensorValX  1.00
pfset Geom.Bscl.Perm.TensorValY  1.00
#pfset Geom.Bscl.Perm.TensorValZ  1.00
pfset Geom.Bscl.Perm.TensorValZ 0.08913
pfset Geom.Bsic.Perm.TensorValX  1.00
pfset Geom.Bsic.Perm.TensorValY  1.00
#pfset Geom.Bsic.Perm.TensorValZ  1.00
pfset Geom.Bsic.Perm.TensorValZ 0.05248
pfset Geom.Bc.Perm.TensorValX  1.00
pfset Geom.Bc.Perm.TensorValY  1.00
#pfset Geom.Bc.Perm.TensorValZ  1.00
pfset Geom.Bc.Perm.TensorValZ 0.02455
pfset Geom.Bo.Perm.TensorValX  1.00
pfset Geom.Bo.Perm.TensorValY  1.00
#pfset Geom.Bo.Perm.TensorValZ  1.00
pfset Geom.Bo.Perm.TensorValZ 0.01479
pfset Geom.PR.Perm.TensorValX  1.00
pfset Geom.PR.Perm.TensorValY  1.00
#pfset Geom.PR.Perm.TensorValZ  1.00
pfset Geom.PR.Perm.TensorValZ  0.95833
pfset Geom.Ps.Perm.TensorValX  1.00
pfset Geom.Ps.Perm.TensorValY  1.00
#pfset Geom.Ps.Perm.TensorValZ  1.00
pfset Geom.Ps.Perm.TensorValZ 0.02344
pfset Geom.Pls.Perm.TensorValX  1.00
pfset Geom.Pls.Perm.TensorValY  1.00
#pfset Geom.Pls.Perm.TensorValZ  1.00
pfset Geom.Pls.Perm.TensorValZ 0.03802
pfset Geom.Psi.Perm.TensorValX  1.00
pfset Geom.Psi.Perm.TensorValY  1.00
#pfset Geom.Psi.Perm.TensorValZ  1.00
pfset Geom.Psi.Perm.TensorValZ 0.06026
pfset Geom.Psil.Perm.TensorValX  1.00
pfset Geom.Psil.Perm.TensorValY  1.00
#pfset Geom.Psil.Perm.TensorValZ  1.00
pfset Geom.Psil.Perm.TensorValZ 0.08318
pfset Geom.Psicl.Perm.TensorValX  1.00
pfset Geom.Psicl.Perm.TensorValY  1.00
#pfset Geom.Psicl.Perm.TensorValZ  1.00
pfset Geom.Psicl.Perm.TensorValZ 0.10965
pfset Geom.Pl.Perm.TensorValX  1.00
pfset Geom.Pl.Perm.TensorValY  1.00
#pfset Geom.Pl.Perm.TensorValZ  1.00
pfset Geom.Pl.Perm.TensorValZ 0.12882
pfset Geom.Psl.Perm.TensorValX  1.00
pfset Geom.Psl.Perm.TensorValY  1.00
#pfset Geom.Psl.Perm.TensorValZ  1.00
pfset Geom.Psl.Perm.TensorValZ 0.13183
pfset Geom.Pcl.Perm.TensorValX  1.00
pfset Geom.Pcl.Perm.TensorValY  1.00
#pfset Geom.Pcl.Perm.TensorValZ  1.00
pfset Geom.Pcl.Perm.TensorValZ 0.11749
pfset Geom.Pscl.Perm.TensorValX  1.00
pfset Geom.Pscl.Perm.TensorValY  1.00
#pfset Geom.Pscl.Perm.TensorValZ  1.00
pfset Geom.Pscl.Perm.TensorValZ 0.08913
pfset Geom.Psic.Perm.TensorValX  1.00
pfset Geom.Psic.Perm.TensorValY  1.00
#pfset Geom.Psic.Perm.TensorValZ  1.00
pfset Geom.Psic.Perm.TensorValZ 0.05248
pfset Geom.Pc.Perm.TensorValX  1.00
pfset Geom.Pc.Perm.TensorValY  1.00
#pfset Geom.Pc.Perm.TensorValZ  1.00
pfset Geom.Pc.Perm.TensorValZ 0.02455
pfset Geom.Po.Perm.TensorValX  1.00
pfset Geom.Po.Perm.TensorValY  1.00
#pfset Geom.Po.Perm.TensorValZ  1.00
pfset Geom.Po.Perm.TensorValZ 0.01479
pfset Geom.SR.Perm.TensorValX  1.00
pfset Geom.SR.Perm.TensorValY  1.00
#pfset Geom.SR.Perm.TensorValZ  1.00
pfset Geom.SR.Perm.TensorValZ  0.02455
pfset Geom.Ss.Perm.TensorValX  1.00
pfset Geom.Ss.Perm.TensorValY  1.00
#pfset Geom.Ss.Perm.TensorValZ  1.00
pfset Geom.Ss.Perm.TensorValZ  0.02344
pfset Geom.Sls.Perm.TensorValX  1.00
pfset Geom.Sls.Perm.TensorValY  1.00
#pfset Geom.Sls.Perm.TensorValZ  1.00
pfset Geom.Sls.Perm.TensorValZ  0.03802
pfset Geom.Ssi.Perm.TensorValX  1.00
pfset Geom.Ssi.Perm.TensorValY  1.00
#pfset Geom.Ssi.Perm.TensorValZ  1.00
pfset Geom.Ssi.Perm.TensorValZ  0.06026
pfset Geom.Ssil.Perm.TensorValX  1.00
pfset Geom.Ssil.Perm.TensorValY  1.00
#pfset Geom.Ssil.Perm.TensorValZ  1.00
pfset Geom.Ssil.Perm.TensorValZ  0.08318
pfset Geom.Ssicl.Perm.TensorValX  1.00
pfset Geom.Ssicl.Perm.TensorValY  1.00
#pfset Geom.Ssicl.Perm.TensorValZ  1.00
pfset Geom.Ssicl.Perm.TensorValZ  0.10965
pfset Geom.Sl.Perm.TensorValX  1.00
pfset Geom.Sl.Perm.TensorValY  1.00
#pfset Geom.Sl.Perm.TensorValZ  1.00
pfset Geom.Sl.Perm.TensorValZ  0.12882
pfset Geom.VR.Perm.TensorValX  1.00
pfset Geom.VR.Perm.TensorValY  1.00
#pfset Geom.VR.Perm.TensorValZ  1.00
pfset Geom.VR.Perm.TensorValZ  0.02455
pfset Geom.Vs.Perm.TensorValX  1.00
pfset Geom.Vs.Perm.TensorValY  1.00
#pfset Geom.Vs.Perm.TensorValZ  1.00
pfset Geom.Vs.Perm.TensorValZ  0.02344
pfset Geom.Vls.Perm.TensorValX  1.00
pfset Geom.Vls.Perm.TensorValY  1.00
#pfset Geom.Vls.Perm.TensorValZ  1.00
pfset Geom.Vls.Perm.TensorValZ  0.03802
pfset Geom.Vsi.Perm.TensorValX  1.00
pfset Geom.Vsi.Perm.TensorValY  1.00
#pfset Geom.Vsi.Perm.TensorValZ  1.00
pfset Geom.Vsi.Perm.TensorValZ  0.06026
pfset Geom.Vsil.Perm.TensorValX  1.00
pfset Geom.Vsil.Perm.TensorValY  1.00
#pfset Geom.Vsil.Perm.TensorValZ  1.00
pfset Geom.Vsil.Perm.TensorValZ  0.08318
pfset Geom.Vsicl.Perm.TensorValX  1.00
pfset Geom.Vsicl.Perm.TensorValY  1.00
#pfset Geom.Vsicl.Perm.TensorValZ  1.00
pfset Geom.Vsicl.Perm.TensorValZ  0.10965
pfset Geom.Vl.Perm.TensorValX  1.00
pfset Geom.Vl.Perm.TensorValY  1.00
#pfset Geom.Vl.Perm.TensorValZ  1.00
pfset Geom.Vl.Perm.TensorValZ  0.12882
pfset Geom.Vsl.Perm.TensorValX  1.00
pfset Geom.Vsl.Perm.TensorValY  1.00
#pfset Geom.Vsl.Perm.TensorValZ  1.00
pfset Geom.Vsl.Perm.TensorValZ  0.13183
pfset Geom.Vcl.Perm.TensorValX  1.00
pfset Geom.Vcl.Perm.TensorValY  1.00
#pfset Geom.Vcl.Perm.TensorValZ  1.00
pfset Geom.Vcl.Perm.TensorValZ  0.11749
pfset Geom.Vscl.Perm.TensorValX  1.00
pfset Geom.Vscl.Perm.TensorValY  1.00
#pfset Geom.Vscl.Perm.TensorValZ  1.00
pfset Geom.Vscl.Perm.TensorValZ  0.08913
pfset Geom.Vsic.Perm.TensorValX  1.00
pfset Geom.Vsic.Perm.TensorValY  1.00
#pfset Geom.Vsic.Perm.TensorValZ  1.00
pfset Geom.Vsic.Perm.TensorValZ  0.05248
pfset Geom.Vc.Perm.TensorValX  1.00
pfset Geom.Vc.Perm.TensorValY  1.00
#pfset Geom.Vc.Perm.TensorValZ  1.00
pfset Geom.Vc.Perm.TensorValZ  0.02455
pfset Geom.Vo.Perm.TensorValX  1.00
pfset Geom.Vo.Perm.TensorValY  1.00
#pfset Geom.Vo.Perm.TensorValZ  1.00
pfset Geom.Vo.Perm.TensorValZ  0.01479
pfset Geom.MV.Perm.TensorValX  1.00
pfset Geom.MV.Perm.TensorValY  1.00
pfset Geom.MV.Perm.TensorValZ  0.1  ;# a vertical anisotropy of 1/10 used here as a first approximation - not based on any specific reference value

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

pfset SpecificStorage.Type                Constant
pfset SpecificStorage.GeomNames           "domain"
pfset Geom.domain.SpecificStorage.Value   1.0e-5

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

pfset Phase.Names "water"
pfset Phase.water.Density.Type	        Constant
pfset Phase.water.Density.Value	        1.0
pfset Phase.water.Viscosity.Type	      Constant
pfset Phase.water.Viscosity.Value	      1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

pfset Contaminants.Names			""

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

pfset Geom.Retardation.GeomNames           ""

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

pfset Gravity				1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

#
pfset TimingInfo.BaseUnit        1.0
#pfset TimingInfo.StartCount     1
pfset TimingInfo.StartCount      $startcount
pfset TimingInfo.StartTime       $starttime
pfset TimingInfo.DumpInterval    1.0
pfset TimingInfo.StopTime        $stoptime

pfset TimeStep.Type              Constant
pfset TimeStep.Value              1.0
#pfset TimeStep.Type              Growth
#pfset TimeStep.InitialStep        500
#pfset TimeStep.GrowthFactor       1.5
#pfset TimeStep.MaxStep            8800
#pfset TimeStep.MinStep            0.001
#pfset TimeStep.Value             0.1
#pfset TimeStep.Value              500
#pfset TimeStep.Value             0.5

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------
pfset Geom.Porosity.GeomNames		"BR Bs Bls Bsi Bsil Bsicl Bl Bsl Bcl Bscl Bsic Bc Bo PR Ps Pls Psi Psil Psicl Pl Psl Pcl Pscl Psic Pc Po SR Ss Sls Ssi Ssil Ssicl Sl VR Vs Vls Vsi Vsil Vsicl Vl Vsl Vcl Vscl Vsic Vc Vo MV"

pfset Geom.BR.Porosity.Type			Constant
pfset Geom.BR.Porosity.Value			0.045
pfset Geom.Bs.Porosity.Type			Constant
pfset Geom.Bs.Porosity.Value			0.290
pfset Geom.Bls.Porosity.Type			Constant
pfset Geom.Bls.Porosity.Value			0.320
pfset Geom.Bsi.Porosity.Type			Constant
pfset Geom.Bsi.Porosity.Value			0.360
pfset Geom.Bsil.Porosity.Type			Constant
pfset Geom.Bsil.Porosity.Value			0.390
pfset Geom.Bsicl.Porosity.Type			Constant
pfset Geom.Bsicl.Porosity.Value			0.420
pfset Geom.Bl.Porosity.Type			Constant
pfset Geom.Bl.Porosity.Value			0.460
pfset Geom.Bsl.Porosity.Type			Constant
pfset Geom.Bsl.Porosity.Value			0.490
pfset Geom.Bcl.Porosity.Type			Constant
pfset Geom.Bcl.Porosity.Value			0.510
pfset Geom.Bscl.Porosity.Type			Constant
pfset Geom.Bscl.Porosity.Value			0.540
pfset Geom.Bsic.Porosity.Type			Constant
pfset Geom.Bsic.Porosity.Value			0.580
pfset Geom.Bc.Porosity.Type			Constant
pfset Geom.Bc.Porosity.Value			0.610
pfset Geom.Bo.Porosity.Type			Constant
pfset Geom.Bo.Porosity.Value			0.260
pfset Geom.PR.Porosity.Type			Constant
pfset Geom.PR.Porosity.Value			0.045
pfset Geom.Ps.Porosity.Type			Constant
pfset Geom.Ps.Porosity.Value			0.290
pfset Geom.Pls.Porosity.Type			Constant
pfset Geom.Pls.Porosity.Value			0.320
pfset Geom.Psi.Porosity.Type			Constant
pfset Geom.Psi.Porosity.Value			0.360
pfset Geom.Psil.Porosity.Type			Constant
pfset Geom.Psil.Porosity.Value			0.390
pfset Geom.Psicl.Porosity.Type			Constant
pfset Geom.Psicl.Porosity.Value			0.420
pfset Geom.Pl.Porosity.Type			Constant
pfset Geom.Pl.Porosity.Value			0.460
pfset Geom.Psl.Porosity.Type			Constant
pfset Geom.Psl.Porosity.Value			0.490
pfset Geom.Pcl.Porosity.Type			Constant
pfset Geom.Pcl.Porosity.Value			0.510
pfset Geom.Pscl.Porosity.Type			Constant
pfset Geom.Pscl.Porosity.Value			0.540
pfset Geom.Psic.Porosity.Type			Constant
pfset Geom.Psic.Porosity.Value			0.580
pfset Geom.Pc.Porosity.Type			Constant
pfset Geom.Pc.Porosity.Value			0.610
pfset Geom.Po.Porosity.Type			Constant
pfset Geom.Po.Porosity.Value			0.260
pfset Geom.SR.Porosity.Type			Constant
pfset Geom.SR.Porosity.Value			0.110
pfset Geom.Ss.Porosity.Type			Constant
pfset Geom.Ss.Porosity.Value			0.290
pfset Geom.Sls.Porosity.Type			Constant
pfset Geom.Sls.Porosity.Value			0.320
pfset Geom.Ssi.Porosity.Type			Constant
pfset Geom.Ssi.Porosity.Value			0.360
pfset Geom.Ssil.Porosity.Type			Constant
pfset Geom.Ssil.Porosity.Value			0.390
pfset Geom.Ssicl.Porosity.Type			Constant
pfset Geom.Ssicl.Porosity.Value			0.420
pfset Geom.Sl.Porosity.Type			Constant
pfset Geom.Sl.Porosity.Value			0.460
pfset Geom.VR.Porosity.Type			Constant
pfset Geom.VR.Porosity.Value			0.110
pfset Geom.Vs.Porosity.Type			Constant
pfset Geom.Vs.Porosity.Value			0.290
pfset Geom.Vls.Porosity.Type			Constant
pfset Geom.Vls.Porosity.Value			0.320
pfset Geom.Vsi.Porosity.Type			Constant
pfset Geom.Vsi.Porosity.Value			0.360
pfset Geom.Vsil.Porosity.Type			Constant
pfset Geom.Vsil.Porosity.Value			0.390
pfset Geom.Vsicl.Porosity.Type			Constant
pfset Geom.Vsicl.Porosity.Value			0.420
pfset Geom.Vl.Porosity.Type			Constant
pfset Geom.Vl.Porosity.Value			0.460
pfset Geom.Vsl.Porosity.Type			Constant
pfset Geom.Vsl.Porosity.Value			0.490
pfset Geom.Vcl.Porosity.Type			Constant
pfset Geom.Vcl.Porosity.Value			0.510
pfset Geom.Vscl.Porosity.Type			Constant
pfset Geom.Vscl.Porosity.Value			0.540
pfset Geom.Vsic.Porosity.Type			Constant
pfset Geom.Vsic.Porosity.Value			0.580
pfset Geom.Vc.Porosity.Type			Constant
pfset Geom.Vc.Porosity.Value			0.610
pfset Geom.Vo.Porosity.Type			Constant
pfset Geom.Vo.Porosity.Value			0.260
pfset Geom.MV.Porosity.Type                     Constant
pfset Geom.MV.Porosity.Value                    0.150

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

pfset Domain.GeomName domain

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

pfset Phase.RelPerm.Type               VanGenuchten
pfset Phase.RelPerm.GeomNames          "BR Bs Bls Bsi Bsil Bsicl Bl Bsl Bcl Bscl Bsic Bc Bo PR Ps Pls Psi Psil Psicl Pl Psl Pcl Pscl Psic Pc Po SR Ss Sls Ssi Ssil Ssicl Sl VR Vs Vls Vsi Vsil Vsicl Vl Vsl Vcl Vscl Vsic Vc Vo MV"

pfset Geom.BR.RelPerm.Alpha			3.8
pfset Geom.BR.RelPerm.N			2.000
pfset Geom.Bs.RelPerm.Alpha			3.52
pfset Geom.Bs.RelPerm.N			3.180
pfset Geom.Bls.RelPerm.Alpha			3.48
pfset Geom.Bls.RelPerm.N			2.000
pfset Geom.Bsi.RelPerm.Alpha			0.66
pfset Geom.Bsi.RelPerm.N			2.000
pfset Geom.Bsil.RelPerm.Alpha			0.51
pfset Geom.Bsil.RelPerm.N			2.000
pfset Geom.Bsicl.RelPerm.Alpha			0.84
pfset Geom.Bsicl.RelPerm.N			2.000
pfset Geom.Bl.RelPerm.Alpha			1.11
pfset Geom.Bl.RelPerm.N			2.000
pfset Geom.Bsl.RelPerm.Alpha			2.67
pfset Geom.Bsl.RelPerm.N			2.000
pfset Geom.Bcl.RelPerm.Alpha			1.58
pfset Geom.Bcl.RelPerm.N			2.000
pfset Geom.Bscl.RelPerm.Alpha			2.11
pfset Geom.Bscl.RelPerm.N			2.000
pfset Geom.Bsic.RelPerm.Alpha			1.62
pfset Geom.Bsic.RelPerm.N			2.000
pfset Geom.Bc.RelPerm.Alpha			1.5
pfset Geom.Bc.RelPerm.N			2.000
pfset Geom.Bo.RelPerm.Alpha			3.52
pfset Geom.Bo.RelPerm.N			3.180
pfset Geom.PR.RelPerm.Alpha			3.8
pfset Geom.PR.RelPerm.N			2.000
pfset Geom.Ps.RelPerm.Alpha			3.52
pfset Geom.Ps.RelPerm.N			3.180
pfset Geom.Pls.RelPerm.Alpha			3.48
pfset Geom.Pls.RelPerm.N			2.000
pfset Geom.Psi.RelPerm.Alpha			0.66
pfset Geom.Psi.RelPerm.N			2.000
pfset Geom.Psil.RelPerm.Alpha			0.51
pfset Geom.Psil.RelPerm.N			2.000
pfset Geom.Psicl.RelPerm.Alpha			0.84
pfset Geom.Psicl.RelPerm.N			2.000
pfset Geom.Pl.RelPerm.Alpha			1.11
pfset Geom.Pl.RelPerm.N			2.000
pfset Geom.Psl.RelPerm.Alpha			2.67
pfset Geom.Psl.RelPerm.N			2.000
pfset Geom.Pcl.RelPerm.Alpha			1.58
pfset Geom.Pcl.RelPerm.N			2.000
pfset Geom.Pscl.RelPerm.Alpha			2.11
pfset Geom.Pscl.RelPerm.N			2.000
pfset Geom.Psic.RelPerm.Alpha			1.62
pfset Geom.Psic.RelPerm.N			2.000
pfset Geom.Pc.RelPerm.Alpha			1.5
pfset Geom.Pc.RelPerm.N			2.000
pfset Geom.Po.RelPerm.Alpha			3.52
pfset Geom.Po.RelPerm.N			3.180
pfset Geom.SR.RelPerm.Alpha			0.51
pfset Geom.SR.RelPerm.N			2.000
pfset Geom.Ss.RelPerm.Alpha			3.52
pfset Geom.Ss.RelPerm.N			3.180
pfset Geom.Sls.RelPerm.Alpha			3.48
pfset Geom.Sls.RelPerm.N			2.000
pfset Geom.Ssi.RelPerm.Alpha			0.66
pfset Geom.Ssi.RelPerm.N			2.000
pfset Geom.Ssil.RelPerm.Alpha			0.51
pfset Geom.Ssil.RelPerm.N			2.000
pfset Geom.Ssicl.RelPerm.Alpha			0.84
pfset Geom.Ssicl.RelPerm.N			2.000
pfset Geom.Sl.RelPerm.Alpha			1.11
pfset Geom.Sl.RelPerm.N			2.000
pfset Geom.VR.RelPerm.Alpha			0.51
pfset Geom.VR.RelPerm.N			2.000
pfset Geom.Vs.RelPerm.Alpha			3.52
pfset Geom.Vs.RelPerm.N			3.180
pfset Geom.Vls.RelPerm.Alpha			3.48
pfset Geom.Vls.RelPerm.N			2.000
pfset Geom.Vsi.RelPerm.Alpha			0.66
pfset Geom.Vsi.RelPerm.N			2.000
pfset Geom.Vsil.RelPerm.Alpha			0.51
pfset Geom.Vsil.RelPerm.N			2.000
pfset Geom.Vsicl.RelPerm.Alpha			0.84
pfset Geom.Vsicl.RelPerm.N			2.000
pfset Geom.Vl.RelPerm.Alpha			1.11
pfset Geom.Vl.RelPerm.N			2.000
pfset Geom.Vsl.RelPerm.Alpha			2.67
pfset Geom.Vsl.RelPerm.N			2.000
pfset Geom.Vcl.RelPerm.Alpha			1.58
pfset Geom.Vcl.RelPerm.N			2.000
pfset Geom.Vscl.RelPerm.Alpha			2.11
pfset Geom.Vscl.RelPerm.N			2.000
pfset Geom.Vsic.RelPerm.Alpha			1.62
pfset Geom.Vsic.RelPerm.N			2.000
pfset Geom.Vc.RelPerm.Alpha			1.5
pfset Geom.Vc.RelPerm.N			2.000
pfset Geom.Vo.RelPerm.Alpha			3.52
pfset Geom.Vo.RelPerm.N			3.180
pfset Geom.MV.RelPerm.Alpha                   3.52
pfset Geom.MV.RelPerm.N                       3.180

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

pfset Phase.Saturation.Type              VanGenuchten
pfset Phase.Saturation.GeomNames         "BR Bs Bls Bsi Bsil Bsicl Bl Bsl Bcl Bscl Bsic Bc Bo PR Ps Pls Psi Psil Psicl Pl Psl Pcl Pscl Psic Pc Po SR Ss Sls Ssi Ssil Ssicl Sl VR Vs Vls Vsi Vsil Vsicl Vl Vsl Vcl Vscl Vsic Vc Vo MV"

pfset Geom.BR.Saturation.Alpha			3.8
pfset Geom.BR.Saturation.N			2.000
pfset Geom.BR.Saturation.SRes			0.20  ;#0.889 <-- changed this value for run 03B on 2016.06.12
pfset Geom.BR.Saturation.SSat			1.000
pfset Geom.Bs.Saturation.Alpha			3.52
pfset Geom.Bs.Saturation.N			3.180
pfset Geom.Bs.Saturation.SRes			0.140
pfset Geom.Bs.Saturation.SSat			1.000
pfset Geom.Bls.Saturation.Alpha			3.48
pfset Geom.Bls.Saturation.N			2.000
pfset Geom.Bls.Saturation.SRes			0.130
pfset Geom.Bls.Saturation.SSat			1.000
pfset Geom.Bsi.Saturation.Alpha			0.66
pfset Geom.Bsi.Saturation.N			2.000
pfset Geom.Bsi.Saturation.SRes			0.100
pfset Geom.Bsi.Saturation.SSat			1.000
pfset Geom.Bsil.Saturation.Alpha			0.51
pfset Geom.Bsil.Saturation.N			2.000
pfset Geom.Bsil.Saturation.SRes			0.150
pfset Geom.Bsil.Saturation.SSat			1.000
pfset Geom.Bsicl.Saturation.Alpha			0.84
pfset Geom.Bsicl.Saturation.N			2.000
pfset Geom.Bsicl.Saturation.SRes			0.190
pfset Geom.Bsicl.Saturation.SSat			1.000
pfset Geom.Bl.Saturation.Alpha			1.11
pfset Geom.Bl.Saturation.N			2.000
pfset Geom.Bl.Saturation.SRes			0.150
pfset Geom.Bl.Saturation.SSat			1.000
pfset Geom.Bsl.Saturation.Alpha			2.67
pfset Geom.Bsl.Saturation.N			2.000
pfset Geom.Bsl.Saturation.SRes			0.100
pfset Geom.Bsl.Saturation.SSat			1.000
pfset Geom.Bcl.Saturation.Alpha			1.58
pfset Geom.Bcl.Saturation.N			2.000
pfset Geom.Bcl.Saturation.SRes			0.180
pfset Geom.Bcl.Saturation.SSat			1.000
pfset Geom.Bscl.Saturation.Alpha			2.11
pfset Geom.Bscl.Saturation.N			2.000
pfset Geom.Bscl.Saturation.SRes			0.160
pfset Geom.Bscl.Saturation.SSat			1.000
pfset Geom.Bsic.Saturation.Alpha			1.62
pfset Geom.Bsic.Saturation.N			2.000
pfset Geom.Bsic.Saturation.SRes			0.230
pfset Geom.Bsic.Saturation.SSat			1.000
pfset Geom.Bc.Saturation.Alpha			1.5
pfset Geom.Bc.Saturation.N			2.000
pfset Geom.Bc.Saturation.SRes			0.210
pfset Geom.Bc.Saturation.SSat			1.000
pfset Geom.Bo.Saturation.Alpha			3.52
pfset Geom.Bo.Saturation.N			3.180
pfset Geom.Bo.Saturation.SRes			0.140
pfset Geom.Bo.Saturation.SSat			1.000
pfset Geom.PR.Saturation.Alpha			3.8
pfset Geom.PR.Saturation.N			2.000
pfset Geom.PR.Saturation.SRes			0.889
pfset Geom.PR.Saturation.SSat			1.000
pfset Geom.Ps.Saturation.Alpha			3.52
pfset Geom.Ps.Saturation.N			3.180
pfset Geom.Ps.Saturation.SRes			0.140
pfset Geom.Ps.Saturation.SSat			1.000
pfset Geom.Pls.Saturation.Alpha			3.48
pfset Geom.Pls.Saturation.N			2.000
pfset Geom.Pls.Saturation.SRes			0.130
pfset Geom.Pls.Saturation.SSat			1.000
pfset Geom.Psi.Saturation.Alpha			0.66
pfset Geom.Psi.Saturation.N			2.000
pfset Geom.Psi.Saturation.SRes			0.100
pfset Geom.Psi.Saturation.SSat			1.000
pfset Geom.Psil.Saturation.Alpha			0.51
pfset Geom.Psil.Saturation.N			2.000
pfset Geom.Psil.Saturation.SRes			0.150
pfset Geom.Psil.Saturation.SSat			1.000
pfset Geom.Psicl.Saturation.Alpha			0.84
pfset Geom.Psicl.Saturation.N			2.000
pfset Geom.Psicl.Saturation.SRes			0.190
pfset Geom.Psicl.Saturation.SSat			1.000
pfset Geom.Pl.Saturation.Alpha			1.11
pfset Geom.Pl.Saturation.N			2.000
pfset Geom.Pl.Saturation.SRes			0.150
pfset Geom.Pl.Saturation.SSat			1.000
pfset Geom.Psl.Saturation.Alpha			2.67
pfset Geom.Psl.Saturation.N			2.000
pfset Geom.Psl.Saturation.SRes			0.100
pfset Geom.Psl.Saturation.SSat			1.000
pfset Geom.Pcl.Saturation.Alpha			1.58
pfset Geom.Pcl.Saturation.N			2.000
pfset Geom.Pcl.Saturation.SRes			0.180
pfset Geom.Pcl.Saturation.SSat			1.000
pfset Geom.Pscl.Saturation.Alpha			2.11
pfset Geom.Pscl.Saturation.N			2.000
pfset Geom.Pscl.Saturation.SRes			0.160
pfset Geom.Pscl.Saturation.SSat			1.000
pfset Geom.Psic.Saturation.Alpha			1.62
pfset Geom.Psic.Saturation.N			2.000
pfset Geom.Psic.Saturation.SRes			0.230
pfset Geom.Psic.Saturation.SSat			1.000
pfset Geom.Pc.Saturation.Alpha			1.5
pfset Geom.Pc.Saturation.N			2.000
pfset Geom.Pc.Saturation.SRes			0.210
pfset Geom.Pc.Saturation.SSat			1.000
pfset Geom.Po.Saturation.Alpha			3.52
pfset Geom.Po.Saturation.N			3.180
pfset Geom.Po.Saturation.SRes			0.140
pfset Geom.Po.Saturation.SSat			1.000
pfset Geom.SR.Saturation.Alpha			0.510
pfset Geom.SR.Saturation.N			2.000
pfset Geom.SR.Saturation.SRes			0.150
pfset Geom.SR.Saturation.SSat			1.000
pfset Geom.Ss.Saturation.Alpha			3.52
pfset Geom.Ss.Saturation.N			3.180
pfset Geom.Ss.Saturation.SRes			0.140
pfset Geom.Ss.Saturation.SSat			1.000
pfset Geom.Sls.Saturation.Alpha			3.48
pfset Geom.Sls.Saturation.N			2.000
pfset Geom.Sls.Saturation.SRes			0.130
pfset Geom.Sls.Saturation.SSat			1.000
pfset Geom.Ssi.Saturation.Alpha			0.66
pfset Geom.Ssi.Saturation.N			2.000
pfset Geom.Ssi.Saturation.SRes			0.100
pfset Geom.Ssi.Saturation.SSat			1.000
pfset Geom.Ssil.Saturation.Alpha			0.51
pfset Geom.Ssil.Saturation.N			2.000
pfset Geom.Ssil.Saturation.SRes			0.150
pfset Geom.Ssil.Saturation.SSat			1.000
pfset Geom.Ssicl.Saturation.Alpha			0.84
pfset Geom.Ssicl.Saturation.N			2.000
pfset Geom.Ssicl.Saturation.SRes			0.190
pfset Geom.Ssicl.Saturation.SSat			1.000
pfset Geom.Sl.Saturation.Alpha			1.11
pfset Geom.Sl.Saturation.N			2.000
pfset Geom.Sl.Saturation.SRes			0.150
pfset Geom.Sl.Saturation.SSat			1.000
pfset Geom.VR.Saturation.Alpha			0.510
pfset Geom.VR.Saturation.N			2.000
pfset Geom.VR.Saturation.SRes			0.150
pfset Geom.VR.Saturation.SSat			1.000
pfset Geom.Vs.Saturation.Alpha			3.52
pfset Geom.Vs.Saturation.N			3.180
pfset Geom.Vs.Saturation.SRes			0.140
pfset Geom.Vs.Saturation.SSat			1.000
pfset Geom.Vls.Saturation.Alpha			3.48
pfset Geom.Vls.Saturation.N			2.000
pfset Geom.Vls.Saturation.SRes			0.130
pfset Geom.Vls.Saturation.SSat			1.000
pfset Geom.Vsi.Saturation.Alpha			0.66
pfset Geom.Vsi.Saturation.N			2.000
pfset Geom.Vsi.Saturation.SRes			0.100
pfset Geom.Vsi.Saturation.SSat			1.000
pfset Geom.Vsil.Saturation.Alpha			0.51
pfset Geom.Vsil.Saturation.N			2.000
pfset Geom.Vsil.Saturation.SRes			0.150
pfset Geom.Vsil.Saturation.SSat			1.000
pfset Geom.Vsicl.Saturation.Alpha			0.84
pfset Geom.Vsicl.Saturation.N			2.000
pfset Geom.Vsicl.Saturation.SRes			0.190
pfset Geom.Vsicl.Saturation.SSat			1.000
pfset Geom.Vl.Saturation.Alpha			1.11
pfset Geom.Vl.Saturation.N			2.000
pfset Geom.Vl.Saturation.SRes			0.150
pfset Geom.Vl.Saturation.SSat			1.000
pfset Geom.Vsl.Saturation.Alpha			2.67
pfset Geom.Vsl.Saturation.N			2.000
pfset Geom.Vsl.Saturation.SRes			0.100
pfset Geom.Vsl.Saturation.SSat			1.000
pfset Geom.Vcl.Saturation.Alpha			1.58
pfset Geom.Vcl.Saturation.N			2.000
pfset Geom.Vcl.Saturation.SRes			0.180
pfset Geom.Vcl.Saturation.SSat			1.000
pfset Geom.Vscl.Saturation.Alpha			2.11
pfset Geom.Vscl.Saturation.N			2.000
pfset Geom.Vscl.Saturation.SRes			0.160
pfset Geom.Vscl.Saturation.SSat			1.000
pfset Geom.Vsic.Saturation.Alpha			1.62
pfset Geom.Vsic.Saturation.N			2.000
pfset Geom.Vsic.Saturation.SRes			0.230
pfset Geom.Vsic.Saturation.SSat			1.000
pfset Geom.Vc.Saturation.Alpha			1.5
pfset Geom.Vc.Saturation.N			2.000
pfset Geom.Vc.Saturation.SRes			0.210
pfset Geom.Vc.Saturation.SSat			1.000
pfset Geom.Vo.Saturation.Alpha			3.52
pfset Geom.Vo.Saturation.N			3.180
pfset Geom.Vo.Saturation.SRes			0.140
pfset Geom.Vo.Saturation.SSat			1.000
pfset Geom.MV.Saturation.Alpha                  3.520
pfset Geom.MV.Saturation.N                      3.180
pfset Geom.MV.Saturation.SRes                   0.140
pfset Geom.MV.Saturation.SSat                   1.00

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------

pfset Wells.Names                           ""

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------

pfset Cycle.Names "constant"
pfset Cycle.constant.Names              "alltime"
pfset Cycle.constant.alltime.Length      10000000
pfset Cycle.constant.Repeat             -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------

pfset BCPressure.PatchNames                   [pfget Geom.domain.Patches]

pfset Patch.x-lower.BCPressure.Type		      FluxConst
pfset Patch.x-lower.BCPressure.Cycle		      "constant"
pfset Patch.x-lower.BCPressure.alltime.Value	      0.0

pfset Patch.y-lower.BCPressure.Type		      FluxConst
pfset Patch.y-lower.BCPressure.Cycle		      "constant"
pfset Patch.y-lower.BCPressure.alltime.Value	      0.0

pfset Patch.z-lower.BCPressure.Type		      FluxConst
pfset Patch.z-lower.BCPressure.Cycle		      "constant"
pfset Patch.z-lower.BCPressure.alltime.Value	       0.0

pfset Patch.x-upper.BCPressure.Type		      FluxConst
pfset Patch.x-upper.BCPressure.Cycle		      "constant"
pfset Patch.x-upper.BCPressure.alltime.Value	      0.0

pfset Patch.y-upper.BCPressure.Type		      FluxConst
pfset Patch.y-upper.BCPressure.Cycle		      "constant"
pfset Patch.y-upper.BCPressure.alltime.Value	      0.0

pfset Patch.z-upper.BCPressure.Type		      OverlandFlow
pfset Patch.z-upper.BCPressure.Cycle		      "constant"
pfset Patch.z-upper.BCPressure.alltime.Value	 0.00000

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

pfset TopoSlopesY.Type "PFBFile"
pfset TopoSlopesY.GeomNames "domain"
pfset TopoSlopesY.FileName  slope_y_Rev032415.pfb


#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

pfset TopoSlopesX.Type "PFBFile"
pfset TopoSlopesX.GeomNames "domain"
pfset TopoSlopesX.FileName slope_x_Rev032415.pfb


#---------------------------------------------------------
# Mannings coefficient
#---------------------------------------------------------

pfset Mannings.Type "PFBFile"
pfset Mannings.GeomNames "domain"
pfset Mannings.FileName CV_1km_ManN.pfb

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

pfset PhaseSources.water.Type                         Constant
pfset PhaseSources.water.GeomNames                    domain
pfset PhaseSources.water.Geom.domain.Value        0.0

#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

pfset KnownSolution                                    NoKnownSolution

#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

pfset Solver                                             Richards
pfset Solver.MaxIter                                     2500000

pfset Solver.TerrainFollowingGrid                        True

pfset Solver.Nonlinear.MaxIter                           400
pfset Solver.Nonlinear.ResidualTol                       1e-5
pfset Solver.Nonlinear.EtaValue                          0.0001

pfset Solver.PrintSubsurf				                        True
pfset  Solver.Drop                                      1E-20
pfset Solver.AbsTol                                     1E-10
pfset Solver.MaxConvergenceFailures                       7

pfset Solver.Nonlinear.UseJacobian                       True
pfset Solver.Nonlinear.DerivativeEpsilon                 1e-16
pfset Solver.Nonlinear.StepTol				 			             1e-20
pfset Solver.Nonlinear.Globalization                     LineSearch
pfset Solver.Linear.KrylovDimension                      250
pfset Solver.Linear.MaxRestarts                           5

pfset Solver.Linear.Preconditioner                       PFMG
pfset Solver.Linear.Preconditioner.PCMatrixType          FullJacobian

pfset Solver.WriteSiloSubsurfData                 False
pfset Solver.WriteSiloPressure                    False
pfset Solver.WriteSiloSaturation                  False
pfset Solver.WriteSiloConcentration               False
pfset Solver.WriteSiloSlopes                      False
pfset Solver.WriteSiloMask                        False

pfset Solver.PrintSubsurfData                     True
pfset Solver.PrintSpecificStorage                 True
pfset Solver.PrintMask                            True
pfset Solver.PrintPressure                        True
pfset Solver.PrintSaturation                      True
pfset Solver.PrintPorosity                        True
pfset Solver.PrintSlopes                          True

#---------------------------------------------------------
# CLM Solver Section:
#---------------------------------------------------------
#Output setup
pfset Solver.LSM                                      CLM
pfset Solver.CLM.Print1dOut                           False
pfset Solver.BinaryOutDir                             False
pfset Solver.CLM.CLMDumpInterval                      1

#Evap and veg stress functions/parameters
pfset Solver.CLM.EvapBeta                             Linear
pfset Solver.CLM.VegWaterStress                       Saturation
pfset Solver.CLM.ResSat                               0.25
pfset Solver.CLM.WiltingPoint                         0.25
pfset Solver.CLM.FieldCapacity                        1.0

#Met forcing and timestep setup
pfset Solver.CLM.MetForcing                           3D
pfset Solver.CLM.MetFileName                          "NLDAS"
pfset Solver.CLM.MetFilePath                          "NLDAS/WY2017"
pfset Solver.CLM.MetFileNT                            240
pfset Solver.CLM.IstepStart                           $istep

#Irrigation setup
pfset Solver.CLM.IrrigationType                       none

pfset Solver.PrintPressure                            True
pfset Solver.PrintSaturation                          True
pfset Solver.WriteCLMBinary                           False

pfset Solver.WriteSiloCLM                             False
pfset Solver.PrintCLM                                 True

pfset Solver.CLM.ReuseCount                           1
pfset Solver.CLM.WriteLogs 	                          False
pfset Solver.CLM.WriteLastRST                         True
pfset Solver.CLM.DailyRST                             True
pfset Solver.CLM.SingleFile                           True

pfset Solver.CLM.RootZoneNZ                           4
pfset Solver.CLM.SoiLayer                             4


#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

pfset Geom.domain.ICPressure.RefGeom                    domain
pfset Geom.domain.ICPressure.RefPatch                   z-lower

# restart from last timestep
pfset ICPressure.Type                                   PFBFile
pfset ICPressure.GeomNames                              domain
pfset Geom.domain.ICPressure.FileName                   pfinit.pfb
pfdist pfinit.pfb

#---------
##  Distribute slopes
#---------

pfset ComputationalGrid.NZ                1

pfdist slope_y_Rev032415.pfb
pfdist slope_x_Rev032415.pfb
pfdist CV_1km_ManN.pfb

pfset ComputationalGrid.NZ                5

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------

pfwritedb $runname
#pfrun $runname # comment out pfrun command for running on Cheyenne
#pfundist $runname
