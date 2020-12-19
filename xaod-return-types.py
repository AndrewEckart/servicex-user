from func_adl_servicex import ServiceXSourceXAOD

dataset_name = "mc15_13TeV:mc15_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.merge.DAOD_STDM3.e3601_s2576_s2132_r6630_r6264_p2363_tid05630052_00"
src = ServiceXSourceXAOD(dataset_name)\
    .SelectMany('lambda e: e.Jets("AntiKt4EMTopoJets")') \
    .Select('lambda j: j.pt()/1000.0')

return_types = [
    src.AsAwkwardArray('JetPt'),
    src.AsPandasDF('JetPt'),
    # src.AsParquetFiles('pq'),
    # src.AsROOTTTree('JetPt')
]

for r in return_types:
    print(type(r))
