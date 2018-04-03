# Generated by Django 2.0.1 on 2018-04-03 10:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testrailcaseid', models.CharField(blank=True, max_length=12, null=True)),
                ('casedesc', models.CharField(max_length=255, verbose_name='Title')),
                ('isenabled', models.BooleanField(default=True)),
                ('issmoke', models.BooleanField(default=False)),
                ('dependent', models.CharField(blank=True, max_length=8, null=True)),
                ('debuginfo', models.CharField(blank=True, max_length=9999, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now_add=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Caseset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.CharField(max_length=200)),
                ('caseid', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('isenabled', models.BooleanField(default=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Codelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=32)),
                ('codedescr', models.CharField(max_length=255)),
                ('codevalue', models.CharField(max_length=255)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.CharField(max_length=100)),
                ('locmode', models.CharField(blank=True, choices=[('id', 'id'), ('name', 'name'), ('css selector', 'css selector'), ('xpath', 'xpath'), ('class_name', 'class name'), ('tag_name', 'tag name'), ('link_text', 'link text'), ('portial_link_text', 'portial link text')], max_length=32, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(blank=True, null=True, verbose_name='所属产品')),
                ('keyword', models.CharField(max_length=32, unique=True)),
                ('kwdescr', models.TextField(blank=True, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'ordering': ['productid'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='模块名称')),
                ('isenabled', models.BooleanField(default=True, verbose_name='状态')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('createat', models.CharField(blank=True, max_length=32, null=True, verbose_name='创建者')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('updateat', models.CharField(blank=True, max_length=32, null=True, verbose_name='更新者')),
                ('sortby', models.IntegerField(blank=True, default=0, null=True, verbose_name='排序')),
            ],
            options={
                'ordering': ['-sortby'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='产品名称')),
                ('isenabled', models.BooleanField(default=True, verbose_name='产品状态')),
                ('descr', models.TextField(blank=True, null=True, verbose_name='产品描述')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('createat', models.CharField(blank=True, max_length=32, null=True, verbose_name='创建者')),
                ('updatetime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('updateat', models.CharField(blank=True, max_length=32, null=True, verbose_name='更新者')),
                ('sortby', models.IntegerField(blank=True, default=0, null=True, verbose_name='排序')),
            ],
            options={
                'ordering': ['-sortby'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='项目名称')),
                ('version', models.CharField(blank=True, max_length=32, null=True, verbose_name='版本')),
                ('isenabled', models.BooleanField(default=True, verbose_name='状态')),
                ('descr', models.TextField(blank=True, null=True, verbose_name='项目描述')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('createat', models.CharField(blank=True, max_length=32, null=True, verbose_name='创建者')),
                ('updatetime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('updateat', models.CharField(blank=True, max_length=32, null=True, verbose_name='更新者')),
                ('sortby', models.IntegerField(blank=True, default=0, null=True, verbose_name='排序')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.Product', verbose_name='产品名称')),
            ],
            options={
                'ordering': ['-sortby'],
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stepid', models.IntegerField(blank=True, null=True)),
                ('descr', models.CharField(blank=True, max_length=200, null=True)),
                ('inputtext', models.CharField(blank=True, max_length=200, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
                ('caseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.Case')),
                ('elementid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autoplay.Element')),
                ('keywordid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=255, verbose_name='任务描述')),
                ('tasktype', models.CharField(blank=True, choices=[('1', '执行用例'), ('2', '用例同步'), ('3', '关联Jenkins')], max_length=32)),
                ('status', models.SmallIntegerField(default=0, verbose_name='任务状态')),
                ('issmoke', models.BooleanField(default=False)),
                ('testrailsuites', models.CharField(blank=True, max_length=8, null=True, verbose_name='TestRail测试集ID')),
                ('testrailrunid', models.CharField(blank=True, max_length=8, null=True, verbose_name='TestRail执行ID')),
                ('testsectionid', models.CharField(blank=True, max_length=8, null=True, verbose_name='TestRail用例节点ID')),
                ('jenkins_server_url', models.CharField(blank=True, max_length=100, null=True, verbose_name='JenkinsServer')),
                ('user_id', models.CharField(blank=True, max_length=32, null=True, verbose_name='JenkinsUserid')),
                ('api_token', models.CharField(blank=True, max_length=32, null=True, verbose_name='JenkinsApitoken')),
                ('build_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='JenkinsBuildName')),
                ('caselist', models.CharField(max_length=10240, verbose_name='用例列表')),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
                ('projectid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Taskhistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasktype', models.CharField(blank=True, max_length=32)),
                ('taskname', models.CharField(max_length=255, verbose_name='任务描述')),
                ('case_tag_all', models.CharField(blank=True, max_length=8, null=True)),
                ('case_tag_pass', models.CharField(blank=True, max_length=8, null=True)),
                ('case_tag_fail', models.CharField(blank=True, max_length=8, null=True)),
                ('case_tag_error', models.CharField(blank=True, max_length=8, null=True)),
                ('starttime', models.DateTimeField(blank=True)),
                ('exectime', models.CharField(blank=True, max_length=32, null=True)),
                ('reporturl', models.CharField(max_length=255, null=True, verbose_name='report Url')),
                ('build_name', models.CharField(blank=True, max_length=32, null=True)),
                ('build_number', models.CharField(blank=True, max_length=8, null=True)),
                ('taskid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.Task')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, null=True, unique=True, verbose_name='username')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('realname', models.CharField(blank=True, max_length=50, null=True, verbose_name='真实姓名')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('dept', models.CharField(choices=[('测试', '测试'), ('开发', '开发')], max_length=100, verbose_name='部门')),
                ('is_active', models.BooleanField(default=True, verbose_name='激活状态')),
                ('is_admin', models.BooleanField(default=False, verbose_name='是否管理员')),
                ('testrailuser', models.CharField(blank=True, max_length=50, null=True, verbose_name='TestRail用户名')),
                ('testrailpass', models.CharField(blank=True, max_length=50, null=True, verbose_name='TestRail密码')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserandProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.Product')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.User')),
            ],
        ),
        migrations.AddField(
            model_name='taskhistory',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.User'),
        ),
        migrations.AddField(
            model_name='module',
            name='projectid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.Project', verbose_name='所属项目'),
        ),
        migrations.AddField(
            model_name='element',
            name='moduleid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.Module'),
        ),
        migrations.AddField(
            model_name='element',
            name='projectid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.Project'),
        ),
        migrations.AddField(
            model_name='codelist',
            name='taskid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.Task'),
        ),
        migrations.AddField(
            model_name='case',
            name='moduleid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.Module'),
        ),
        migrations.AddField(
            model_name='case',
            name='projectid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplay.Project'),
        ),
    ]