# Generated by Django 5.2.1 on 2025-06-10 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="agent",
            options={
                "ordering": ["-created_time"],
                "verbose_name": "代理用户",
                "verbose_name_plural": "代理用户",
            },
        ),
        migrations.AlterField(
            model_name="agent",
            name="contact",
            field=models.CharField(blank=True, max_length=100, verbose_name="联系方式"),
        ),
        migrations.AlterField(
            model_name="agent",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="agent",
            name="free_time",
            field=models.CharField(blank=True, max_length=100, verbose_name="空闲时间"),
        ),
        migrations.AlterField(
            model_name="agent",
            name="password",
            field=models.CharField(max_length=255, verbose_name="密码"),
        ),
        migrations.AlterField(
            model_name="agent",
            name="personal_info",
            field=models.TextField(blank=True, verbose_name="个人简介"),
        ),
        migrations.AlterField(
            model_name="agent",
            name="role",
            field=models.CharField(
                choices=[("agent", "探员"), ("admin", "管理员")],
                default="agent",
                max_length=10,
                verbose_name="角色",
            ),
        ),
        migrations.AlterField(
            model_name="agent",
            name="status",
            field=models.BooleanField(default=True, verbose_name="状态"),
        ),
        migrations.AlterField(
            model_name="agent",
            name="updated_time",
            field=models.DateTimeField(auto_now=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="agent",
            name="username",
            field=models.CharField(max_length=50, unique=True, verbose_name="用户名"),
        ),
        migrations.AlterField(
            model_name="agent",
            name="wx_qrcode",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="微信二维码"
            ),
        ),
        migrations.AlterModelTable(
            name="agent",
            table="agents",
        ),
    ]
