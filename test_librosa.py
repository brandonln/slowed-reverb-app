import librosa as lb 
import resampy as rs 

f1, sr1 = lb.core.load("stargazing_slowed.wav", sr=None)
print(f1)
print(sr1)


speed = 0.861
factor = 1/(1+(1-0.861))
print(factor)
sr2=int(sr1*factor)

print(sr2)

f2 = lb.core.resample(f1, sr1, sr2)
print(f2)

lb.output.write_wav("stargazing_slowed.wav", f2, sr2)
