import PIL
import numpy as np
import pandas as pd
import json


def most_similar_images(img, n_similar=3):
    # embeddings of input img set to random
    input_embeddings = np.random.rand(1024)

    # read embeddings of imgs
    df_saved_images = pd.read_parquet("embeddings_df.parquet", engine='pyarrow')

    n_rows = df_saved_images.shape[0]
    rmse_images = []

    for row_index in range(n_rows):

        # Get the row using index
        row = df_saved_images.iloc[row_index]

        # calculate rmse
        rmse = np.sqrt(np.mean((row - input_embeddings) ** 2))

        # append tuple with rmse and row index
        rmse_images.append((rmse, row_index))

    # sort by smallest rmse
    sorted_rmse = sorted(rmse_images)
    first_three = sorted_rmse[:n_similar]

    # get name/ index of smallest rmse: index 1 means shoe1
    image_names = ["shoe" + str(item[1]) + ".png" for item in first_three]

    # put images and scores (rmse) in json
    objects = []
    for i in range(n_similar):
        obj = {'filename': image_names[i], 'rmse': rmse_images[i][0]}
        objects.append(obj)

    return json.dumps(objects)
