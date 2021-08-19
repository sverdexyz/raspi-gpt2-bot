import sys
from gpt2_client import GPT2Client


from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost

YOUR_BLOG = Client('https://'+sys.argv[1]+'/xmlrpc.php', sys.argv[2], sys.argv[3])


def post_entry(title,content):
    """
    Post a blog entry to YOUR_BLOG
    """
    post = WordPressPost()
    post.title = title
    #post.slug='MY_POST_PERMANENT_LINK'
    post.content = content
    post.id = YOUR_BLOG.call(posts.NewPost(post))
    post.post_status = 'publish'
    YOUR_BLOG.call(posts.EditPost(post.id, post))
    
if __name__ == "__main__":
    """
    Run GPT2 with an input text, capture output and post it to blog
    """
    title = ' '.join(sys.argv[4:])
    print(title)


    #Note 774 or 1558 does NOT fit into Raspberry Pi RAM                                 
    gpt2 = GPT2Client('345M') # This could also be `345M`, `774M`, or `1558M`      
    gpt2.load_model(force_download=False) # Use cached versions if available.  
    gpt2_text =  gpt2.generate_batch_from_prompts(
        [title]) # returns an array of generated text
    print(gpt2_text[0])
    post_entry(title,gpt2_text)
