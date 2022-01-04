from django.db import models





class Color(models.Model):
    color_name=models.CharField(max_length=20,verbose_name="颜色名称")
    color_times=models.IntegerField(verbose_name="使用次数")



    class Meta:
        db_table="colors_and_times" #表名
        verbose_name="颜色及使用次数" #admin中显示的名称
        verbose_name_plural=verbose_name #显示的复数名称


    def __str__(self):
        return self.color_name
