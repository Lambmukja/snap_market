from config import config
from operator import itemgetter
from market import Market
import statistics
from tags import Tag
from typing import Bool, List, Tuple

weight_config = config('config.json', 'DEFAULT')
alpha = weight_config['alpha']
beta = weight_config['beta']
gamma = weight_config['gamma']


def recommend(tags: List[Tuple]) -> List[int]:
    """Recommend with tag and return photographer id list

    :param tags: list of user tag(info(char), type(int))
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
        score = alpha * avg_weight + gamma * match_rate
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
