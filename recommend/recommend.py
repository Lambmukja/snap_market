from operator import itemgetter
from typing import Bool, List, Tuple
from market import Post
from tags import Tag

def recommend(tags: List[Tuple], debug=False: Bool) -> List[int]:
    """Recommend with tag and return photographer id list

    :param tags: list of user tag(info(char), type(int))
    :param debug; if debbuging, show search result.
    :type debug: bool
    :return: return photographer 1-5th id list
    :rtype: list[int]
    """
    # fetch tag list
    tag_objs = list(Tag.objects.all().order_by('type').values('name', 'type'))
    tag_names, tag_types = map(list, zip(*tag_objs))
    # check if there is non-exist tag type
    if not all(name in tag_types for name in tag_objs):
        raise ValueError('there is non-exist tag type in input tag list')

    # search by score
    """check point
        - [ ] How to measuring score.
        - [ ] How to store related field in database.
        - [ ] What value type to return.
    """
    posts = list(Post.objects.filter(tags__in=tags).order_by('score'))
    return posts[0:5]


if __name__ == '__main__':
    pass
