import numpy as np

from emmental.utils.utils import prob_to_pred


def precision_scorer(golds, probs, preds, uids=None, pos_label=1):
    """Precision.

    :param golds: Ground truth (correct) target values.
    :type golds: 1-d np.array
    :param probs: Predicted target probabilities. (Not used!)
    :type probs: k-d np.array
    :param preds: Predicted target values.
    :type preds: 1-d np.array
    :param uids: Unique ids.
    :type uids: list
    :return: Precision.
    :rtype: dict
    """
    if len(golds.shape) > 1:
        golds = prob_to_pred(golds)
    pred_pos = np.where(preds == pos_label, True, False)
    gt_pos = np.where(golds == pos_label, True, False)
    TP = np.sum(pred_pos * gt_pos)
    FP = np.sum(pred_pos * np.logical_not(gt_pos))

    precision = TP / (TP + FP) if TP + FP > 0 else 0.0

    return {"precision": precision}
