
def temporal_module_degree_zscore(net, communities=None):
    '''
    Temporal version of within module degree centrality. 

    Static participatoin coefficient is:

    $P_i = 1 - sum_s^{N_M}({(k_is)/k_i}^2)$

    Where s is the index of each community (N_M). k_i is total degree of node. And k_is is degree of connections within community.

    This "temporal" version only loops through temporal snapshots.

    Parameters
    ----------
    net : array, dict
        graphlet or contact sequence input. Only positive matrices considered.
    communities : array
        community vector. Either 1D (node) community index or 2D (node,time).

    Note
    ----
    If directed, function sums axis=1, so G may want to be transposed before hand depending on what type of directed part_coef you are interested in.

    Returns
    -------
    Z : array
        module degree zscore.

    Source
    ------
    Guimera et al (2005) Functional cartography of complex metabolic networks. Nature.
    '''

    if not communities:
        if isinstance(net,dict):
            if 'communities' in net.keys():
                communities = net['communities']
            else:
                raise ValueError('Community index not found')
        else:
            raise ValueError('Community must be provided for graphlet input')

    # Get input in right format
    net, netinfo = utils.process_input(net, ['C', 'G', 'TO'])

    if np.sum(net<0) > 0:
        raise ValueError('Negative connections found')

    k_is = np.zeros(netinfo['netshape'][0],netinfo['netshape'][2])
    part = np.ones(netinfo['netshape'][0],netinfo['netshape'][2])

    for t in netinfo['shape'][2]
        if len(communities.shape)==2:
            C = np.unique(communities[:,t])
        else:
            C = np.unique(communities)
            for i in :
                k_is[:,t] += np.square(np.sum(G[communities == i,:,t], axis=1))

    part = part - (k_is / np.square(np.sum(net, axis=1)))
    # Set any division by 0 to 0
    part[np.isnan(part)==1] = 0

    return part
