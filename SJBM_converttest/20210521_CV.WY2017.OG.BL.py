#------------------------------------------------------------------
# *original version*
# a constant applied annual P minus E, 5-layers vertical
# discretization [jg 5/16/14]
# *modified version, for pftools tutorial*
# LThatch, May 21, 2021
#-------------------------------------------------------------------

tcl_precision = 17

#---------------------------------------------------------
# Import ParFlow TCL package
#---------------------------------------------------------

from parflow import Run
20210521_CV.WY2017.OG.BL = Run("20210521_CV.WY2017.OG.BL", __file__)

20210521_CV.WY2017.OG.BL.FileVersion = 4

20210521_CV.WY2017.OG.BL.Process.Topology.P = 18
20210521_CV.WY2017.OG.BL.Process.Topology.Q = 14
20210521_CV.WY2017.OG.BL.Process.Topology.R = 1


#---------------------------------------------------------
# User Settings
#---------------------------------------------------------

oldrunname = 'CV.WY2017to2019.1km.5lay.BL.SU2009_Y17 ;#used for initial condition'
runname = 'CV.WY2017.OG.BL'

istep = 1

NLDASdist = 0
year_restart = 1 ;# to 1 if starting over at a new year (with a new runname)
#                     ;# set to 0 if restarting within a year (or same runname)

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------

20210521_CV.WY2017.OG.BL.ComputationalGrid.Lower.X = 0.0
20210521_CV.WY2017.OG.BL.ComputationalGrid.Lower.Y = 0.0
20210521_CV.WY2017.OG.BL.ComputationalGrid.Lower.Z = 0.0

20210521_CV.WY2017.OG.BL.ComputationalGrid.NX = 270
20210521_CV.WY2017.OG.BL.ComputationalGrid.NY = 220
20210521_CV.WY2017.OG.BL.ComputationalGrid.NZ = 5

20210521_CV.WY2017.OG.BL.ComputationalGrid.DX = 1000.0
20210521_CV.WY2017.OG.BL.ComputationalGrid.DY = 1000.0
20210521_CV.WY2017.OG.BL.ComputationalGrid.DZ = 100.0

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------

20210521_CV.WY2017.OG.BL.GeomInput.Names = 'domaininput ind_input'

20210521_CV.WY2017.OG.BL.GeomInput.domaininput.GeomName = 'domain'
20210521_CV.WY2017.OG.BL.GeomInput.domaininput.InputType = 'Box'

#---------------------------------------------------------
# Domain Geometry 
#---------------------------------------------------------

20210521_CV.WY2017.OG.BL.Geom.domain.Lower.X = 0.0
20210521_CV.WY2017.OG.BL.Geom.domain.Lower.Y = 0.0
20210521_CV.WY2017.OG.BL.Geom.domain.Lower.Z = 0.0
#  
20210521_CV.WY2017.OG.BL.Geom.domain.Upper.X = 270000.0
20210521_CV.WY2017.OG.BL.Geom.domain.Upper.Y = 220000.0
20210521_CV.WY2017.OG.BL.Geom.domain.Upper.Z = 500.0
20210521_CV.WY2017.OG.BL.Geom.domain.Patches = 'x_lower x_upper y_lower y_upper z_lower z_upper'

#----------------------------------------------------------------------------
# Start/Stop times
#----------------------------------------------------------------------------

nproc = [expr [pfget Process.Topology.P]*[pfget Process.Topology.Q]*[pfget Process.Topology.R]]
runlength = 8760

startcount = [expr (int($istep-1))]
starttime = [expr $istep-1]
stoptime = $runlength ;#[expr ($runlength -$startcount)]

# Copy final pressure to PFB for restart
last = [expr $istep-1] ;# $final_actual_press_index
# if {$year_restart ==1} then {
#     set fname_ic [format "%s.out.press.08760.pfb"  $oldrunname]
# } else {
#     set fname_ic [format "%s.out.press.%05d.pfb" $runname $last]
# }
# exec cp $fname_ic pfinit.pfb
# puts [format "Using %s for initial pressure" $fname_ic]

#-----------------------------------------------------------
# Distribute NLDAS Forcing files
#-----------------------------------------------------------

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

#-----------------------------------------------------------------------------
# Subsurface Indicator Geometry Input
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.ComputationalGrid.NZ = 5
20210521_CV.WY2017.OG.BL.GeomInput.ind_input.InputType = 'IndicatorField'
20210521_CV.WY2017.OG.BL.GeomInput.ind_input.GeomNames = 'BR Bs Bls Bsi Bsil Bsicl Bl Bsl Bcl Bscl Bsic Bc Bo PR Ps Pls Psi Psil Psicl Pl Psl Pcl Pscl Psic Pc Po SR Ss Sls Ssi Ssil Ssicl Sl VR Vs Vls Vsi Vsil Vsicl Vl Vsl Vcl Vscl Vsic Vc Vo MV'
20210521_CV.WY2017.OG.BL.Geom.ind_input.FileName = 'text_ind.270i220j500k.v3.UniqCatAgg_5lay111514.pfb'
20210521_CV.WY2017.OG.BL.GeomInput.BR.Value = 0
20210521_CV.WY2017.OG.BL.GeomInput.Bs.Value = 1
20210521_CV.WY2017.OG.BL.GeomInput.Bls.Value = 2
20210521_CV.WY2017.OG.BL.GeomInput.Bsi.Value = 3
20210521_CV.WY2017.OG.BL.GeomInput.Bsil.Value = 4
20210521_CV.WY2017.OG.BL.GeomInput.Bsicl.Value = 5
20210521_CV.WY2017.OG.BL.GeomInput.Bl.Value = 6
20210521_CV.WY2017.OG.BL.GeomInput.Bsl.Value = 7
20210521_CV.WY2017.OG.BL.GeomInput.Bcl.Value = 8
20210521_CV.WY2017.OG.BL.GeomInput.Bscl.Value = 9
20210521_CV.WY2017.OG.BL.GeomInput.Bsic.Value = 10
20210521_CV.WY2017.OG.BL.GeomInput.Bc.Value = 11
20210521_CV.WY2017.OG.BL.GeomInput.Bo.Value = 12
20210521_CV.WY2017.OG.BL.GeomInput.PR.Value = 13
20210521_CV.WY2017.OG.BL.GeomInput.Ps.Value = 14
20210521_CV.WY2017.OG.BL.GeomInput.Pls.Value = 15
20210521_CV.WY2017.OG.BL.GeomInput.Psi.Value = 16
20210521_CV.WY2017.OG.BL.GeomInput.Psil.Value = 17
20210521_CV.WY2017.OG.BL.GeomInput.Psicl.Value = 18
20210521_CV.WY2017.OG.BL.GeomInput.Pl.Value = 19
20210521_CV.WY2017.OG.BL.GeomInput.Psl.Value = 20
20210521_CV.WY2017.OG.BL.GeomInput.Pcl.Value = 21
20210521_CV.WY2017.OG.BL.GeomInput.Pscl.Value = 22
20210521_CV.WY2017.OG.BL.GeomInput.Psic.Value = 23
20210521_CV.WY2017.OG.BL.GeomInput.Pc.Value = 24
20210521_CV.WY2017.OG.BL.GeomInput.Po.Value = 25
20210521_CV.WY2017.OG.BL.GeomInput.SR.Value = 26
20210521_CV.WY2017.OG.BL.GeomInput.Ss.Value = 27
20210521_CV.WY2017.OG.BL.GeomInput.Sls.Value = 28
20210521_CV.WY2017.OG.BL.GeomInput.Ssi.Value = 29
20210521_CV.WY2017.OG.BL.GeomInput.Ssil.Value = 30
20210521_CV.WY2017.OG.BL.GeomInput.Ssicl.Value = 31
20210521_CV.WY2017.OG.BL.GeomInput.Sl.Value = 32
20210521_CV.WY2017.OG.BL.GeomInput.VR.Value = 33
20210521_CV.WY2017.OG.BL.GeomInput.Vs.Value = 34
20210521_CV.WY2017.OG.BL.GeomInput.Vls.Value = 35
20210521_CV.WY2017.OG.BL.GeomInput.Vsi.Value = 36
20210521_CV.WY2017.OG.BL.GeomInput.Vsil.Value = 37
20210521_CV.WY2017.OG.BL.GeomInput.Vsicl.Value = 38
20210521_CV.WY2017.OG.BL.GeomInput.Vl.Value = 39
20210521_CV.WY2017.OG.BL.GeomInput.Vsl.Value = 40
20210521_CV.WY2017.OG.BL.GeomInput.Vcl.Value = 41
20210521_CV.WY2017.OG.BL.GeomInput.Vscl.Value = 42
20210521_CV.WY2017.OG.BL.GeomInput.Vsic.Value = 43
20210521_CV.WY2017.OG.BL.GeomInput.Vc.Value = 44
20210521_CV.WY2017.OG.BL.GeomInput.Vo.Value = 45
20210521_CV.WY2017.OG.BL.GeomInput.MV.Value = 46

