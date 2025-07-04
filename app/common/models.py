from django.db import models

# - created_at : 데이터 생성시간
# - updated_at : 데이터 업데이트 시간

class CommonModel(models.Model):
    # 생성된 시간 (고정)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # 데이터가 업데이트된 시간 => 데이터가 업데이트 될 때마다 시간이 계속 변경
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True # DB에 테이블을 추가하지 마시오.