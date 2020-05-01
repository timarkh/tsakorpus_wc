# A shell script used to prepare the corpus files for indexing.
# Generates word lists, annotates them, runs a convertor and puts
# the resulting JSON files to the appropriate folder.
# Also moves the images from the folder specified by the user.
START_TIME="$(date -u +%s)"
cd src_convertors/corpus
python3 concordancer.py
echo "Word lists generated."
# Russian morphology (Yandex's mystem)
wget http://download.cdn.yandex.net/mystem/mystem-3.1-linux-64bit.tar.gz
tar -xf mystem-3.1-linux-64bit.tar.gz
sed -i 's/\t[0-9]+//g' russian_wordlist.csv
./mystem -ni --eng-gr --format xml russian_wordlist.csv russian_wordlist.csv-parsed.txt
# rm russian_wordlist.csv
rm mystem-3.1-linux-64bit.tar.gz
rm mystem
sed -i 's/=" \/>/" \//g' russian_wordlist.csv-parsed.txt
sed -i 's/<ana lex="[^<>"]" gr="S,abbr[^<>"]*" \/>//g' russian_wordlist.csv-parsed.txt
echo "Russian word list analyzed."

# Conversion to Tsakorpus JSON
python3 prepare_meta.py
cd ..
python3 img_csv2json.py
echo "Source conversion ready."

find corpus -type f -name '*_wordlist.csv' -delete
find corpus -type f -name '*-parsed.txt' -delete
rm corpus/meta_enhanced.csv
rm -rf ../corpus/wc_corpus
mkdir -p ../corpus/wc_corpus
mv corpus/json ../corpus/wc_corpus
echo "JSON files moved."

cd ..
rm -rf search/img
mkdir search/img
python3 move_images.py
END_TIME="$(date -u +%s)"
ELAPSED_TIME="$(($END_TIME-$START_TIME))"
echo "Corpus files prepared in $ELAPSED_TIME seconds, finishing now."