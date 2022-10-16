import numpy
from sklearn.cluster import KMeans


class AlgorithmModel:
    def __init__(self):
        pass

    def create_model(self, n_clusters):
        return KMeans(n_clusters=n_clusters)

    def find_dominant_colors(self, cluster):
        return numpy.array(cluster.cluster_centers_, dtype="uint")

    def find_dominance_percentage(self, cluster, image):
        return (numpy.unique(cluster.labels_, return_counts=True)[1]) / image.shape[0]

    def zipped_dominance_and_percentage(self, cluster, image):
        return sorted(
            zip(
                self.find_dominance_percentage(cluster, image),
                self.find_dominant_colors(cluster),
            ),
            reverse=True,
        )