#--------------------------------------------
# variable dz assignments
#------------------------------------------

20210521_CV.WY2017.OG.BL.Solver.Nonlinear.VariableDz = True
20210521_CV.WY2017.OG.BL.dzScale.GeomNames = 'domain'
20210521_CV.WY2017.OG.BL.dzScale.Type = 'nzList'
20210521_CV.WY2017.OG.BL.dzScale.nzListNumber = 5

# 5 layers, starts at 0 for the bottom to 4 at the top
20210521_CV.WY2017.OG.BL.Cell.0.dzScale.Value = 4.98
20210521_CV.WY2017.OG.BL.Cell.1.dzScale.Value = 0.01
20210521_CV.WY2017.OG.BL.Cell.2.dzScale.Value = 0.006
20210521_CV.WY2017.OG.BL.Cell.3.dzScale.Value = 0.003
20210521_CV.WY2017.OG.BL.Cell.4.dzScale.Value = 0.001

#-----------------------------------------------------------------------------
# Perm - Horizontal Values
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.Geom.Perm.Names = 'BR Bs Bls Bsi Bsil Bsicl Bl Bsl Bcl Bscl Bsic Bc Bo PR Ps Pls Psi Psil Psicl Pl Psl Pcl Pscl Psic Pc Po SR Ss Sls Ssi Ssil Ssicl Sl VR Vs Vls Vsi Vsil Vsicl Vl Vsl Vcl Vscl Vsic Vc Vo MV'

20210521_CV.WY2017.OG.BL.Geom.BR.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.BR.Perm.Value = 0.0042
20210521_CV.WY2017.OG.BL.Geom.Bs.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bs.Perm.Value = 2.9943496
20210521_CV.WY2017.OG.BL.Geom.Bls.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bls.Perm.Value = 1.0146179
20210521_CV.WY2017.OG.BL.Geom.Bsi.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bsi.Perm.Value = 0.3437973
20210521_CV.WY2017.OG.BL.Geom.Bsil.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bsil.Perm.Value = 0.1219839
20210521_CV.WY2017.OG.BL.Geom.Bsicl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bsicl.Perm.Value = 0.0432815
20210521_CV.WY2017.OG.BL.Geom.Bl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bl.Perm.Value = 0.0127733
20210521_CV.WY2017.OG.BL.Geom.Bsl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bsl.Perm.Value = 0.0049694
20210521_CV.WY2017.OG.BL.Geom.Bcl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bcl.Perm.Value = 0.0021198
20210521_CV.WY2017.OG.BL.Geom.Bscl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bscl.Perm.Value = 0.0007697
20210521_CV.WY2017.OG.BL.Geom.Bsic.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bsic.Perm.Value = 0.0002549
20210521_CV.WY2017.OG.BL.Geom.Bc.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bc.Perm.Value = 0.0000992
20210521_CV.WY2017.OG.BL.Geom.Bo.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bo.Perm.Value = 7.5214661
20210521_CV.WY2017.OG.BL.Geom.PR.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.PR.Perm.Value = 0.0003456
20210521_CV.WY2017.OG.BL.Geom.Ps.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Ps.Perm.Value = 2.9943496
20210521_CV.WY2017.OG.BL.Geom.Pls.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Pls.Perm.Value = 1.0146179
20210521_CV.WY2017.OG.BL.Geom.Psi.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Psi.Perm.Value = 0.3437973
20210521_CV.WY2017.OG.BL.Geom.Psil.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Psil.Perm.Value = 0.1219839
20210521_CV.WY2017.OG.BL.Geom.Psicl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Psicl.Perm.Value = 0.0432815
20210521_CV.WY2017.OG.BL.Geom.Pl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Pl.Perm.Value = 0.0127733
20210521_CV.WY2017.OG.BL.Geom.Psl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Psl.Perm.Value = 0.0049694
20210521_CV.WY2017.OG.BL.Geom.Pcl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Pcl.Perm.Value = 0.0021198
20210521_CV.WY2017.OG.BL.Geom.Pscl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Pscl.Perm.Value = 0.0007697
20210521_CV.WY2017.OG.BL.Geom.Psic.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Psic.Perm.Value = 0.0002549
20210521_CV.WY2017.OG.BL.Geom.Pc.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Pc.Perm.Value = 0.0000992
20210521_CV.WY2017.OG.BL.Geom.Po.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Po.Perm.Value = 7.5214661
20210521_CV.WY2017.OG.BL.Geom.SR.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.SR.Perm.Value = 0.0000992
20210521_CV.WY2017.OG.BL.Geom.Ss.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Ss.Perm.Value = 2.9943496
20210521_CV.WY2017.OG.BL.Geom.Sls.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Sls.Perm.Value = 1.0146179
20210521_CV.WY2017.OG.BL.Geom.Ssi.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Ssi.Perm.Value = 0.3437973
20210521_CV.WY2017.OG.BL.Geom.Ssil.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Ssil.Perm.Value = 0.1219839
20210521_CV.WY2017.OG.BL.Geom.Ssicl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Ssicl.Perm.Value = 0.0432815
20210521_CV.WY2017.OG.BL.Geom.Sl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Sl.Perm.Value = 0.0127733
20210521_CV.WY2017.OG.BL.Geom.VR.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.VR.Perm.Value = 0.0000992
20210521_CV.WY2017.OG.BL.Geom.Vs.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vs.Perm.Value = 2.9943496
20210521_CV.WY2017.OG.BL.Geom.Vls.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vls.Perm.Value = 1.0146179
20210521_CV.WY2017.OG.BL.Geom.Vsi.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vsi.Perm.Value = 0.3437973
20210521_CV.WY2017.OG.BL.Geom.Vsil.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vsil.Perm.Value = 0.1219839
20210521_CV.WY2017.OG.BL.Geom.Vsicl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vsicl.Perm.Value = 0.0432815
20210521_CV.WY2017.OG.BL.Geom.Vl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vl.Perm.Value = 0.0127733
20210521_CV.WY2017.OG.BL.Geom.Vsl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vsl.Perm.Value = 0.0049694
20210521_CV.WY2017.OG.BL.Geom.Vcl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vcl.Perm.Value = 0.0021198
20210521_CV.WY2017.OG.BL.Geom.Vscl.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vscl.Perm.Value = 0.0007697
20210521_CV.WY2017.OG.BL.Geom.Vsic.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vsic.Perm.Value = 0.0002549
20210521_CV.WY2017.OG.BL.Geom.Vc.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vc.Perm.Value = 0.0000992
20210521_CV.WY2017.OG.BL.Geom.Vo.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vo.Perm.Value = 7.5214661
20210521_CV.WY2017.OG.BL.Geom.MV.Perm.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.MV.Perm.Value = 0.041667
#-----------------------------------------------------------------------------
# Perm - Tensors
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.Perm.TensorType = 'TensorByGeom'
20210521_CV.WY2017.OG.BL.Geom.Perm.TensorByGeom.Names = 'BR Bs Bls Bsi Bsil Bsicl Bl Bsl Bcl Bscl Bsic Bc Bo PR Ps Pls Psi Psil Psicl Pl Psl Pcl Pscl Psic Pc Po SR Ss Sls Ssi Ssil Ssicl Sl VR Vs Vls Vsi Vsil Vsicl Vl Vsl Vcl Vscl Vsic Vc Vo MV'

