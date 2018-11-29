from market import Market
from tags import Tag


def update_weights() -> List[int]:
    """Update each tag's weight
    Assume that Tag objects are sorted with tag type(int)
                and each tag object has own reference number.

    :return: :list: list of weight
    :rtype: List
    """
    tags = Tag.objects.all()
    # get total number of tag reference
    total_tag_num = sum(tag.reference for tag in tags)
    # calculate each tag weight
    weights = list()
    for tag in tags:
        tag_ref = tag.reference
        weight = tag_ref / total_tag_num
        tag.weight = weight
        tag.save() # update tag object
        weights.append((tag.name, weight))
    return weights



def update_score_metric():
    """Update every scoring metric result

    :param debug: if debug mode, show log
    :type debug: Bool
    """
    # left this as an additional implementation.
    pass


if __name__ == '__main__':
    # test
    pass
