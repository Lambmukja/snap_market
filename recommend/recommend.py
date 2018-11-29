from config import config
from operator import itemgetter
from market import Market
import statistics
from tags import Tag
from typing import Bool, List, Tuple

params = config()
alpha, beta, gamma = params.values()

def update_weights():
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
    for tag in tags:
        tag_ref = tag.reference
        weight = tag_ref / total_tag_num
        tag.weight = weight
        tag.save() # update tag object


def update_score_metric(debug=False: Bool):
    """Update every scoring metric result
    :param debug: if debug mode, show log
    :type debug: Bool
    """
    # left this as an additional implementation.
    pass


def recommend(tags: List[Tuple], debug=False: Bool) -> List[int]:
    """Recommend with tag and return photographer id list
    :param tags: list of user tag(info(char), type(int))
    :param debug; if debbuging, show search result.
    :type debug: Bool
    :return: return photographer 1-5th id list
    :rtype: list[int]
    """
    markets = Market.objects.all()
    tag_types = set(map(lambda x: x[1], tags))
    result = list()
    for market in markets:
        market_tag_types = set(map(lambda x: x[1], market.tags))
        matched_tags = market_tags & tag_types
        # calculate average matched weight
        filtered_tags = Tag.objects.filter(tags__in=matched_tags)
        avg_weight = statistics.mean(map(lambda x: weight[x.type],
                                                   filtered_tags))
        # calculate match_rate
        match_rate = len(matched_tags) / len(tags)
        score = alpha * avg_weight +  + gamma * match_rate
        result.append((market.studio_name, score))
    result = sorted(result, key=itemgetter(1)) # sort with score
    return result


if __name__ == '__main__':
    """
    # fetch tag list
    tag_objs = list(Tag.objects.all().order_by('type').values('name', 'type'))
    tag_names, tag_types = map(list, zip(*tag_objs))
    # check if there is non-exist tag type
    if not all(name in tag_types for name in tags):
        raise ValueError('there is non-exist tag type in input tag list')
    """
    pass
