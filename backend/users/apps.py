from django.apps import AppConfig
# 引入 Django 框架中用于应用配置的基类 AppConfig。

# 创建一个名为 UsersConfig 的配置类，它继承自 AppConfig。
# 按惯例，这个类名是应用名称首字母大写加上 Config，可自定义。
class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
# 指定模型中自动创建的主键字段类型。BigAutoField 是一个 64 位的整型主键字段，适合未来大数据量的项目。
    name = "users"
# 表示该 App 的 Python 包名称是 users，即这个应用的文件夹名。
# Django 用这个字段识别这是哪个应用。