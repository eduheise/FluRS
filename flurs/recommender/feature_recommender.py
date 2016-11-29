from flurs.recommender import recommender

from abc import ABCMeta, abstractmethod


class FeatureRecommender(recommender.Recommender):

    """Base class for experimentation of the incremental models with positive-only feedback.

    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_user(self, u, feature):
        """For new users, append their information into the dictionaries.

        Args:
            u (int): User index.
            feature (numpy 1d array): Feature vector for user.

        """
        self.users[u] = {'observed': set(), 'feature': feature}
        self.n_user += 1

    @abstractmethod
    def add_item(self, i, feature):
        """For new items, append their information into the dictionaries.

        Args:
            i (int): Item index.
            feature (numpy 1d array): Feature vector for item.

        """
        self.items[i] = {'feature': feature}
        self.n_item += 1

    @abstractmethod
    def update(self, u, i, r, context, is_batch_train):
        """Update model parameters based on d, a sample represented as a dictionary.

        Args:
            u (int): User index.
            i (int): Item index.
            r (float): Observed true value.
            context (numpy 1d array): Feature vector representing contextual information.

        """
        pass

    @abstractmethod
    def recommend(self, u, target_i_indices, context):
        """Recommend items for a user represented as a dictionary d.

        First, scores are computed.
        Next, `self.__scores2recos()` is called to convert the scores into a recommendation list.

        Args:
            u (int): Target user index.
            target_i_indices (numpy array; (# target items, )): Target items' indices. Only these items are considered as the recommendation candidates.
            context (numpy 1d array): Feature vector representing contextual information.

        Returns:
            (numpy array, numpy array) : (Sorted list of items, Sorted scores).

        """
        return