# Generated by Django 5.1.7 on 2025-03-25 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gameApp", "0034_alter_userprofile_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="icon",
            field=models.ImageField(
                blank=True,
                default=(
                    b"\x89PNG\r\n",
                    b"\x1a\n",
                    b"\x00\x00\x00\r",
                    b'IHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\x00\x00szz\xf4\x00\x00\x00\tpHYs\x00\x00.#\x00\x00.#\x01x\xa5?v\x00\x00\x01\tIDATX\x85\xcd\x97A\x16\x84 \x08\x86\xb17\xc7\xf1\x08\xad:\xb8+\x8f\xd0}\x9cU="@\x14G\xc7U\xf9\x90\xef\x0f\x043\xc4\\\x12,\x1c\x9f\xeb\xe1\xdc\xc31\x13|\x7f\xf8\xf503\x12\x0f&\x06\xcf\x10\xf1\xe2Q\xe8/E\xb0\xacY\xa1\xe781\x97\xb4\xd1\t\x1a\xa2\x11\x02c.I\xda\xe4\x1b79rhp\x00T\x86\x96E4\x1a\xb5\xd2\xad\xc1\x01\x94\x08H\x9b\xf3\xdc\xc3q9\xd5\xd2c\x81\x8b\x02\xbcM\xc9\n',
                    b"\x17\x05xD\xb4\xc0U\x013\xe0M\x02p\xde\xf1~\xf0\xc0\xef\x85\xcd\x8b\x06\xf9x5\xa2^'\x9eM\xeb\x12\xe0\x85\x03\x08\x8d\x08\x03\xf0;\x85i\xcd\xca]\x86\x1c\x88;'\xac\xf9\x97\xec\xbbR uI\xe9 \xd3\x8e|5\x05\xd2\xa0\xe5\x87\xe7\xb9\x14H\xf6\xdd\x028G\xbd\xf6\xae\x14X7\x9afo\x12@\x1dXOC\xba\x8e\xb5_y/P;\xe1Ha\xaa/\xe9gq\x14\xbc\xca\xf9\xab\xdf\xf2\xa5\x17\x93UW\xb3\xd0Z\xd3\xa3E\x84\x95e\x08\x00\xf0\x05\x0f}\"\">\x920\xad\x00\x00\x00\x00IEND\xaeB`\x82",
                ),
                upload_to="static/user_icons/",
            ),
        ),
    ]