20210521_CV.WY2017.OG.BL.Geom.BR.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.BR.Perm.TensorValY = 1.00
#pfset Geom.BR.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.BR.Perm.TensorValZ = 0.95833
20210521_CV.WY2017.OG.BL.Geom.Bs.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Bs.Perm.TensorValY = 1.00
#pfset Geom.Bs.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Bs.Perm.TensorValZ = 0.02344
20210521_CV.WY2017.OG.BL.Geom.Bls.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Bls.Perm.TensorValY = 1.00
#pfset Geom.Bls.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Bls.Perm.TensorValZ = 0.03802
20210521_CV.WY2017.OG.BL.Geom.Bsi.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Bsi.Perm.TensorValY = 1.00
#pfset Geom.Bsi.Perm.TensorValZ  1.00 
20210521_CV.WY2017.OG.BL.Geom.Bsi.Perm.TensorValZ = 0.06026
20210521_CV.WY2017.OG.BL.Geom.Bsil.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Bsil.Perm.TensorValY = 1.00
#pfset Geom.Bsil.Perm.TensorValZ  1.00  
20210521_CV.WY2017.OG.BL.Geom.Bsil.Perm.TensorValZ = 0.08318
20210521_CV.WY2017.OG.BL.Geom.Bsicl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Bsicl.Perm.TensorValY = 1.00
#pfset Geom.Bsicl.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Bsicl.Perm.TensorValZ = 0.10965
20210521_CV.WY2017.OG.BL.Geom.Bl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Bl.Perm.TensorValY = 1.00
#pfset Geom.Bl.Perm.TensorValZ  1.00    
20210521_CV.WY2017.OG.BL.Geom.Bl.Perm.TensorValZ = 0.12882
20210521_CV.WY2017.OG.BL.Geom.Bsl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Bsl.Perm.TensorValY = 1.00
#pfset Geom.Bsl.Perm.TensorValZ  1.00    
20210521_CV.WY2017.OG.BL.Geom.Bsl.Perm.TensorValZ = 0.13183
20210521_CV.WY2017.OG.BL.Geom.Bcl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Bcl.Perm.TensorValY = 1.00
#pfset Geom.Bcl.Perm.TensorValZ  1.00    
20210521_CV.WY2017.OG.BL.Geom.Bcl.Perm.TensorValZ = 0.11749
20210521_CV.WY2017.OG.BL.Geom.Bscl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Bscl.Perm.TensorValY = 1.00
#pfset Geom.Bscl.Perm.TensorValZ  1.00    
20210521_CV.WY2017.OG.BL.Geom.Bscl.Perm.TensorValZ = 0.08913
20210521_CV.WY2017.OG.BL.Geom.Bsic.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Bsic.Perm.TensorValY = 1.00
#pfset Geom.Bsic.Perm.TensorValZ  1.00    
20210521_CV.WY2017.OG.BL.Geom.Bsic.Perm.TensorValZ = 0.05248
20210521_CV.WY2017.OG.BL.Geom.Bc.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Bc.Perm.TensorValY = 1.00
#pfset Geom.Bc.Perm.TensorValZ  1.00      
20210521_CV.WY2017.OG.BL.Geom.Bc.Perm.TensorValZ = 0.02455
20210521_CV.WY2017.OG.BL.Geom.Bo.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Bo.Perm.TensorValY = 1.00
#pfset Geom.Bo.Perm.TensorValZ  1.00   
20210521_CV.WY2017.OG.BL.Geom.Bo.Perm.TensorValZ = 0.01479
20210521_CV.WY2017.OG.BL.Geom.PR.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.PR.Perm.TensorValY = 1.00
#pfset Geom.PR.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.PR.Perm.TensorValZ = 0.95833
20210521_CV.WY2017.OG.BL.Geom.Ps.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Ps.Perm.TensorValY = 1.00
#pfset Geom.Ps.Perm.TensorValZ  1.00  
20210521_CV.WY2017.OG.BL.Geom.Ps.Perm.TensorValZ = 0.02344
20210521_CV.WY2017.OG.BL.Geom.Pls.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Pls.Perm.TensorValY = 1.00
#pfset Geom.Pls.Perm.TensorValZ  1.00  
20210521_CV.WY2017.OG.BL.Geom.Pls.Perm.TensorValZ = 0.03802
20210521_CV.WY2017.OG.BL.Geom.Psi.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Psi.Perm.TensorValY = 1.00
#pfset Geom.Psi.Perm.TensorValZ  1.00  
20210521_CV.WY2017.OG.BL.Geom.Psi.Perm.TensorValZ = 0.06026
20210521_CV.WY2017.OG.BL.Geom.Psil.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Psil.Perm.TensorValY = 1.00
#pfset Geom.Psil.Perm.TensorValZ  1.00 
20210521_CV.WY2017.OG.BL.Geom.Psil.Perm.TensorValZ = 0.08318
20210521_CV.WY2017.OG.BL.Geom.Psicl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Psicl.Perm.TensorValY = 1.00
#pfset Geom.Psicl.Perm.TensorValZ  1.00 
20210521_CV.WY2017.OG.BL.Geom.Psicl.Perm.TensorValZ = 0.10965
20210521_CV.WY2017.OG.BL.Geom.Pl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Pl.Perm.TensorValY = 1.00
#pfset Geom.Pl.Perm.TensorValZ  1.00  
20210521_CV.WY2017.OG.BL.Geom.Pl.Perm.TensorValZ = 0.12882
20210521_CV.WY2017.OG.BL.Geom.Psl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Psl.Perm.TensorValY = 1.00
#pfset Geom.Psl.Perm.TensorValZ  1.00  
20210521_CV.WY2017.OG.BL.Geom.Psl.Perm.TensorValZ = 0.13183
20210521_CV.WY2017.OG.BL.Geom.Pcl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Pcl.Perm.TensorValY = 1.00
#pfset Geom.Pcl.Perm.TensorValZ  1.00  
20210521_CV.WY2017.OG.BL.Geom.Pcl.Perm.TensorValZ = 0.11749
20210521_CV.WY2017.OG.BL.Geom.Pscl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Pscl.Perm.TensorValY = 1.00
#pfset Geom.Pscl.Perm.TensorValZ  1.00  
20210521_CV.WY2017.OG.BL.Geom.Pscl.Perm.TensorValZ = 0.08913
20210521_CV.WY2017.OG.BL.Geom.Psic.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Psic.Perm.TensorValY = 1.00
#pfset Geom.Psic.Perm.TensorValZ  1.00  
20210521_CV.WY2017.OG.BL.Geom.Psic.Perm.TensorValZ = 0.05248
20210521_CV.WY2017.OG.BL.Geom.Pc.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Pc.Perm.TensorValY = 1.00
#pfset Geom.Pc.Perm.TensorValZ  1.00   
20210521_CV.WY2017.OG.BL.Geom.Pc.Perm.TensorValZ = 0.02455
20210521_CV.WY2017.OG.BL.Geom.Po.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Po.Perm.TensorValY = 1.00
#pfset Geom.Po.Perm.TensorValZ  1.00   
20210521_CV.WY2017.OG.BL.Geom.Po.Perm.TensorValZ = 0.01479
20210521_CV.WY2017.OG.BL.Geom.SR.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.SR.Perm.TensorValY = 1.00
#pfset Geom.SR.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.SR.Perm.TensorValZ = 0.02455
20210521_CV.WY2017.OG.BL.Geom.Ss.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Ss.Perm.TensorValY = 1.00
#pfset Geom.Ss.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Ss.Perm.TensorValZ = 0.02344
20210521_CV.WY2017.OG.BL.Geom.Sls.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Sls.Perm.TensorValY = 1.00
#pfset Geom.Sls.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Sls.Perm.TensorValZ = 0.03802
20210521_CV.WY2017.OG.BL.Geom.Ssi.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Ssi.Perm.TensorValY = 1.00
#pfset Geom.Ssi.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Ssi.Perm.TensorValZ = 0.06026
20210521_CV.WY2017.OG.BL.Geom.Ssil.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Ssil.Perm.TensorValY = 1.00
#pfset Geom.Ssil.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Ssil.Perm.TensorValZ = 0.08318
20210521_CV.WY2017.OG.BL.Geom.Ssicl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Ssicl.Perm.TensorValY = 1.00
#pfset Geom.Ssicl.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Ssicl.Perm.TensorValZ = 0.10965
20210521_CV.WY2017.OG.BL.Geom.Sl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Sl.Perm.TensorValY = 1.00
#pfset Geom.Sl.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Sl.Perm.TensorValZ = 0.12882
20210521_CV.WY2017.OG.BL.Geom.VR.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.VR.Perm.TensorValY = 1.00
#pfset Geom.VR.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.VR.Perm.TensorValZ = 0.02455
20210521_CV.WY2017.OG.BL.Geom.Vs.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Vs.Perm.TensorValY = 1.00
#pfset Geom.Vs.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Vs.Perm.TensorValZ = 0.02344
20210521_CV.WY2017.OG.BL.Geom.Vls.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Vls.Perm.TensorValY = 1.00
#pfset Geom.Vls.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Vls.Perm.TensorValZ = 0.03802
20210521_CV.WY2017.OG.BL.Geom.Vsi.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Vsi.Perm.TensorValY = 1.00
#pfset Geom.Vsi.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Vsi.Perm.TensorValZ = 0.06026
20210521_CV.WY2017.OG.BL.Geom.Vsil.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Vsil.Perm.TensorValY = 1.00
#pfset Geom.Vsil.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Vsil.Perm.TensorValZ = 0.08318
20210521_CV.WY2017.OG.BL.Geom.Vsicl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Vsicl.Perm.TensorValY = 1.00
#pfset Geom.Vsicl.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Vsicl.Perm.TensorValZ = 0.10965
20210521_CV.WY2017.OG.BL.Geom.Vl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Vl.Perm.TensorValY = 1.00
#pfset Geom.Vl.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Vl.Perm.TensorValZ = 0.12882
20210521_CV.WY2017.OG.BL.Geom.Vsl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Vsl.Perm.TensorValY = 1.00
#pfset Geom.Vsl.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Vsl.Perm.TensorValZ = 0.13183
20210521_CV.WY2017.OG.BL.Geom.Vcl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Vcl.Perm.TensorValY = 1.00
#pfset Geom.Vcl.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Vcl.Perm.TensorValZ = 0.11749
20210521_CV.WY2017.OG.BL.Geom.Vscl.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Vscl.Perm.TensorValY = 1.00
#pfset Geom.Vscl.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Vscl.Perm.TensorValZ = 0.08913
20210521_CV.WY2017.OG.BL.Geom.Vsic.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Vsic.Perm.TensorValY = 1.00
#pfset Geom.Vsic.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Vsic.Perm.TensorValZ = 0.05248
20210521_CV.WY2017.OG.BL.Geom.Vc.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Vc.Perm.TensorValY = 1.00
#pfset Geom.Vc.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Vc.Perm.TensorValZ = 0.02455
20210521_CV.WY2017.OG.BL.Geom.Vo.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.Vo.Perm.TensorValY = 1.00
#pfset Geom.Vo.Perm.TensorValZ  1.00
20210521_CV.WY2017.OG.BL.Geom.Vo.Perm.TensorValZ = 0.01479
20210521_CV.WY2017.OG.BL.Geom.MV.Perm.TensorValX = 1.00
20210521_CV.WY2017.OG.BL.Geom.MV.Perm.TensorValY = 1.00
20210521_CV.WY2017.OG.BL.Geom.MV.Perm.TensorValZ = 0.1 ;# a vertical anisotropy of 1/10 used here as a first approximation - not based on any specific reference value

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.SpecificStorage.Type = 'Constant'
20210521_CV.WY2017.OG.BL.SpecificStorage.GeomNames = 'domain'
20210521_CV.WY2017.OG.BL.Geom.domain.SpecificStorage.Value = 1.0e-5

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.Phase.Names = 'water'

