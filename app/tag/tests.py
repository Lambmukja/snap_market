import random

from faker import Faker
from django.test import TestCase
from model_mommy import mommy

from market.models import Market
from tag.utils.provider import MarketProvider, TagProvider
from tag.models import Tag
from tag.recommend.recommend import recommend


fake = Faker('ko_KR')
fake.add_provider(MarketProvider)
fake.add_provider(TagProvider)

class RecommendTestCase(TestCase):
    def setUp(self):
        self.tags = mommy.make('Tag', _quantity=5)
        self.markets = mommy.make('Market', _quantity=100)

        for i, tag in enumerate(self.tags):
            # tag attributes
            tag_attrs = fake.tag(tag_type=i)
            for key, value in tag_attrs.items():
                setattr(tag, key, value)
            tag.save()

        tags = [i for (i, tag) in enumerate(self.tags)]
        for i, market in enumerate(self.markets):
            # market attributes
            market_attrs = fake.market()
            for key, value in market_attrs.items():
                setattr(market, key, value)
            # set tag
            market_tags = random.sample(tags, random.randint(1, len(tags) - 1))
            # market only tag type list
            setattr(market, 'tags', market_tags)
            market.save()

    def test_recommend_correct(self):
        tags=[0, 1, 3]
        result = recommend(tags)
        print(result)

