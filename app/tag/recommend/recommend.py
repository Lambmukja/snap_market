import statistics
from operator import itemgetter
from typing import List, Tuple

from market.models import Market
from tag.models import Tag
from tag.recommend.config import Config


def recommend(tags: List[Tuple]):
    """Recommend with tag and return photographer id list

    :param tags: list of user tag(info(char), type(int))
    :return: return photographer 1-5th id list
    :rtype: list[tuple]
    """
    markets = Market.objects.all()
    tag_types = set(map(lambda x: x[1], tags))
    result = list()
    for market in markets:
        market_tags = set(map(lambda x: x[1], market.tags))
        matched_tags = market_tags & tag_types
        # calculate average matched weight
        filtered_tags = Tag.objects.filter(tags__in=matched_tags)
        avg_weight = statistics.mean(map(lambda x: filtered_tags.weight[x.type],
                                         filtered_tags))
        # calculate match_rate
        match_rate = len(matched_tags) / len(tags)
        score = Config.ALPHA * avg_weight + Config.GAMMA * match_rate
        result.append((market.studio_name, score))
    result = sorted(result, key=itemgetter(1))  # sort with score
    return result