20210521_CV.WY2017.OG.BL.Phase.water.Density.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Phase.water.Density.Value = 1.0

20210521_CV.WY2017.OG.BL.Phase.water.Viscosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.TimingInfo.BaseUnit = 1.0
20210521_CV.WY2017.OG.BL.TimingInfo.StartCount = startcount
20210521_CV.WY2017.OG.BL.TimingInfo.StartTime = starttime
20210521_CV.WY2017.OG.BL.TimingInfo.DumpInterval = 1.0
20210521_CV.WY2017.OG.BL.TimingInfo.StopTime = stoptime

20210521_CV.WY2017.OG.BL.TimeStep.Type = 'Constant'
20210521_CV.WY2017.OG.BL.TimeStep.Value = 1.0

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.Geom.Porosity.GeomNames = 'BR Bs Bls Bsi Bsil Bsicl Bl Bsl Bcl Bscl Bsic Bc Bo PR Ps Pls Psi Psil Psicl Pl Psl Pcl Pscl Psic Pc Po SR Ss Sls Ssi Ssil Ssicl Sl VR Vs Vls Vsi Vsil Vsicl Vl Vsl Vcl Vscl Vsic Vc Vo MV'

20210521_CV.WY2017.OG.BL.Geom.BR.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.BR.Porosity.Value = 0.045
20210521_CV.WY2017.OG.BL.Geom.Bs.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bs.Porosity.Value = 0.290
20210521_CV.WY2017.OG.BL.Geom.Bls.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bls.Porosity.Value = 0.320
20210521_CV.WY2017.OG.BL.Geom.Bsi.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bsi.Porosity.Value = 0.360
20210521_CV.WY2017.OG.BL.Geom.Bsil.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bsil.Porosity.Value = 0.390
20210521_CV.WY2017.OG.BL.Geom.Bsicl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bsicl.Porosity.Value = 0.420
20210521_CV.WY2017.OG.BL.Geom.Bl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bl.Porosity.Value = 0.460
20210521_CV.WY2017.OG.BL.Geom.Bsl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bsl.Porosity.Value = 0.490
20210521_CV.WY2017.OG.BL.Geom.Bcl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bcl.Porosity.Value = 0.510
20210521_CV.WY2017.OG.BL.Geom.Bscl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bscl.Porosity.Value = 0.540
20210521_CV.WY2017.OG.BL.Geom.Bsic.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bsic.Porosity.Value = 0.580
20210521_CV.WY2017.OG.BL.Geom.Bc.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bc.Porosity.Value = 0.610
20210521_CV.WY2017.OG.BL.Geom.Bo.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Bo.Porosity.Value = 0.260
20210521_CV.WY2017.OG.BL.Geom.PR.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.PR.Porosity.Value = 0.045
20210521_CV.WY2017.OG.BL.Geom.Ps.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Ps.Porosity.Value = 0.290
20210521_CV.WY2017.OG.BL.Geom.Pls.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Pls.Porosity.Value = 0.320
20210521_CV.WY2017.OG.BL.Geom.Psi.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Psi.Porosity.Value = 0.360
20210521_CV.WY2017.OG.BL.Geom.Psil.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Psil.Porosity.Value = 0.390
20210521_CV.WY2017.OG.BL.Geom.Psicl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Psicl.Porosity.Value = 0.420
20210521_CV.WY2017.OG.BL.Geom.Pl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Pl.Porosity.Value = 0.460
20210521_CV.WY2017.OG.BL.Geom.Psl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Psl.Porosity.Value = 0.490
20210521_CV.WY2017.OG.BL.Geom.Pcl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Pcl.Porosity.Value = 0.510
20210521_CV.WY2017.OG.BL.Geom.Pscl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Pscl.Porosity.Value = 0.540
20210521_CV.WY2017.OG.BL.Geom.Psic.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Psic.Porosity.Value = 0.580
20210521_CV.WY2017.OG.BL.Geom.Pc.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Pc.Porosity.Value = 0.610
20210521_CV.WY2017.OG.BL.Geom.Po.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Po.Porosity.Value = 0.260
20210521_CV.WY2017.OG.BL.Geom.SR.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.SR.Porosity.Value = 0.110
20210521_CV.WY2017.OG.BL.Geom.Ss.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Ss.Porosity.Value = 0.290
20210521_CV.WY2017.OG.BL.Geom.Sls.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Sls.Porosity.Value = 0.320
20210521_CV.WY2017.OG.BL.Geom.Ssi.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Ssi.Porosity.Value = 0.360
20210521_CV.WY2017.OG.BL.Geom.Ssil.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Ssil.Porosity.Value = 0.390
20210521_CV.WY2017.OG.BL.Geom.Ssicl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Ssicl.Porosity.Value = 0.420
20210521_CV.WY2017.OG.BL.Geom.Sl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Sl.Porosity.Value = 0.460
20210521_CV.WY2017.OG.BL.Geom.VR.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.VR.Porosity.Value = 0.110
20210521_CV.WY2017.OG.BL.Geom.Vs.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vs.Porosity.Value = 0.290
20210521_CV.WY2017.OG.BL.Geom.Vls.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vls.Porosity.Value = 0.320
20210521_CV.WY2017.OG.BL.Geom.Vsi.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vsi.Porosity.Value = 0.360
20210521_CV.WY2017.OG.BL.Geom.Vsil.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vsil.Porosity.Value = 0.390
20210521_CV.WY2017.OG.BL.Geom.Vsicl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vsicl.Porosity.Value = 0.420
20210521_CV.WY2017.OG.BL.Geom.Vl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vl.Porosity.Value = 0.460
20210521_CV.WY2017.OG.BL.Geom.Vsl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vsl.Porosity.Value = 0.490
20210521_CV.WY2017.OG.BL.Geom.Vcl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vcl.Porosity.Value = 0.510
20210521_CV.WY2017.OG.BL.Geom.Vscl.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vscl.Porosity.Value = 0.540
20210521_CV.WY2017.OG.BL.Geom.Vsic.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vsic.Porosity.Value = 0.580
20210521_CV.WY2017.OG.BL.Geom.Vc.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vc.Porosity.Value = 0.610
20210521_CV.WY2017.OG.BL.Geom.Vo.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.Vo.Porosity.Value = 0.260
20210521_CV.WY2017.OG.BL.Geom.MV.Porosity.Type = 'Constant'
20210521_CV.WY2017.OG.BL.Geom.MV.Porosity.Value = 0.150

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.Phase.RelPerm.Type = 'VanGenuchten'
20210521_CV.WY2017.OG.BL.Phase.RelPerm.GeomNames = 'BR Bs Bls Bsi Bsil Bsicl Bl Bsl Bcl Bscl Bsic Bc Bo PR Ps Pls Psi Psil Psicl Pl Psl Pcl Pscl Psic Pc Po SR Ss Sls Ssi Ssil Ssicl Sl VR Vs Vls Vsi Vsil Vsicl Vl Vsl Vcl Vscl Vsic Vc Vo MV'

