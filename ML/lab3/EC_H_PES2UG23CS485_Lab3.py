# lab.py
import torch

def get_entropy_of_dataset(tensor: torch.Tensor):
    """
    Calculate the entropy of the entire dataset.
    Formula: Entropy = -Σ(p_i * log2(p_i)) where p_i is the probability of class i

    Args:
        tensor (torch.Tensor): Input dataset as a tensor, where the last column is the target.

    Returns:
        float: Entropy of the dataset.
    """
    # TODO: Implement this function
    if tensor.numel() == 0:
        return 0.0

    y = tensor[:, -1]
    classes, counts = torch.unique(y, return_counts=True)
    probs = counts.float() / counts.sum()
    nonzero = probs[probs > 0]
    if nonzero.numel() == 0:
        return 0.0
    ent = -torch.sum(nonzero * torch.log2(nonzero)).item()
    return float(ent)
    


def get_avg_info_of_attribute(tensor: torch.Tensor, attribute: int):
    """
    Calculate the average information (weighted entropy) of an attribute.
    Formula: Avg_Info = Σ((|S_v|/|S|) * Entropy(S_v)) where S_v is subset with attribute value v.

    Args:
        tensor (torch.Tensor): Input dataset as a tensor.
        attribute (int): Index of the attribute column.

    Returns:
        float: Average information of the attribute.
    """
    # TODO: Implement this function
    if tensor.numel() == 0:
        return 0.0

    total = tensor.size(0)
    values, counts = torch.unique(tensor[:, attribute], return_counts=True)
    avg_info = 0.0
    for v, cnt in zip(values, counts):
        subset = tensor[tensor[:, attribute] == v]
        subset_entropy = get_entropy_of_dataset(subset)
        avg_info += (cnt.item() / total) * subset_entropy
    return float(avg_info)
    


def get_information_gain(tensor: torch.Tensor, attribute: int):
    """
    Calculate Information Gain for an attribute.
    Formula: Information_Gain = Entropy(S) - Avg_Info(attribute)

    Args:
        tensor (torch.Tensor): Input dataset as a tensor.
        attribute (int): Index of the attribute column.

    Returns:
        float: Information gain for the attribute (rounded to 4 decimals).
    """
    # TODO: Implement this function
    total_entropy = get_entropy_of_dataset(tensor)
    avg_info = get_avg_info_of_attribute(tensor, attribute)
    ig = total_entropy - avg_info
    return round(float(ig), 4)
   


def get_selected_attribute(tensor: torch.Tensor):
    """
    Select the best attribute based on highest information gain.

    Returns a tuple with:
    1. Dictionary mapping attribute indices to their information gains
    2. Index of the attribute with highest information gain
    
    Example: ({0: 0.123, 1: 0.768, 2: 1.23}, 2)

    Args:
        tensor (torch.Tensor): Input dataset as a tensor.

    Returns:
        tuple: (dict of attribute:index -> information gain, index of best attribute)
    """
    # TODO: Implement this function
    if tensor.numel() == 0 or tensor.size(1) < 2:
        return {}, None

    ncols = tensor.size(1)
    attr_indices = list(range(ncols - 1))
    gains = {}
    for a in attr_indices:
        gains[a] = get_information_gain(tensor, a)

    # pick attribute with highest gain; tie-breaker: smallest index
    best_attr = max(gains.keys(), key=lambda k: (gains[k], -k))
    return gains, best_attr
  
