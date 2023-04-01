# USAGE

## USING A BROWSER
1. Open the project in PyCharm or any environment.
2. Run main.py.
3. ```Running on http://127.0.0.1:5000``` will show up on the screen.
4. Click on the link and click on ```Choose file ``` to choose the image from your computer: for example 
"shoe_noembed0.png".
5. Click on ```Upload```.
6. The most similar three images will show up on the screen together with the scores, in this case I used RMSE. The 
message will look like this ```[{"filename": "shoe4.png", "rmse": 0.5898408624529249}, {"filename": "shoe2.png", 
"rmse": 0.590007850260575}, {"filename": "shoe7.png", "rmse": 0.5893073725446797}]```.

## USING POSTMAN
1. Run main.py the same as in the example above.
2. Create a workspace on POSTMAN.
3. Choose the request type POST.
4. Enter the link: ```http://127.0.0.1:5000/similar-images```.
5. Click on ```Body``` and enter the ```Key:``` 'image' and at ```Value:``` choose an image from your computer such as 
"shoe_noembed0.png".
6. Click on ```Send```.
7. In the ```Body``` section below you should see the response ```[{"filename": "shoe0.png", "rmse": 0.5754255766178371}
, {"filename": "shoe1.png", "rmse": 0.5756348026208905}, {"filename": "shoe2.png", "rmse": 0.5756609152451475}]```.


## Relational Databases
Are they a good way to store image embeddings? Relational databases are good at storing organised information that has 
predictable structure and size, which makes it difficult to change these aspects. If the embeddings look like the ones 
in the parquet file and do not change length, i.e. each image has an embedding of size 1024, then yes, relational databases can be 
used to store the embeddings.
