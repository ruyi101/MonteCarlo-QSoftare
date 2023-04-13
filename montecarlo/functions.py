"""Provide the primary functions."""



def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format).

    Replace this function and doc string for your own project.

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from.

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution.
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote









    

def metropolis_montecarlo(ham, conf, T=1, nsweep=8000, nburn=2000):
    conf = ham.mc_step(conf, T, nburn)
    E = np.zeros(nsweep)
    M = np.zeros(nsweep)
    E_sq = np.zeros(nsweep)
    M_sq = np.zeros(nsweep)
    for step in range(nsweep):
        conf = ham.mc_step(conf, T)
        
        Ei = ham.energy(conf)

        E[step] = (E[step - 1] * step + Ei)/(step+1)
        
        E_sq[step] = (E_sq[step - 1] * step + (Ei)**2)/(step+1)
        
        Mi = np.sum(2*np.array(conf.config) - 1) 
        
        M[step] = (M[step - 1] * step + Mi)/(step+1)
        
        M_sq[step] = (M_sq[step - 1] * step + Mi**2)/(step+1)
        
    return E, M, E_sq, M_sq






if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