20210521_CV.WY2017.OG.BL.Geom.BR.RelPerm.Alpha = 3.8
20210521_CV.WY2017.OG.BL.Geom.BR.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bs.RelPerm.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Bs.RelPerm.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.Bls.RelPerm.Alpha = 3.48
20210521_CV.WY2017.OG.BL.Geom.Bls.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bsi.RelPerm.Alpha = 0.66
20210521_CV.WY2017.OG.BL.Geom.Bsi.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bsil.RelPerm.Alpha = 0.51
20210521_CV.WY2017.OG.BL.Geom.Bsil.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bsicl.RelPerm.Alpha = 0.84
20210521_CV.WY2017.OG.BL.Geom.Bsicl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bl.RelPerm.Alpha = 1.11
20210521_CV.WY2017.OG.BL.Geom.Bl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bsl.RelPerm.Alpha = 2.67
20210521_CV.WY2017.OG.BL.Geom.Bsl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bcl.RelPerm.Alpha = 1.58
20210521_CV.WY2017.OG.BL.Geom.Bcl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bscl.RelPerm.Alpha = 2.11
20210521_CV.WY2017.OG.BL.Geom.Bscl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bsic.RelPerm.Alpha = 1.62
20210521_CV.WY2017.OG.BL.Geom.Bsic.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bc.RelPerm.Alpha = 1.5
20210521_CV.WY2017.OG.BL.Geom.Bc.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bo.RelPerm.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Bo.RelPerm.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.PR.RelPerm.Alpha = 3.8
20210521_CV.WY2017.OG.BL.Geom.PR.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Ps.RelPerm.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Ps.RelPerm.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.Pls.RelPerm.Alpha = 3.48
20210521_CV.WY2017.OG.BL.Geom.Pls.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Psi.RelPerm.Alpha = 0.66
20210521_CV.WY2017.OG.BL.Geom.Psi.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Psil.RelPerm.Alpha = 0.51
20210521_CV.WY2017.OG.BL.Geom.Psil.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Psicl.RelPerm.Alpha = 0.84
20210521_CV.WY2017.OG.BL.Geom.Psicl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Pl.RelPerm.Alpha = 1.11
20210521_CV.WY2017.OG.BL.Geom.Pl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Psl.RelPerm.Alpha = 2.67
20210521_CV.WY2017.OG.BL.Geom.Psl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Pcl.RelPerm.Alpha = 1.58
20210521_CV.WY2017.OG.BL.Geom.Pcl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Pscl.RelPerm.Alpha = 2.11
20210521_CV.WY2017.OG.BL.Geom.Pscl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Psic.RelPerm.Alpha = 1.62
20210521_CV.WY2017.OG.BL.Geom.Psic.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Pc.RelPerm.Alpha = 1.5
20210521_CV.WY2017.OG.BL.Geom.Pc.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Po.RelPerm.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Po.RelPerm.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.SR.RelPerm.Alpha = 0.51
20210521_CV.WY2017.OG.BL.Geom.SR.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Ss.RelPerm.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Ss.RelPerm.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.Sls.RelPerm.Alpha = 3.48
20210521_CV.WY2017.OG.BL.Geom.Sls.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Ssi.RelPerm.Alpha = 0.66
20210521_CV.WY2017.OG.BL.Geom.Ssi.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Ssil.RelPerm.Alpha = 0.51
20210521_CV.WY2017.OG.BL.Geom.Ssil.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Ssicl.RelPerm.Alpha = 0.84
20210521_CV.WY2017.OG.BL.Geom.Ssicl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Sl.RelPerm.Alpha = 1.11
20210521_CV.WY2017.OG.BL.Geom.Sl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.VR.RelPerm.Alpha = 0.51
20210521_CV.WY2017.OG.BL.Geom.VR.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vs.RelPerm.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Vs.RelPerm.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.Vls.RelPerm.Alpha = 3.48
20210521_CV.WY2017.OG.BL.Geom.Vls.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vsi.RelPerm.Alpha = 0.66
20210521_CV.WY2017.OG.BL.Geom.Vsi.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vsil.RelPerm.Alpha = 0.51
20210521_CV.WY2017.OG.BL.Geom.Vsil.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vsicl.RelPerm.Alpha = 0.84
20210521_CV.WY2017.OG.BL.Geom.Vsicl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vl.RelPerm.Alpha = 1.11
20210521_CV.WY2017.OG.BL.Geom.Vl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vsl.RelPerm.Alpha = 2.67
20210521_CV.WY2017.OG.BL.Geom.Vsl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vcl.RelPerm.Alpha = 1.58
20210521_CV.WY2017.OG.BL.Geom.Vcl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vscl.RelPerm.Alpha = 2.11
20210521_CV.WY2017.OG.BL.Geom.Vscl.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vsic.RelPerm.Alpha = 1.62
20210521_CV.WY2017.OG.BL.Geom.Vsic.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vc.RelPerm.Alpha = 1.5
20210521_CV.WY2017.OG.BL.Geom.Vc.RelPerm.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vo.RelPerm.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Vo.RelPerm.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.MV.RelPerm.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.MV.RelPerm.N = 3.180

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

