from django.db import models
import datetime
from django.contrib.auth.models import User
from tinymce import HTMLField
import django
class TblBlog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_datetime = models.DateTimeField(default= django.utils.timezone.now)
    blog_title = models.CharField(max_length=100, blank=True, null=True)
    blog_summary = models.CharField(max_length=255, blank=True, null=True)
    blog_content = HTMLField()
    blog_like = models.IntegerField(db_column='blog_Like', blank=True, null=True)  # Field name made lowercase.
    blog_description = models.CharField(max_length=255, blank=True, null=True)
    blog_added_by = models.ForeignKey(User, models.DO_NOTHING, db_column='blog_added_by')
    blog_publish = models.ForeignKey('TblPublish', models.DO_NOTHING)
    blog_keyword = models.CharField(max_length=255, blank=True, null=True)
    blog_pics = models.FileField(upload_to='blog/',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_blog'

    def __str__(self):
        return str(self.blog_title)

class TblBlogComments(models.Model):
    blog_comments_id = models.AutoField(primary_key=True)
    blog_comments_datetime = models.DateTimeField(default= django.utils.timezone.now)
    blog = models.ForeignKey(TblBlog, models.DO_NOTHING)
    blog_comments = HTMLField()

    class Meta:
        managed = False
        db_table = 'tbl_blog_comments'

    def __str__(self):
        return str(self.blog_comments)

class TblBlogGvp(models.Model):
    blog_gvp_id = models.AutoField(primary_key=True)
    blog_gvp_datetime = models.DateTimeField(default= django.utils.timezone.now)
    blog = models.ForeignKey(TblBlog, models.DO_NOTHING)
    blog_gif = models.FileField(upload_to='blog_gvp/',blank=True, null=True)
    blog_video = models.FileField(upload_to='blog_gvp/',blank=True, null=True)
    blog_pics = models.FileField(upload_to='blog_gvp/',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_blog_gvp'

    def __str__(self):
        return str(self.blog_gvp_id)


class TblLearnData(models.Model):
    learn_data_id = models.AutoField(primary_key=True)
    learn_data_datetime = models.DateTimeField(default= django.utils.timezone.now)
    learn_topics = models.ForeignKey('TblLearnTopics', models.DO_NOTHING)
    learn_data_like = models.IntegerField(db_column='learn_data_Like', blank=True, null=True)  # Field name made lowercase.
    learn_data_icon = models.FileField(upload_to='learn_data/',blank=True, null=True)
    learn_data =  models.CharField(max_length=255, blank=True, null=True)
    learn_data_description =  HTMLField()
    learn_data_added_by = models.ForeignKey(User, models.DO_NOTHING, db_column='learn_data_added_by')
    learn_data_publish = models.ForeignKey('TblPublish', models.DO_NOTHING)
    learn_data_keyword = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_learn_data'

    def __str__(self):
        return str(self.learn_topics)


class TblLearnDataComments(models.Model):
    learn_data_comments_id = models.AutoField(primary_key=True)
    learn_data_comments_datetime = models.DateTimeField(default= django.utils.timezone.now)
    learn_data = models.ForeignKey(TblLearnData, models.DO_NOTHING)
    learn_data_comments =  HTMLField()

    class Meta:
        managed = False
        db_table = 'tbl_learn_data_comments'

    def __str__(self):
        return str(self.learn_data_comments)

class TblLearnDataGvp(models.Model):
    learn_data_gvp_id = models.AutoField(primary_key=True)
    learn_data_gvp_datetime = models.DateTimeField(default= django.utils.timezone.now)
    learn_data = models.ForeignKey(TblLearnData, models.DO_NOTHING)
    learn_data_gif = models.FileField(upload_to='learn_data_gvp/',blank=True, null=True)
    learn_data_video = models.FileField(upload_to='learn_data_gvp/',blank=True, null=True)
    learn_data_pics = models.FileField(upload_to='learn_data_gvp/',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_learn_data_gvp'

    def __str__(self):
        return str(self.learn_data_gvp_id)

class TblLearnTopics(models.Model):
    learn_topics_id = models.AutoField(primary_key=True)
    learn_topics_datetime = models.DateTimeField(default= django.utils.timezone.now)
    learn_topics = models.CharField(max_length=255, blank=True, null=True)
    learn_topics_icon = models.FileField(upload_to='learn_topics/',blank=True, null=True)
    learn_topics_coverpage_img = models.FileField(upload_to='learn_topics/',blank=True, null=True)
    learn_topics_description =  HTMLField()
    learn_topics_added_by = models.ForeignKey(User, models.DO_NOTHING, db_column='learn_topics_added_by',blank=True)
    learn_topics_publish = models.ForeignKey('TblPublish', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_learn_topics'

    def __str__(self):
        return str(self.learn_topics)

class TblPublish(models.Model):
    publish_id = models.AutoField(primary_key=True)
    input = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_publish'

    def __str__(self):
        return str(self.input)


class TblSnippetData(models.Model):
    snippet_data_id = models.AutoField(primary_key=True)
    snippet_data_datetime = models.DateTimeField(default= django.utils.timezone.now)
    snippet_topics = models.ForeignKey('TblSnippetTopics', models.DO_NOTHING)
    snippet_data_like = models.IntegerField(db_column='snippet_data_Like', blank=True, null=True)  # Field name made lowercase.
    snippet_data_icon = models.FileField(upload_to='snippet_data_gvp/',blank=True, null=True)
    snippet_data_description =  models.CharField(max_length=255, blank=True, null=True)
    snippet_data_expire = models.CharField(max_length=100, blank=True, null=True)
    snippet_data_added_by = models.ForeignKey(User, models.DO_NOTHING, db_column='snippet_data_added_by')
    snippet_data_publish = models.ForeignKey(TblPublish, models.DO_NOTHING)
    snippet_data =   models.CharField(max_length=255, blank=True, null=True)
    snippet_data_subject = models.CharField(max_length=255, blank=True, null=True)
    snippet_data_keyword = models.CharField(max_length=255, blank=True, null=True)
    snippet_data_code = HTMLField()

    class Meta:
        managed = False
        db_table = 'tbl_snippet_data'

    def __str__(self):
        return str(self.snippet_topics)

class TblSnippetDataGvp(models.Model):
    snippet_data_gvp_id = models.AutoField(primary_key=True)
    snippet_data_gvp_datetime = models.DateTimeField(default= django.utils.timezone.now)
    snippet_data = models.ForeignKey(TblSnippetData, models.DO_NOTHING)
    snippet_data_gif = models.FileField(upload_to='snippet_data_gvp/',blank=True, null=True)
    snippet_data_video = models.FileField(upload_to='snippet_data_gvp/',blank=True, null=True)
    snippet_data_pics = models.FileField(upload_to='snippet_data_gvp/',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_snippet_data_gvp'

    def __str__(self):
        return str(self.snippet_data_gvp_id)

class TblSnippetTopics(models.Model):
    snippet_topics_id = models.AutoField(primary_key=True)
    snippet_topics_datetime = models.DateTimeField(default= django.utils.timezone.now)
    snippet_topics = models.CharField(max_length=100, blank=True, null=True)
    snippet_topics_icon = models.FileField(upload_to='snippet_topics/',blank=True, null=True)
    snippet_topics_coverpage_img = models.FileField(upload_to='snippet_topics/',blank=True, null=True)
    snippet_topics_description =  HTMLField()
    snippet_topics_expire = models.CharField(max_length=100, blank=True, null=True)
    snippet_topics_added_by = models.ForeignKey(User, models.DO_NOTHING, db_column='Snippet_topics_added_by')  # Field name made lowercase.
    snippet_topics_publish = models.ForeignKey(TblPublish, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_snippet_topics'

    def __str__(self):
        return str(self.snippet_topics)


class TblHome(models.Model):
    home_id = models.AutoField(primary_key=True)
    home_datetime = models.DateTimeField(default= django.utils.timezone.now)
    home_pics = models.FileField(upload_to='home/',blank=True, null=True)
    home_content =  models.CharField(max_length=255, blank=True, null=True)
    home_content_description =  HTMLField()
    home_publish = models.ForeignKey('TblPublish', models.DO_NOTHING)
    home_added_by = models.ForeignKey(User, models.DO_NOTHING, db_column='home_added_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_home'

    def __str__(self):
        return str(self.home_id)


class TblAbout(models.Model):
    about_id = models.AutoField(primary_key=True)
    about_datetime = models.DateTimeField(default= django.utils.timezone.now)
    about_pics = models.FileField(upload_to='about/',blank=True, null=True)
    about_content = models.CharField(max_length=255, blank=True, null=True)
    about_content_description = HTMLField()
    about_publish = models.ForeignKey('TblPublish', models.DO_NOTHING)
    about_added_by = models.ForeignKey(User, models.DO_NOTHING, db_column='about_added_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_about'

    def __str__(self):
        return str(self.about_id)


class TblAboutExpert(models.Model):
    expert_id = models.AutoField(primary_key=True)
    expert_datetime = models.DateTimeField(blank=True, null=True)
    expert_name = models.CharField(max_length=255, blank=True, null=True)
    expert_skill = models.CharField(max_length=255, blank=True, null=True)
    expert_avtar = models.CharField(max_length=255, blank=True, null=True)
    expert_description =  HTMLField()
    expert_details_added_by = models.ForeignKey(User, models.DO_NOTHING, db_column='expert_details_added_by')
    expert_publish = models.ForeignKey('TblPublish', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_about_expert'
