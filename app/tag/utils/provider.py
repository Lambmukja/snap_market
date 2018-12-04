from faker.providers import BaseProvider
from faker import Faker
"""How to use
----------------
fake = Faker('ko_KR')
fake.add_provider(MarketProvider)
fake.add_provider(MemberProvider)
fake.add_provider(ConsumerProvider)
fake.add_provider(ContractProvider)

market = fake.market()
print(market.studio_name, market.posts, market.working_time)
-----------------
"""

class MarketProvider(BaseProvider):
    def market(self, **kwargs):
        fake  = Faker('ko_KR')
        attributes = {
            'studio_name': fake.company(),
            'posts': "",
            'working_time': {
                'start_time': fake.time(pattern="%H:%M:%S",
                                        end_datetime=None),
                'end_time': fake.time(pattern="%H:%M:%S",
                                      end_datetime=None),
            },
            'costs': fake. pyint(),
            'kakao_id': fake.user_name(),
            'photographer_idx': fake.pyint(),
            'contract_idxs': [], # array of contract idx(int)
            'tags': [],
            'location': fake.address(),
            'phone': fake.phone_number(),
        }
        for key, value in kwargs.items():
            if not key in attributes:
                raise ValueError(f'Key error! There is no {key} in Makret')
            attributes[key] = value
        return attributes

class MemberProvider(BaseProvider):
    def member(self, **kwargs):
        fake  = Faker('ko_KR')
        attributes = {
            'member_type': fake.pyint() % 2,
            'consumer_idx': fake.pyint(),
            'photographer_idx': fake.pyint(),
        }
        for key, value in kwargs.items():
            if not key in attributes:
                raise ValueError(f'Key error! There is no {key} in Member')
            attributes[key] = value
        return attributes


class ConsumerProvider(BaseProvider):
    def consumer(self, **kwargs):
        fake  = Faker('ko_KR')
        attributes = {
            'member_idx': fake.pyint(),
            'contracts': [], # array of contract idx(int)
        }
        for key, value in kwargs.items():
            if not key in attributes:
                raise ValueError(f'Key error! There is no {key} in Consumer')
            attributes[key] = value
        return attributes

class PhotographerProvider(BaseProvider):
    def photographer(self, **kwargs):
        fake  = Faker('ko_KR')
        attributes = {
            markets: [], # array of market idx(int)
            member_idx: fake.pyint(),
        }
        for key, value in kwargs.items():
            if not key in attributes:
                raise ValueError(f'Key error! There is no {key} in Photographer')
            attributes[key] = value
        return attributes


class ContractProvider(BaseProvider):
    def contract(self, **kwargs):
        fake  = Faker('ko_KR')
        attributes = {
            'market_idx': fake.pyint(),
            'consumer_idx': fake.pyint(),
            'start_time': None,
            'end_time': None,
        }
        for key, value in kwargs.items():
            if not key in attributes:
                raise ValueError(f'Key error! There is no {key} in Contract')
            attributes[key] = value
        return attributes


class TagProvider(BaseProvider):
    __counter = 0
    def tag(self, **kwargs):
        fake = Faker('ko_KR')
        attributes = {
            'tag_type': type(self).__counter,
            'tag': fake.name(),
            'reference': fake.pyint(),
            'weight': fake.pyfloat(left_digits=0, positive=True),
        }
        for key, value in kwargs.items():
            if not key in attributes:
                raise ValueError(f'Key error! There is no {key} in Tag')
            attributes[key] = value
        # save tag number
        type(self).__counter += 1
        return attributes

