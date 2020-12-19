from func_adl_servicex import ServiceXSourceXAOD

ds = "mc15_13TeV:mc15_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.merge.DAOD_STDM3.e3601_s2576_s2132_r6630_r6264_p2363_tid05630052_00"

f_ds = ServiceXSourceXAOD(ds)

# Simple request

# r = f_ds \
#     .SelectMany('lambda e: e.Jets("AntiKt4EMTopoJets")') \
#     .Select('lambda j: j.pt() / 1000.0') \
#     .AsPandasDF('JetPt') \
#     .value()
# print(r)

# Multi-variable query
# r = f_ds \
#         .Select('lambda e: (e.Electrons("Electrons"), e.Muons("Muons"))') \
#         .Select('lambda ls: (ls[0].Select(lambda e: e.pt()), \
#                              ls[0].Select(lambda e: e.eta()), \
#                              ls[0].Select(lambda e: e.phi()), \
#                              ls[0].Select(lambda e: e.e()), \
#                              ls[1].Select(lambda m: m.pt()), \
#                              ls[1].Select(lambda m: m.eta()), \
#                              ls[1].Select(lambda m: m.phi()), \
#                              ls[1].Select(lambda m: m.e()))') \
#         .AsAwkwardArray(('ElePt', 'EleEta', 'ElePhi', 'EleE', 'MuPt', 'MuEta', 'MuPhi', 'MuE')) \
#         .value()
# print(r)

# Applying a filter
# r = f_ds \
#     .SelectMany('lambda e: e.Jets("AntiKt4EMTopoJets")') \
#     .Where('lambda j: j.pt() / 1000.0 > 30.0') \
#     .Select('lambda j: j.eta()') \
#     .AsPandasDF('JetPt') \
#     .value()
# print(r)

# Complex example
# r = f_ds \
#     .Where('lambda e: e.Jets("AntiKt4EMTopoJets") \
#             .Where(lambda j: j.pt() / 1000.0 > 30.0).Count() >= 1') \
#     .Select('lambda e: e.Electrons("Electrons")') \
#     .Select('lambda e: e.Select(lambda ele: ele.eta() * ele.phi())') \
#     .AsAwkwardArray('EleMyVar') \
#     .value()
# print(r)

