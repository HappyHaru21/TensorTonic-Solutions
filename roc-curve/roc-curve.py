import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """
    desc = np.argsort(y_score)[::-1]
    y_true, y_score = np.array(y_true)[desc], np.array(y_score)[desc]
    idxs = np.r_[np.where(np.diff(y_score))[0], len(y_true) - 1]
    tps = np.cumsum(y_true)[idxs]
    fps = (idxs + 1) - tps
    return (np.r_[0, fps / fps[-1]], 
            np.r_[0, tps / tps[-1]], 
            np.r_[np.inf, y_score[idxs]])