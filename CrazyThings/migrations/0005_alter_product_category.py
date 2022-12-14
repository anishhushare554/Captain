# Generated by Django 4.1.3 on 2022-11-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CrazyThings", "0004_alter_product_category"),
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
                    ("ru", "running"),
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
                    ("sw", "smartwatch"),
                    ("p", "printer"),
                    ("ch", "chair"),
                    ("tb", "table"),
                    ("sf", "sofa"),
                    ("oc", "officechair"),
                    ("ot", "officetable"),
                    ("os", "officesofa"),
                    ("kb", "kidsbed"),
                    ("ks", "kidsstudy"),
                    ("kst", "kidsseating"),
                    ("otf", "other_furniture"),
                    ("AC", "Air Conditioner"),
                    ("R", "Refrigerator"),
                    ("WM", "Washing Machine"),
                    ("cs", "CookwareSet"),
                    ("gs", "GasStove"),
                    ("mx", "Mixer"),
                    ("jc", "Juicer"),
                    ("ck", "Cooker"),
                    ("hb", "HandBlender"),
                    ("tw", "Tawa"),
                    ("ds", "DinnerSet"),
                    ("ts", "TiffinSet"),
                    ("gl", "GlassSet"),
                    ("cj", "CopperJug"),
                    ("ss", "SpoonSet"),
                    ("pi", "PoojaItem"),
                    ("bi", "BrassItem"),
                    ("hp", "Hotpot"),
                    ("mk", "Kurta"),
                    ("msh", "Sherwani"),
                    ("ms", "suit"),
                    ("wk", "kurti"),
                    ("wsa", "Saree"),
                    ("wsu", "Suit"),
                    ("kb", "Boys"),
                    ("kg", "Girls"),
                    ("br", "brooch"),
                    ("ml", "mala"),
                    ("jt", "juti"),
                    ("sf", "safa"),
                    ("kp", "kamarpatta"),
                    ("jw", "jwellery"),
                    ("er", "earrings"),
                    ("dp", "Dipers"),
                    ("bsc", "Baby_skin_care"),
                    ("bd", "Baby_Diagestions"),
                    ("sp", "sanitary_pads"),
                    ("wmv", "women_multivitamines"),
                    ("hr", "hair_removal"),
                    ("fc", "face_care"),
                    ("hs", "handwash_sanitizer"),
                    ("cc", "cold_cough"),
                    ("dc", "diabetic_care"),
                    ("ac", "abdomen_care"),
                ],
                max_length=5,
            ),
        ),
    ]
