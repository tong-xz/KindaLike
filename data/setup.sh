mkdir ./yelp_dataset
mkdir ./yelp_photos
tar -xzvf yelp_dataset.tar -C ./yelp_dataset
tar -xzvf yelp_photos.tar -C ./yelp_photos
echo "All decompressed"

rm -rf ./yelp_dataset.tar
rm -rf ./yelp_photos.tar
echo "All deleted"