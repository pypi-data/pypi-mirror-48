from emmental.metrics.precision import precision_scorer
from emmental.metrics.recall import recall_scorer


def fbeta_scorer(golds, probs, preds, uids=None, pos_label=1, beta=1):
    """F-beta score is the weighted harmonic mean of precision and recall.

    :param golds: Ground truth (correct) target values.
    :type golds: 1-d np.array
    :param probs: Predicted target probabilities. (Not used!)
    :type probs: k-d np.array
    :param preds: Predicted target values.
    :type preds: 1-d np.array
    :param uids: Unique ids.
    :type uids: list
    :param pos_label: The positive class label, defaults to 1
    :param pos_label: int, optional
    :param beta: Weight of precision in harmonic mean, defaults to 1
    :param beta: float, optional
    :return: F-beta score.
    :rtype: dict
    """

    precision = precision_scorer(golds, probs, preds, uids, pos_label)["precision"]
    recall = recall_scorer(golds, probs, preds, uids, pos_label)["recall"]

    fbeta = (
        (1 + beta ** 2) * (precision * recall) / ((beta ** 2 * precision) + recall)
        if (beta ** 2 * precision) + recall > 0
        else 0.0
    )

    return {f"f{beta}": fbeta}


def f1_scorer(golds, probs, preds, uids=None, pos_label=1):
    return {"f1": fbeta_scorer(golds, probs, preds, uids, pos_label, beta=1)["f1"]}
