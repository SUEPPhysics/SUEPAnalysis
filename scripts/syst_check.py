#Macro for plotting MonoZ NTuples (Testing Systematics)
# Written by Chad Freer
# Jun 11, 2019
# Input tree froom MonoZ NTupilizer


#include "TFile.h"
#include "TSystem.h"
#include "TChain.h"
#include "TTree.h"
#include "TBranch.h"
#include "TStyle.h"
#include "TMath.h"
import ROOT
import sys

MAX_FILES = 10   # Max number of files to process
MAX_EVT   = 100000   # Max number of events to process
PRT_EVT   =  100   # Print every N events
#verbose  = false # Print information about the event and RECO and L1T muons

#for making plots
xaxis="p_{T}^{miss} [GeV]"
yaxis="Entries"

#Change the file name here
fout = ROOT.TFile.Open("systematics.root","RECREATE")

MET_axis = [0,50,100,125,150,175,200,250,300,350,400,500,600]

ROOT.gROOT.SetStyle("Plain")
ROOT.gROOT.ForceStyle()

systmatics = ["ElectronEn", "MuonEn", "jesTotal", "jer", "puWeight", "PDF", "MuonSF", "ElecronSF", "EWK", "nvtxWeight","TriggerSFWeight","btagEventWeight", "QCDScale0w", "QCDScale1w", "QCDScale2w"]
process = "Unpart_ZToEEAndMuMu_SU_0_dU_1p01_LU_15_TuneCP5_13TeV_pythia8"
process = "ZZTo2L2Nu_13TeV_powheg_pythia8"

for name in systmatics:
    f =ROOT.TFile.Open("tree_1.root","READ")
    cc = ROOT.TCanvas("cc", "cc", 600, 800)
    p1 = ROOT.TPad("p1", "p1", 0, 0.25, 1, 1)
    p1.SetBottomMargin(0.9)#Add for ratio plot
    p1.Draw()
    p1.cd()
    #prepare event loop

    MET_NOM = f.Get("measMET_"+process+"_catSignal-0jet")
    if not MET_NOM :
        print " Failed to get data histogram "
        sys.exit (1)
    MET_NOM.SetDirectory(0)
    MET_UP = f.Get("measMET_"+process+"_catSignal-0jet_sys_" + name + "Up")
    MET_UP.SetDirectory(0)
    MET_DOWN = f.Get("measMET_"+process+"_catSignal-0jet_sys_" + name + "Down")
    MET_DOWN.SetDirectory(0)
    MET_NOM.GetXaxis().SetRange(1,11)
    MET_UP.GetXaxis().SetRange(1,11)
    MET_DOWN.GetXaxis().SetRange(1,11)

    #Might as well label things
    MET_NOM.SetLineColor(ROOT.kBlack)
    MET_NOM.Draw()
    MET_NOM.GetXaxis().SetTitle(xaxis)
    MET_NOM.GetYaxis().SetTitle(yaxis)
    MET_UP.SetLineColor(ROOT.kRed)
    MET_UP.Draw("same")
    MET_UP.GetXaxis().SetTitle(xaxis)
    MET_UP.GetYaxis().SetTitle(yaxis)
    MET_DOWN.SetLineColor(ROOT.kBlue)
    MET_DOWN.Draw("same")
    MET_DOWN.GetXaxis().SetTitle(xaxis)
    MET_DOWN.GetYaxis().SetTitle(yaxis)
    #Add a beautiful legend
    leg  = ROOT.TLegend(.67,.67,.87,.87)
    leg.AddEntry(MET_NOM, "Nominal","F")
    leg.AddEntry(MET_UP, name + "Up","F")
    leg.AddEntry(MET_DOWN, name + "Down","F")
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetLineColor(0)
    leg.SetHeader("")
    leg.Draw("same")
    leg.SetTextFont(42)
    cc.Update()

    cc.cd()
    p2 = ROOT.TPad("p2", "p2", 0, 0.05, 1, 0.25)
    p2.SetTopMargin(0.1)  #Command controls the offset from the top pad (0 cuts off numbers!)
    p2.SetBorderMode(0)
    p2.Draw()
    p2.cd()
    MET_UP2 = MET_UP.Clone("copy")
    MET_DOWN2 = MET_DOWN.Clone("copy")
    #Ratio Parameters
    MET_UP2.Divide(MET_NOM)
    MET_DOWN2.Divide(MET_NOM)
    MET_UP2.GetYaxis().SetTitle("SYS/NOM")
    MET_UP2.GetYaxis().SetTitleSize(.12)
    MET_UP2.GetYaxis().SetTitleOffset(0.35)
    MET_UP2.GetYaxis().SetLabelSize(0.12)
    MET_UP2.GetXaxis().SetLabelSize(0.12)
    MET_UP2.GetXaxis().SetTitleSize(.8)
    MET_UP2.SetMaximum(1.5)
    MET_UP2.SetMinimum(0.5)
    MET_UP2.SetStats(0)
    MET_UP2.SetMarkerColor(ROOT.kRed)
    MET_UP2.SetMarkerStyle(20)
    MET_UP2.GetYaxis().SetNdivisions(10)
    MET_UP2.SetTitle("")
    MET_DOWN2.SetMarkerColor(ROOT.kBlue)
    MET_DOWN2.SetMarkerStyle(20)

    #Add a line at 1 for the ratio plot
    ll = ROOT.TLine(50, 1., 600, 1.)
    ll.SetLineWidth(2)
    ll.SetLineStyle(7)
    ll.SetLineColor(ROOT.kBlack)

    #ll.Draw()
    MET_UP2.Draw("hist")
    MET_DOWN2.Draw("hist,same")
    ll.Draw("same")

    #Add gridlines for ratio
    p2.SetGridx()
    p2.SetGridy()

    p2.Modified()
    cc.Update()

    cc.SaveAs(name+"_systematics.png")

