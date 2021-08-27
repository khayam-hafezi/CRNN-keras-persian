CHAR_VECTOR = "BJDSCXQLMNVHYTWAPEZRFKIGO0123456789"

letters = [letter for letter in CHAR_VECTOR]

num_classes = len(letters) + 1

img_w, img_h = 256, 64

# Network parameters
batch_size = 128
val_batch_size = 16

downsample_factor = 8
max_text_len = 8
