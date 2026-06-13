import argparse, numpy as np, mne, os
def bicoh(x,fs,f1,f2):
    n=len(x); w=np.hanning(n); X=np.fft.rfft(x*w); f=np.fft.rfftfreq(n,1/fs)
    i1,i2,i3=np.argmin(abs(f-f1)),np.argmin(abs(f-f2)),np.argmin(abs(f-(f1+f2)))
    num=abs(X[i1]*X[i2]*np.conj(X[i3])); den=np.sqrt(abs(X[i1]*X[i2])**2*abs(X[i3])**2)+1e-12
    return num/den
p=argparse.ArgumentParser(); p.add_argument('--edf',required=True); p.add_argument('--f1',type=float,default=15); p.add_argument('--f2',type=float,default=30); p.add_argument('--window',type=float,default=2); a=p.parse_args()
raw=mne.io.read_raw_edf(a.edf,preload=True,verbose=False); raw.pick_types(eeg=True); fs=raw.info['sfreq']; raw.filter(1.,min(a.f1+a.f2+5,fs/2-0.5),verbose=False)
d=raw.get_data()[0]; L=int(a.window*fs); idx=range(0,min(len(d)-L,2000*L),L)
vals=np.array([bicoh(d[i:i+L],fs,a.f1,a.f2) for i in idx]); epochs=np.array([d[i:i+L] for i in idx])
mask=(vals>=0.6)&(vals<=0.7); gap_epochs=epochs[mask]
os.makedirs('real_data',exist_ok=True); np.save('real_data/shangraw_gap_epochs_gaponly.npy', gap_epochs if len(gap_epochs)>0 else epochs[:10])
print(f"Total epochs: {len(vals)}, Gap epochs 0.6-0.7: {mask.sum()}, mean bicoh: {vals.mean():.3f}")