20210521_CV.WY2017.OG.BL.Phase.Saturation.Type = 'VanGenuchten'
20210521_CV.WY2017.OG.BL.Phase.Saturation.GeomNames = 'BR Bs Bls Bsi Bsil Bsicl Bl Bsl Bcl Bscl Bsic Bc Bo PR Ps Pls Psi Psil Psicl Pl Psl Pcl Pscl Psic Pc Po SR Ss Sls Ssi Ssil Ssicl Sl VR Vs Vls Vsi Vsil Vsicl Vl Vsl Vcl Vscl Vsic Vc Vo MV'

20210521_CV.WY2017.OG.BL.Geom.BR.Saturation.Alpha = 3.8
20210521_CV.WY2017.OG.BL.Geom.BR.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.BR.Saturation.SRes = 0.20 ;#0.889 <-- changed this value for run 03B on 2016.06.12
20210521_CV.WY2017.OG.BL.Geom.BR.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Bs.Saturation.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Bs.Saturation.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.Bs.Saturation.SRes = 0.140
20210521_CV.WY2017.OG.BL.Geom.Bs.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Bls.Saturation.Alpha = 3.48
20210521_CV.WY2017.OG.BL.Geom.Bls.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bls.Saturation.SRes = 0.130
20210521_CV.WY2017.OG.BL.Geom.Bls.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Bsi.Saturation.Alpha = 0.66
20210521_CV.WY2017.OG.BL.Geom.Bsi.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bsi.Saturation.SRes = 0.100
20210521_CV.WY2017.OG.BL.Geom.Bsi.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Bsil.Saturation.Alpha = 0.51
20210521_CV.WY2017.OG.BL.Geom.Bsil.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bsil.Saturation.SRes = 0.150
20210521_CV.WY2017.OG.BL.Geom.Bsil.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Bsicl.Saturation.Alpha = 0.84
20210521_CV.WY2017.OG.BL.Geom.Bsicl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bsicl.Saturation.SRes = 0.190
20210521_CV.WY2017.OG.BL.Geom.Bsicl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Bl.Saturation.Alpha = 1.11
20210521_CV.WY2017.OG.BL.Geom.Bl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bl.Saturation.SRes = 0.150
20210521_CV.WY2017.OG.BL.Geom.Bl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Bsl.Saturation.Alpha = 2.67
20210521_CV.WY2017.OG.BL.Geom.Bsl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bsl.Saturation.SRes = 0.100
20210521_CV.WY2017.OG.BL.Geom.Bsl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Bcl.Saturation.Alpha = 1.58
20210521_CV.WY2017.OG.BL.Geom.Bcl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bcl.Saturation.SRes = 0.180
20210521_CV.WY2017.OG.BL.Geom.Bcl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Bscl.Saturation.Alpha = 2.11
20210521_CV.WY2017.OG.BL.Geom.Bscl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bscl.Saturation.SRes = 0.160
20210521_CV.WY2017.OG.BL.Geom.Bscl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Bsic.Saturation.Alpha = 1.62
20210521_CV.WY2017.OG.BL.Geom.Bsic.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bsic.Saturation.SRes = 0.230
20210521_CV.WY2017.OG.BL.Geom.Bsic.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Bc.Saturation.Alpha = 1.5
20210521_CV.WY2017.OG.BL.Geom.Bc.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Bc.Saturation.SRes = 0.210
20210521_CV.WY2017.OG.BL.Geom.Bc.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Bo.Saturation.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Bo.Saturation.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.Bo.Saturation.SRes = 0.140
20210521_CV.WY2017.OG.BL.Geom.Bo.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.PR.Saturation.Alpha = 3.8
20210521_CV.WY2017.OG.BL.Geom.PR.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.PR.Saturation.SRes = 0.889
20210521_CV.WY2017.OG.BL.Geom.PR.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Ps.Saturation.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Ps.Saturation.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.Ps.Saturation.SRes = 0.140
20210521_CV.WY2017.OG.BL.Geom.Ps.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Pls.Saturation.Alpha = 3.48
20210521_CV.WY2017.OG.BL.Geom.Pls.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Pls.Saturation.SRes = 0.130
20210521_CV.WY2017.OG.BL.Geom.Pls.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Psi.Saturation.Alpha = 0.66
20210521_CV.WY2017.OG.BL.Geom.Psi.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Psi.Saturation.SRes = 0.100
20210521_CV.WY2017.OG.BL.Geom.Psi.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Psil.Saturation.Alpha = 0.51
20210521_CV.WY2017.OG.BL.Geom.Psil.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Psil.Saturation.SRes = 0.150
20210521_CV.WY2017.OG.BL.Geom.Psil.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Psicl.Saturation.Alpha = 0.84
20210521_CV.WY2017.OG.BL.Geom.Psicl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Psicl.Saturation.SRes = 0.190
20210521_CV.WY2017.OG.BL.Geom.Psicl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Pl.Saturation.Alpha = 1.11
20210521_CV.WY2017.OG.BL.Geom.Pl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Pl.Saturation.SRes = 0.150
20210521_CV.WY2017.OG.BL.Geom.Pl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Psl.Saturation.Alpha = 2.67
20210521_CV.WY2017.OG.BL.Geom.Psl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Psl.Saturation.SRes = 0.100
20210521_CV.WY2017.OG.BL.Geom.Psl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Pcl.Saturation.Alpha = 1.58
20210521_CV.WY2017.OG.BL.Geom.Pcl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Pcl.Saturation.SRes = 0.180
20210521_CV.WY2017.OG.BL.Geom.Pcl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Pscl.Saturation.Alpha = 2.11
20210521_CV.WY2017.OG.BL.Geom.Pscl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Pscl.Saturation.SRes = 0.160
20210521_CV.WY2017.OG.BL.Geom.Pscl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Psic.Saturation.Alpha = 1.62
20210521_CV.WY2017.OG.BL.Geom.Psic.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Psic.Saturation.SRes = 0.230
20210521_CV.WY2017.OG.BL.Geom.Psic.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Pc.Saturation.Alpha = 1.5
20210521_CV.WY2017.OG.BL.Geom.Pc.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Pc.Saturation.SRes = 0.210
20210521_CV.WY2017.OG.BL.Geom.Pc.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Po.Saturation.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Po.Saturation.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.Po.Saturation.SRes = 0.140
20210521_CV.WY2017.OG.BL.Geom.Po.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.SR.Saturation.Alpha = 0.510
20210521_CV.WY2017.OG.BL.Geom.SR.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.SR.Saturation.SRes = 0.150
20210521_CV.WY2017.OG.BL.Geom.SR.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Ss.Saturation.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Ss.Saturation.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.Ss.Saturation.SRes = 0.140
20210521_CV.WY2017.OG.BL.Geom.Ss.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Sls.Saturation.Alpha = 3.48
20210521_CV.WY2017.OG.BL.Geom.Sls.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Sls.Saturation.SRes = 0.130
20210521_CV.WY2017.OG.BL.Geom.Sls.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Ssi.Saturation.Alpha = 0.66
20210521_CV.WY2017.OG.BL.Geom.Ssi.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Ssi.Saturation.SRes = 0.100
20210521_CV.WY2017.OG.BL.Geom.Ssi.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Ssil.Saturation.Alpha = 0.51
20210521_CV.WY2017.OG.BL.Geom.Ssil.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Ssil.Saturation.SRes = 0.150
20210521_CV.WY2017.OG.BL.Geom.Ssil.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Ssicl.Saturation.Alpha = 0.84
20210521_CV.WY2017.OG.BL.Geom.Ssicl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Ssicl.Saturation.SRes = 0.190
20210521_CV.WY2017.OG.BL.Geom.Ssicl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Sl.Saturation.Alpha = 1.11
20210521_CV.WY2017.OG.BL.Geom.Sl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Sl.Saturation.SRes = 0.150
20210521_CV.WY2017.OG.BL.Geom.Sl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.VR.Saturation.Alpha = 0.510
20210521_CV.WY2017.OG.BL.Geom.VR.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.VR.Saturation.SRes = 0.150
20210521_CV.WY2017.OG.BL.Geom.VR.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Vs.Saturation.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Vs.Saturation.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.Vs.Saturation.SRes = 0.140
20210521_CV.WY2017.OG.BL.Geom.Vs.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Vls.Saturation.Alpha = 3.48
20210521_CV.WY2017.OG.BL.Geom.Vls.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vls.Saturation.SRes = 0.130
20210521_CV.WY2017.OG.BL.Geom.Vls.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Vsi.Saturation.Alpha = 0.66
20210521_CV.WY2017.OG.BL.Geom.Vsi.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vsi.Saturation.SRes = 0.100
20210521_CV.WY2017.OG.BL.Geom.Vsi.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Vsil.Saturation.Alpha = 0.51
20210521_CV.WY2017.OG.BL.Geom.Vsil.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vsil.Saturation.SRes = 0.150
20210521_CV.WY2017.OG.BL.Geom.Vsil.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Vsicl.Saturation.Alpha = 0.84
20210521_CV.WY2017.OG.BL.Geom.Vsicl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vsicl.Saturation.SRes = 0.190
20210521_CV.WY2017.OG.BL.Geom.Vsicl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Vl.Saturation.Alpha = 1.11
20210521_CV.WY2017.OG.BL.Geom.Vl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vl.Saturation.SRes = 0.150
20210521_CV.WY2017.OG.BL.Geom.Vl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Vsl.Saturation.Alpha = 2.67
20210521_CV.WY2017.OG.BL.Geom.Vsl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vsl.Saturation.SRes = 0.100
20210521_CV.WY2017.OG.BL.Geom.Vsl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Vcl.Saturation.Alpha = 1.58
20210521_CV.WY2017.OG.BL.Geom.Vcl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vcl.Saturation.SRes = 0.180
20210521_CV.WY2017.OG.BL.Geom.Vcl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Vscl.Saturation.Alpha = 2.11
20210521_CV.WY2017.OG.BL.Geom.Vscl.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vscl.Saturation.SRes = 0.160
20210521_CV.WY2017.OG.BL.Geom.Vscl.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Vsic.Saturation.Alpha = 1.62
20210521_CV.WY2017.OG.BL.Geom.Vsic.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vsic.Saturation.SRes = 0.230
20210521_CV.WY2017.OG.BL.Geom.Vsic.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Vc.Saturation.Alpha = 1.5
20210521_CV.WY2017.OG.BL.Geom.Vc.Saturation.N = 2.000
20210521_CV.WY2017.OG.BL.Geom.Vc.Saturation.SRes = 0.210
20210521_CV.WY2017.OG.BL.Geom.Vc.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.Vo.Saturation.Alpha = 3.52
20210521_CV.WY2017.OG.BL.Geom.Vo.Saturation.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.Vo.Saturation.SRes = 0.140
20210521_CV.WY2017.OG.BL.Geom.Vo.Saturation.SSat = 1.000
20210521_CV.WY2017.OG.BL.Geom.MV.Saturation.Alpha = 3.520
20210521_CV.WY2017.OG.BL.Geom.MV.Saturation.N = 3.180
20210521_CV.WY2017.OG.BL.Geom.MV.Saturation.SRes = 0.140
20210521_CV.WY2017.OG.BL.Geom.MV.Saturation.SSat = 1.00


