import numpy as np
import matplotlib.pyplot as plt

class PointMatcher:
    def __init__(self, points_a, points_b, eps=0.0):
        """
        Initialize the PointMatcher with two sets of 2D points.
        
        :param points_a: List or array of (x, y) tuples – the main point set.
        :param points_b: List or array of (x, y) tuples – the pattern to match.
        :param eps: Tolerance for fuzzy matching (default = 0.0 for exact match).
        """
        self.points_a = np.array(points_a)
        self.points_b = np.array(points_b)
        self.eps = eps

    def exact_match(self):
        """
        Check if all points in B exist exactly in A.
        
        :return: True if exact match found, else False.
        """
        a_set = set(map(tuple, self.points_a))
        return all(tuple(point) in a_set for point in self.points_b)

    def fuzzy_match(self):
        """
        Check if all points in B are close enough to any point in A within epsilon.
        
        :return: True if fuzzy match found, else False.
        """
        def is_close(p1):
            return any(np.linalg.norm(p1 - pa) <= self.eps for pa in self.points_a)

        return all(is_close(pb) for pb in self.points_b)

    def plot(self, show_connections=True):
        """
        Visualize point sets A and B, with optional connections for fuzzy/exact matches.
        """
        a = self.points_a
        b = self.points_b

        plt.figure(figsize=(6, 6))
        plt.scatter(a[:, 0], a[:, 1], color='gray', label='A (main set)', s=50)
        plt.scatter(b[:, 0], b[:, 1], color='red', marker='*', label='B (pattern)', s=150)

        if show_connections:
            # Fuzzy match mode
            if self.eps > 0:
                matched_pairs = []
                for bp in b:
                    distances = np.linalg.norm(a - bp, axis=1)
                    nearest_idx = np.argmin(distances)
                    if distances[nearest_idx] <= self.eps:
                        nearest = a[nearest_idx]
                        matched_pairs.append((bp, nearest))
                        # draw dashed line to matched A point
                        plt.plot([bp[0], nearest[0]], [bp[1], nearest[1]], 'r--', alpha=0.5)

                # Connect matched points from B in order (like a path)
                if matched_pairs:
                    b_matched_sorted = np.array([bp for bp, _ in matched_pairs])
                    plt.plot(b_matched_sorted[:, 0], b_matched_sorted[:, 1], 'red', linewidth=2, alpha=0.6)

            # Exact match mode
            elif self.eps == 0 and self.exact_match():
                # Connect B points in order
                plt.plot(b[:, 0], b[:, 1], 'green', linewidth=2, label='Exact match path')

        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        plt.title(f'Point Matching Visualization (eps={self.eps})')
        plt.show()