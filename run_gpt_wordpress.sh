title=`wget -q -O- "https://rss.nytimes.com/services/xml/rss/nyt/Arts.xml" |  xmlstarlet sel -T -t -m rss/channel/item/description -v . -n |head -n1`
echo $title
python3.5 post_wordpress.py $1 $2 $3 $title
