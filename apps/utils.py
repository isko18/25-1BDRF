import os 

def get_product_upload_path(instance, filename):
    return os.path.join(
        'product',
        str(instance.product.id),
        filename
    )