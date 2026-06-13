import argparse, numpy as np
from scipy.signal import hilbert
from scipy.stats import percentileofscore
import matplotlib.pyplot as plt

def load_data(path):
    x = np.load(path)
    return x[None, :] if x.ndim == 1 else x

def wigner_proxy(x):
    # no cwt needed - use analytic signal negativity as proxy
    a = hilbert(x - x.mean())
    env = np.abs(a)
    # negativity = fraction below 5th percentile (non-classical dip)
    neg_frac = (env < np.percentile(env, 5)).mean()
    return neg_frac

def squeezed_test(x, n_surrogates=50):
    angles = np.linspace(0, np.pi, 12)
    seps = []
    for a in angles:
        rot = x * np.cos(a) + np.imag(hilbert(x)) * np.sin(a)
        var = rot.var(1).mean()
        surr = [np.random.permutation(rot.ravel()).reshape(rot.shape).var(1).mean() for _ in range(n_surrogates)]
        seps.append(abs(percentileofscore(surr, var)/100 - 0.5))
    return angles[np.argmax(seps)], max(seps), angles, seps

def midcircuit_projection(x):
    t0 = x.shape[1]//2
    ths = np.linspace(x[:,t0].min(), x[:,t0].max(), 9)
    shapes = [x[x[:,t0]>th, t0:].mean(0) for th in ths if (x[:,t0]>th).sum()>2]
    shapes = np.array(shapes)
    pred = 1 - shapes.var(0).mean()/x.var() if len(shapes)>1 else 0
    return pred, shapes

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    args = ap.parse_args()
    X = load_data(args.data)
    print(f"Loaded {X.shape[0]} trials, {X.shape[1]} samples")
    negs = [wigner_proxy(t) for t in X]
    print(f"[Test1 Wigner] mean negativity: {np.mean(negs):.3f} (Oxford >0.15)")
    ba, sep, angs, seps = squeezed_test(X)
    print(f"[Test2 Squeeze] best angle {ba:.2f} rad, separation {sep:.3f} (>0.4 good)")
    pred, shapes = midcircuit_projection(X)
    print(f"[Test3 Projection] predictability {pred:.3f} (>0.3 suggests effect)")
    fig, ax = plt.subplots(3,1,figsize=(8,9))
    ax[0].hist(negs, bins=15); ax[0].set_title("Wigner negativity")
    ax[1].plot(angs, seps, 'o-'); ax[1].set_title("Squeeze vs separation")
    ax[2].imshow(shapes, aspect='auto', cmap='RdBu'); ax[2].set_title("Mid-circuit shapes")
    plt.tight_layout(); plt.savefig("saner_tests.png", dpi=150)
    print("Saved saner_tests.png")
