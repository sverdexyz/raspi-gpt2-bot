# raspi-gpt2-bot
Raspberry Pi enabled GPT2 bot plugin for Wordpress and Twitter

#usage
```
./run_gpt_wordpress.sh 'WORDPRESS_DOMAIN' 'WORDPRESS_USER' 'WORDPRESS_USER_PWD'
```

#Get Twitter credentials
https://developer.twitter.com/en/portal/products/elevated

#Install on Raspberry 4
- Recommended to be ONLY run on a Raspberry Pi as the old version of Tensorflow
  is very insecure
- 4GB RAM should be enough for the 345M model
- ONLY Tensorflow 1.1.13 works on Rapsberry Pi, use AT YOUR OWN RISK,
  as such an old Tensorflow introduces a miriad security vulerabilities.
- Twitter support is experimental and running it live using prod credentials will
  likely result in suspension of your Twitter API write priviliges. Tweet less often.

#Posting to Twitter and Nostr
Fill in the provided Nostr and Twitter credentials. For Twitter you need "Elevated" Write-enabled
developer API keys and you need to apply for them and give reasons.

https://developer.twitter.com/en

Once you have credentials post as follows:

```
python3.9 twostr twitter.json nostr.json "This is my first EVER tweet posted to Twitter and Nostr"
```