#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.Cycle.Names = 'constant'
20210521_CV.WY2017.OG.BL.Cycle.constant.Names = 'alltime'
20210521_CV.WY2017.OG.BL.Cycle.constant.alltime.Length = 10000000
20210521_CV.WY2017.OG.BL.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.BCPressure.PatchNames = [pfget Geom.domain.Patches]

20210521_CV.WY2017.OG.BL.Patch.x_lower.BCPressure.Type = 'FluxConst'
20210521_CV.WY2017.OG.BL.Patch.x_lower.BCPressure.Cycle = 'constant'
20210521_CV.WY2017.OG.BL.Patch.x_lower.BCPressure.alltime.Value = 0.0

20210521_CV.WY2017.OG.BL.Patch.y_lower.BCPressure.Type = 'FluxConst'
20210521_CV.WY2017.OG.BL.Patch.y_lower.BCPressure.Cycle = 'constant'
20210521_CV.WY2017.OG.BL.Patch.y_lower.BCPressure.alltime.Value = 0.0

20210521_CV.WY2017.OG.BL.Patch.z_lower.BCPressure.Type = 'FluxConst'
20210521_CV.WY2017.OG.BL.Patch.z_lower.BCPressure.Cycle = 'constant'
20210521_CV.WY2017.OG.BL.Patch.z_lower.BCPressure.alltime.Value = 0.0

20210521_CV.WY2017.OG.BL.Patch.x_upper.BCPressure.Type = 'FluxConst'
20210521_CV.WY2017.OG.BL.Patch.x_upper.BCPressure.Cycle = 'constant'
20210521_CV.WY2017.OG.BL.Patch.x_upper.BCPressure.alltime.Value = 0.0

20210521_CV.WY2017.OG.BL.Patch.y_upper.BCPressure.Type = 'FluxConst'
20210521_CV.WY2017.OG.BL.Patch.y_upper.BCPressure.Cycle = 'constant'
20210521_CV.WY2017.OG.BL.Patch.y_upper.BCPressure.alltime.Value = 0.0

20210521_CV.WY2017.OG.BL.Patch.z_upper.BCPressure.Type = 'OverlandFlow'
20210521_CV.WY2017.OG.BL.Patch.z_upper.BCPressure.Cycle = 'constant'
20210521_CV.WY2017.OG.BL.Patch.z_upper.BCPressure.alltime.Value = 0.00000

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

