from models import ImageUrl

def save_to_db(urls_list):
    for url_item in urls_list:
        new_url=
        image_row=ImageUrl.objects.create(
            original_url=url_item,
            compressed_url=new_url
        )
        image_row.save()