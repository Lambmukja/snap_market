import statistics
from operator import itemgetter
from typing import List

from market.models import Market
from tag.models import Tag
from tag.recommend.config import Config


def recommend(user_tags: List[int]):
    """Recommend with tag and return photographer id list

    :param user_tags: list of user tag(type(int))
    :return: return list of each market name and market's score
    :rtype: list[tuple]
    """
    tags = Tag.objects.all()
    markets = Market.objects.all()
    user_tag_ids = set(user_tags)
    result = list()
    for market in markets:
        # get only market's tags and convert to set
        market_tags = set(market.tags)
        matched_tags = list(market_tags & user_tag_ids)  # set & operation

        # calculate average matched weight
        filtered_tags = Tag.objects.filter(id__in=matched_tags)
        if not filtered_tags:
            continue
        weights = [tag.weight for tag in filtered_tags]
        avg_weight = statistics.mean(weights)
        # calculate match_rate
        match_rate = len(matched_tags) / len(user_tags)
        score = Config.ALPHA * avg_weight + Config.GAMMA * match_rate
        result.append((market, score))

    result = sorted(result, key=itemgetter(1), reverse=True)  # sort with as decreasing order
    return result
