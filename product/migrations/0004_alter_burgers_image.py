from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_burgers_category_alter_burgers_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burgers',
            name='image',
            field=models.ImageField(default='burgers\\empty_cart.png', null=True, upload_to='burgers'),
        ),
    ]
