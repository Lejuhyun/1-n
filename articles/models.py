from django.db import models

# Create your models here.
class Article(models.Model):
    title =models.CharField(max_length =100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete= models.CASCADE)  # 데이터베이스 관계 설정(내가 연결하고 싶은 데이터)
                                                                     # on_delete: 상위 데이터가 삭제됐을 때...cascade: 하위 데이터도 삭제함
       