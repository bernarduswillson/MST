def mst_based_clustering(mst_result, n):
    clusters = []

    for edge in mst_result:
        node1, node2 = edge
        node1_cluster = None
        node2_cluster = None

        for cluster in clusters:
            if node1 in cluster:
                node1_cluster = cluster
            if node2 in cluster:
                node2_cluster = cluster

        if node1_cluster is None and node2_cluster is None:
            clusters.append([node1, node2])
        elif node1_cluster is None:
            node2_cluster.append(node1)
        elif node2_cluster is None:
            node1_cluster.append(node2)
        elif node1_cluster != node2_cluster:
            node1_cluster.extend(node2_cluster)
            clusters.remove(node2_cluster)

        # Check if the desired number of clusters is reached
        if len(clusters) == n:
            break

    return clusters
