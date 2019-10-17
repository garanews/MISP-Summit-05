 def matchVectors(self, vector_a, vector_b):
    # ensure binary representation and apply weights
    if not self._isDecompressed(vector_a):
        vector_a = self.decompress(vector_a)
    vector_a = self._apply_weights(vector_a)
    if not self._isDecompressed(vector_b):
        vector_b = self.decompress(vector_b)
    vector_b = self._apply_weights(vector_b)
    # calculate Jaccard index
    if NUMPY_AVAILABLE:
        maxPQ = np.sum(np.maximum(vector_a, vector_b))
        return np.sum(np.minimum(vector_a, vector_b)) / maxPQ
    intersection_score = 0
    union_score = 0
    jaccard_index = 0
    for offset in range(len(vector_a)):
        intersection_score += vector_a[offset] & vector_b[offset]
        union_score += vector_a[offset] | vector_b[offset]
    if union_score > 0:
        jaccard_index = 1.0 * intersection_score / union_score
    return jaccard_index