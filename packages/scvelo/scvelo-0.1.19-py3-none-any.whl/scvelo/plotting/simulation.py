from ..tools.dynamical_model_utils import unspliced, mRNA, vectorize, tau_inv
from .utils import make_dense

import numpy as np
import matplotlib.pyplot as pl
from matplotlib import rcParams


def get_dynamics(adata, key='fit', extrapolate=False, sorted=False, t=None):
    alpha, beta, gamma, t_, scaling = get_vars(adata, key)
    if extrapolate:
        u0_ = unspliced(t_, 0, alpha, beta)
        tmax = t_ + tau_inv(u0_ * 1e-4, u0=u0_, alpha=0, beta=beta)
        t = np.concatenate([np.linspace(0, t_, num=500), t_ + np.linspace(0, tmax, num=500)])
    elif t is None or t is True:
        t = adata.obs[key + '_t'].values if key is 'true' else adata.layers[key + '_t']

    tau, alpha, u0, s0 = vectorize(np.sort(t) if sorted else t, t_, alpha, beta, gamma)
    ut, st = mRNA(tau, u0, s0, alpha, beta, gamma)

    return alpha, ut, st


def compute_dynamics(adata, basis, key='true', extrapolate=None, sort=True, t_=None, t=None):
    idx = np.where(adata.var_names == basis)[0][0] if isinstance(basis, str) else basis
    key = 'fit' if key + '_gamma' not in adata.var_keys() else key

    alpha = adata.var[key + '_alpha'][idx] if key + '_alpha' in adata.var.keys() else 1
    beta = adata.var[key + '_beta'][idx] if key + '_beta' in adata.var.keys() else 1
    gamma = adata.var[key + '_gamma'][idx]
    t_ = adata.var[key + '_t_'][idx] if t_ is None else t_
    scaling = adata.var[key + '_scaling'][idx] if key + '_scaling' in adata.var.keys() else 1

    if t is None or t is True:
        t = adata.obs[key + '_t'].values if key is 'true' else adata.layers[key + '_t'][:, idx]

    if extrapolate:
        u0_ = unspliced(t_, 0, alpha, beta)
        tmax = np.max(t) if True else tau_inv(u0_ * 1e-4, u0=u0_, alpha=0, beta=beta)
        t = np.concatenate([np.linspace(0, t_, num=500), np.linspace(t_, tmax, num=500)])

    tau, alpha, u0, s0 = vectorize(np.sort(t) if sort else t, t_, alpha, beta, gamma)

    ut, st = mRNA(tau, u0, s0, alpha, beta, gamma)
    ut *= scaling

    vt = ut * beta - st * gamma
    return alpha, ut, st, vt


def show_full_dynamics(adata, basis, key='true', use_raw=False, linewidth=1, show_assigments=None):
    color = 'grey' if key is 'true' else 'purple'
    linewidth = .5 * linewidth if key is 'true' else linewidth

    _, ut, st, _ = compute_dynamics(adata, basis, key, extrapolate=True, t=show_assigments)
    pl.plot(st, ut, color=color, linewidth=linewidth)

    if key is not 'true':
        _, ut, st, _ = compute_dynamics(adata, basis, key, extrapolate=False, sort=False, t=show_assigments)
        pl.scatter(st, ut, color=color, s=1)
        if show_assigments is not None and show_assigments is not False:
            skey, ukey = ('spliced', 'unspliced') if use_raw or 'Ms' not in adata.layers.keys() else ('Ms', 'Mu')
            s, u = make_dense(adata[:, basis].layers[skey]).flatten(), make_dense(adata[:, basis].layers[ukey]).flatten()
            pl.plot(np.array([s, st]), np.array([u, ut]), color='grey', linewidth=.1 * linewidth)

    idx = np.where(adata.var_names == basis)[0][0]
    beta, gamma = adata.var[key + '_beta'][idx], adata.var[key + '_gamma'][idx]
    scaling = adata.var[key + '_scaling'][idx] if key + '_scaling' in adata.var.keys() else 1

    xnew = np.linspace(0, st.max())
    label = 'learned dynamics' if key is 'fit' else 'true dynamics'
    pl.plot(xnew, gamma / beta * scaling * xnew, color=color, linestyle='--', linewidth=linewidth, label=label)
    return label


def simulation(adata, var_names='all', legend_loc='upper right', linewidth=None, dpi=None, **kwargs):
    from ..tools.utils import make_dense
    from .scatter import scatter
    var_names = adata.var_names if var_names is 'all' else [name for name in var_names if name in adata.var_names]

    figsize = rcParams['figure.figsize']
    ncols = len(var_names)
    for i, gs in enumerate(pl.GridSpec(1, ncols, pl.figure(None, (figsize[0] * ncols, figsize[1]), dpi=dpi))):
        idx = np.where(adata.var_names == var_names[i])[0][0]

        alpha, ut, st, _ = compute_dynamics(adata, idx)

        t = adata.obs['true_t'] if 'true_t' in adata.obs.keys() else make_dense(adata.layers['fit_t'][:, idx])
        idx_sorted = np.argsort(t)
        t = t[idx_sorted]

        u = make_dense(adata.layers['unspliced'][:, idx])[idx_sorted]
        s = make_dense(adata.layers['spliced'][:, idx])[idx_sorted]

        ax = pl.subplot(gs)

        _kwargs = {'alpha': .3, 'title': '', 'xlabel': 'time', 'ylabel': 'counts'}
        _kwargs.update(kwargs)

        ax = scatter(x=t, y=u, color='darkblue', ax=ax, show=False, **_kwargs)
        ax = scatter(x=t, y=s, color='red', ax=ax, show=False, **_kwargs)

        linewidth = 1 if linewidth is None else linewidth
        ax.plot(t, alpha, label='alpha', linestyle='--', color='grey', linewidth=linewidth)
        ax.plot(t, ut, label='unspliced', color='darkblue', linewidth=linewidth)
        ax.plot(t, st, label='spliced', color='red', linewidth=linewidth)

        pl.xlim(0)
        pl.ylim(0)
        if legend_loc is not 'none':
            pl.legend(loc=legend_loc)