20210521_CV.WY2017.OG.BL.TopoSlopesY.Type = 'PFBFile'
20210521_CV.WY2017.OG.BL.TopoSlopesY.GeomNames = 'domain'
20210521_CV.WY2017.OG.BL.TopoSlopesY.FileName = 'slope_y_Rev032415.pfb'

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

20210521_CV.WY2017.OG.BL.TopoSlopesX.Type = 'PFBFile'
20210521_CV.WY2017.OG.BL.TopoSlopesX.GeomNames = 'domain'
20210521_CV.WY2017.OG.BL.TopoSlopesX.FileName = 'slope_x_Rev032415.pfb'


#---------------------------------------------------------
# Mannings coefficient 
#---------------------------------------------------------

20210521_CV.WY2017.OG.BL.Mannings.Type = 'PFBFile'
20210521_CV.WY2017.OG.BL.Mannings.GeomNames = 'domain'
20210521_CV.WY2017.OG.BL.Mannings.FileName = 'CV_1km_ManN.pfb'

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.PhaseSources.water.Type = 'Constant'
20210521_CV.WY2017.OG.BL.PhaseSources.water.GeomNames = 'domain'
20210521_CV.WY2017.OG.BL.PhaseSources.water.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.KnownSolution = 'NoKnownSolution'

#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

20210521_CV.WY2017.OG.BL.Solver = 'Richards'
20210521_CV.WY2017.OG.BL.Solver.MaxIter = 2500000

20210521_CV.WY2017.OG.BL.Solver.TerrainFollowingGrid = True

20210521_CV.WY2017.OG.BL.Solver.Nonlinear.MaxIter = 400
20210521_CV.WY2017.OG.BL.Solver.Nonlinear.ResidualTol = 1e-5
20210521_CV.WY2017.OG.BL.Solver.Nonlinear.EtaValue = 0.0001

20210521_CV.WY2017.OG.BL.Solver.PrintSubsurf = True
20210521_CV.WY2017.OG.BL. = 'Solver.Drop 1E_20'
20210521_CV.WY2017.OG.BL.Solver.AbsTol = 1E-10
20210521_CV.WY2017.OG.BL.Solver.MaxConvergenceFailures = 7

20210521_CV.WY2017.OG.BL.Solver.Nonlinear.UseJacobian = True
20210521_CV.WY2017.OG.BL.Solver.Nonlinear.DerivativeEpsilon = 1e-16
20210521_CV.WY2017.OG.BL.Solver.Nonlinear.StepTol = 1e-20
20210521_CV.WY2017.OG.BL.Solver.Nonlinear.Globalization = 'LineSearch'
20210521_CV.WY2017.OG.BL.Solver.Linear.KrylovDimension = 250
20210521_CV.WY2017.OG.BL.Solver.Linear.MaxRestarts = 5

20210521_CV.WY2017.OG.BL.Solver.Linear.Preconditioner = 'PFMG'
20210521_CV.WY2017.OG.BL.Solver.Linear.Preconditioner.PCMatrixType = 'FullJacobian'

20210521_CV.WY2017.OG.BL.Solver.WriteSiloSubsurfData = False
20210521_CV.WY2017.OG.BL.Solver.WriteSiloPressure = False
20210521_CV.WY2017.OG.BL.Solver.WriteSiloSaturation = False
20210521_CV.WY2017.OG.BL.Solver.WriteSiloConcentration = False
20210521_CV.WY2017.OG.BL.Solver.WriteSiloSlopes = False
20210521_CV.WY2017.OG.BL.Solver.WriteSiloMask = False

20210521_CV.WY2017.OG.BL.Solver.PrintSubsurfData = True
20210521_CV.WY2017.OG.BL.Solver.PrintSpecificStorage = True
20210521_CV.WY2017.OG.BL.Solver.PrintMask = True
20210521_CV.WY2017.OG.BL.Solver.PrintPressure = True
20210521_CV.WY2017.OG.BL.Solver.PrintSaturation = True
20210521_CV.WY2017.OG.BL.Solver.PrintPorosity = True
20210521_CV.WY2017.OG.BL.Solver.PrintSlopes = True

#---------------------------------------------------------
# CLM Solver Section:
#---------------------------------------------------------

20210521_CV.WY2017.OG.BL.Solver.LSM = 'CLM'
20210521_CV.WY2017.OG.BL.Solver.CLM.Print1dOut = False
20210521_CV.WY2017.OG.BL.Solver.BinaryOutDir = False
20210521_CV.WY2017.OG.BL.Solver.CLM.CLMDumpInterval = 1

#Evap and veg stress functions/parameters
20210521_CV.WY2017.OG.BL.Solver.CLM.EvapBeta = 'Linear'
20210521_CV.WY2017.OG.BL.Solver.CLM.VegWaterStress = 'Saturation'
20210521_CV.WY2017.OG.BL.Solver.CLM.ResSat = 0.25
20210521_CV.WY2017.OG.BL.Solver.CLM.WiltingPoint = 0.25
20210521_CV.WY2017.OG.BL.Solver.CLM.FieldCapacity = 1.0

#Met forcing and timestep setup
20210521_CV.WY2017.OG.BL.Solver.CLM.MetForcing = 3D
20210521_CV.WY2017.OG.BL.Solver.CLM.MetFileName = 'NLDAS'
20210521_CV.WY2017.OG.BL.Solver.CLM.MetFilePath = '/glade/scratch/lmthatch/SJBM_Scaling/00_Input/01_NLDAS/1km/WY2017_OG'
20210521_CV.WY2017.OG.BL.Solver.CLM.MetFileNT = 240
20210521_CV.WY2017.OG.BL.Solver.CLM.IstepStart = istep

#Irrigation setup
20210521_CV.WY2017.OG.BL.Solver.CLM.IrrigationType = 'none'
20210521_CV.WY2017.OG.BL.Solver.PrintPressure = True
20210521_CV.WY2017.OG.BL.Solver.PrintSaturation = True
20210521_CV.WY2017.OG.BL.Solver.WriteCLMBinary = False
20210521_CV.WY2017.OG.BL.Solver.WriteSiloCLM = False
20210521_CV.WY2017.OG.BL.Solver.PrintCLM = True

20210521_CV.WY2017.OG.BL.Solver.CLM.ReuseCount = 1
20210521_CV.WY2017.OG.BL.Solver.CLM.WriteLogs = False
20210521_CV.WY2017.OG.BL.Solver.CLM.WriteLastRST = True
20210521_CV.WY2017.OG.BL.Solver.CLM.DailyRST = True
20210521_CV.WY2017.OG.BL.Solver.CLM.SingleFile = True

20210521_CV.WY2017.OG.BL.Solver.CLM.RootZoneNZ = 4
20210521_CV.WY2017.OG.BL.Solver.CLM.SoiLayer = 4


#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

20210521_CV.WY2017.OG.BL.Geom.domain.ICPressure.RefGeom = 'domain'
20210521_CV.WY2017.OG.BL.Geom.domain.ICPressure.RefPatch = 'z_lower'

20210521_CV.WY2017.OG.BL.ICPressure.Type = 'PFBFile'
20210521_CV.WY2017.OG.BL.ICPressure.GeomNames = 'domain'
20210521_CV.WY2017.OG.BL.Geom.domain.ICPressure.FileName = 'pfinit.pfb ;# $fname_ic'
# pfdist pfinit.pfb

#---------
##  Distribute slopes
#---------

20210521_CV.WY2017.OG.BL.ComputationalGrid.NZ = 1

# pfdist slope_y_Rev032415.pfb
# pfdist slope_x_Rev032415.pfb
# pfdist CV_1km_ManN.pfb

20210521_CV.WY2017.OG.BL.ComputationalGrid.NZ = 5

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------
# pfwritedb $runname
#pfrun $runname
#pfundist $runname
20210521_CV.WY2017.OG.BL.run()
