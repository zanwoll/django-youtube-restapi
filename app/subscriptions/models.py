from django.db import models
from common.models import CommonModel

# - User : FK => subscription (내가 구독한 사람) -> 100명 -> 99명
# - User : FK => subscribed_to (나를 구독한 사람) -> 1만 -> 9999명

class Subscription(CommonModel):
    subscriber = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscribers')