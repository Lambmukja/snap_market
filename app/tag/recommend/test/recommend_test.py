"""
# fetch tag list
tag_objs = list(Tag.objects.all().order_by('type').values('name', 'type'))
tag_names, tag_types = map(list, zip(*tag_objs))
# check if there is non-exist tag type
if not all(name in tag_types for name in tags):
    raise ValueError('there is non-exist tag type in input tag list')
"""
