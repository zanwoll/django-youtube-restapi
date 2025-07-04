from django.db import models
from common.models import CommonModel

# - User: FK
    # => User : Comment => 1 : N
    # => User : Comment, Comment, Comment => 0
    # => Comment : User, User, User => X
# - Video: FK
    # => Video : Comment => 1 : N(FK)
    # => Video : Comment, Comment, Comment => 0
    # => Comment : Video, Video, Video => X
# - content: TextField
# - dislike : PositiveIntegerField

class Comment(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)
    # 법적인 이슈랑 연결이 되어있어요. (정보 통신 보호법 + Euro 6)
    
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    
    # 대댓글
    # parnet = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)