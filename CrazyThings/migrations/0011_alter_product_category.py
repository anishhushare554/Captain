# Generated by Django 4.1.3 on 2022-12-01 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CrazyThings", "0010_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("cr", "cricket"),
                    ("ba", "badminton"),
                    ("cy", "cycling"),
                    ("fo", "football"),
                    ("sw", "swimming"),
                    ("vb", "volleyball"),
                    ("bb", "basketball"),
                    ("tt", "tabletennis"),
                    ("m", "mobile"),
                    ("tv", "television"),
                    ("l", "laptop"),
                    ("c", "camera"),
                    ("hp", "Headphone"),
                    ("s", "speaker"),
                    ("sm", "smartwatch"),
                    ("p", "printer"),
                    ("b", "beds"),
                    ("so", "sofas"),
                    ("ch", "chairs"),
                    ("t", "tables"),
                    ("w", "wardrobes"),
                    ("sh", "shelves"),
                    ("ca", "cabinet"),
                    ("ma", "mattress"),
                    ("ac", "air"),
                    ("v", "vitamins"),
                    ("p", "personal"),
                    ("fv", "fruitvegetable"),
                    ("be", "beverages"),
                    ("fg", "foodgrains"),
                    ("co", "cookies"),
                    ("no", "noodles"),
                    ("ol", "oil"),
                    ("sn", "snacks"),
                    ("de", "deo"),
                ],
                max_length=5,
            ),
        ),
    ]
