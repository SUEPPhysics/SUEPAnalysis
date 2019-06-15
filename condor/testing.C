/*Macro for plotting MonoZ NTuples (Testing Systematics)
 Written by Chad Freer 
 Jun 11, 2019
 Input tree froom MonoZ NTupilizer 
 */

#include "TFile.h"
#include "TSystem.h"
#include "TChain.h"
#include "TTree.h"
#include "TBranch.h"
#include "TStyle.h"
#include "TMath.h"

const int MAX_FILES = 10;   // Max number of files to process
const int MAX_EVT   = 100000;   // Max number of events to process
const int PRT_EVT   =  100;   // Print every N events
const bool verbose  = false; // Print information about the event and RECO and L1T muons

//for making plots
static TString xaxis="p_{T}^{miss} [GeV]";
static TString yaxis="Entries";

//Change the file name here
TFile *fout = new TFile("systematics_testing.root","RECREATE");

Float_t MET_axis[] = {0,50,100,125,150,175,200,250,300,350,400,500,600};

TH1F *MET_NOM = new TH1F ("MET_NOM",xaxis,12,MET_axis);
TH1F *MET_UP = new TH1F ("MET_NOM",xaxis,12,MET_axis);
TH1F *MET_DOWN = new TH1F ("MET_NOM",xaxis,12,MET_axis);

Float_t MET_pt_nom;
Float_t MET_pt_jerUp;
Float_t MET_pt_jerDown;
Float_t Up;
Float_t Down;
//TString UP_Variation = "MET_pt_jerUp";
//TString DOWN_Variation = "MET_pt_jerUp";

void testing(){
   gROOT->SetStyle("Plain");
   //Open and read file
   TFile *f = new TFile("D6F99CDC-D6A4-E811-A6E9-0CC47A166D66_Skim.root","READ");
   TTree *tree= (TTree*)f->Get("Events");

   TCanvas *cc = new TCanvas("cc", "cc", 600, 800);
   TPad *p1 = new TPad("p1", "p1", 0, 0.25, 1, 1);
   p1->SetBottomMargin(0.9);//Add for ratio plot 
   p1->Draw();
   p1->cd();
   //prepare event loop
   std::cout << "\n******* About to loop over the events *******" << std::endl;
   int nEvents = tree->GetEntries();
   tree->SetBranchAddress("MET_pt_nom", &MET_pt_nom);
   //tree->SetBranchAddress("MET_pt_jerUp", &MET_pt_jerUp);
   //tree->SetBranchAddress("MET_pt_jerDown", &MET_pt_jerDown);
   tree->SetBranchAddress("MET_pt_jerUp", &Up);
   tree->SetBranchAddress("MET_pt_jerDown", &Down);

   for (int iEvt = 0; iEvt < nEvents; iEvt++) {
     if (iEvt > MAX_EVT) break;
     if ( (iEvt % PRT_EVT) == 0 ) {
        std::cout << "\n*************************************" << std::endl;
        std::cout << "Looking at event " << iEvt << " out of " << nEvents << std::endl;
        std::cout << "*************************************" << std::endl;    
     }//end conditional
     tree->GetEntry(iEvt);
     //std::cout << MET_pt_nom << std::endl;
     MET_NOM->Fill(MET_pt_nom,1);
     //MET_UP->Fill(MET_pt_jerUp,1);
     //MET_DOWN->Fill(MET_pt_jerDown,1);
     MET_UP->Fill(Up,1);
     MET_DOWN->Fill(Down,1);
   }//end event loop
   //Might as well label things
   MET_NOM->SetLineColor(kBlack);
   MET_NOM->Draw();
   MET_NOM->GetXaxis()->SetTitle(xaxis);
   MET_NOM->GetYaxis()->SetTitle(yaxis);
   MET_UP->SetLineColor(kRed);
   MET_UP->Draw("same");
   MET_UP->GetXaxis()->SetTitle(xaxis);
   MET_UP->GetYaxis()->SetTitle(yaxis);
   MET_DOWN->SetLineColor(kBlue);
   MET_DOWN->Draw("same");
   MET_DOWN->GetXaxis()->SetTitle(xaxis);
   MET_DOWN->GetYaxis()->SetTitle(yaxis);	
   //Add a beautiful legend
   TLegend* leg  = new TLegend(.67,.67,.87,.87);
   leg->AddEntry(MET_NOM, "Nominal","F");
   leg->AddEntry(MET_UP, "MET_pt_jerUp","F");
   leg->AddEntry(MET_DOWN, "MET_pt_jerDown","F");
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   leg->SetLineColor(0);
   leg->SetHeader("");
   leg->Draw("same");
   leg->SetTextFont(42);
   cc->Update();

   cc->cd();
   TPad *p2 = new TPad("p2", "p2", 0, 0.05, 1, 0.25);
   p2->SetTopMargin(0.1);  //Command controls the offset from the top pad (0 cuts off numbers!)
   p2->SetBorderMode(0);
   p2->Draw();
   p2->cd();
   TH1F *MET_UP2 = (TH1F*)MET_UP->Clone("copy");
   TH1F *MET_DOWN2 = (TH1F*)MET_DOWN->Clone("copy");
   //Ratio Parameters
   MET_UP2->Divide(MET_NOM);
   MET_DOWN2->Divide(MET_NOM);
   MET_UP2->GetYaxis()->SetTitle("SYS/NOM");
   MET_UP2->GetYaxis()->SetTitleSize(.12);
   MET_UP2->GetYaxis()->SetTitleOffset(0.35);
   MET_UP2->GetYaxis()->SetLabelSize(0.12);
   MET_UP2->GetXaxis()->SetLabelSize(0.12);
   MET_UP2->GetXaxis()->SetTitleSize(.8);
   MET_UP2->SetMaximum(1.5);
   MET_UP2->SetMinimum(0.5);
   MET_UP2->SetStats(0);
   MET_UP2->SetMarkerColor(kRed);
   MET_UP2->SetMarkerStyle(20);
   MET_UP2->GetYaxis()->SetNdivisions(10);
   MET_UP2->SetTitle("");
   MET_DOWN2->SetMarkerColor(kBlue);
   MET_DOWN2->SetMarkerStyle(20);
   
   //Add a line at 1 for the ratio plot
   TLine *ll = new TLine(1, 1., 37, 1.);
   ll->SetLineWidth(2);
   ll->SetLineStyle(7);
   ll->SetLineColor(kBlack);
   
   //ll->Draw();
   MET_UP2->Draw("P");
   MET_DOWN2->Draw("Psame");
   ll->Draw("same");
   
   //Add gridlines for ratio
   p2->SetGridx();
   p2->SetGridy();
   
   p2->Modified();
   cc->Update();
	
    //Cleaning up after ourselves
    std::cout << "\n******* Finished looping over the events *******" << std::endl;
    delete tree;
    std::cout << "\nDone with Read_FlatNtuple(). Exiting.\n" << std::endl;
    fout->Write();

}//end void

