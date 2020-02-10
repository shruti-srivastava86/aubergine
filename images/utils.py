from models import ImageUrl

def save_to_db(urls_list):
    for url_item in urls_list:
        a,b=url_item.split('.s3')
        new_url=str(a)+'-resized'+str(b)
        image_row=ImageUrl.objects.create(
            original_url=url_item,
            compressed_url=new_url
        )
        image_row.save()