import pandas as pd
from simplegmail import Gmail

client = Gmail()

params = {
  "to": "",
  "sender": "kinjawadekaradi112@gmail.com",
#   "cc": ["bob@bobsemail.com"],
#   "bcc": ["marie@gossip.com", "hidden@whereami.com"],
  "subject": "Test mail",
#   "msg_html": "<h1>Woah, my first email!</h1><br />This is an HTML email.",
  "msg_plain": "Hi\nThis is a plain text email.",
  "attachments": ["path/to/something/cool.pdf", "path/to/image.jpg", "path/to/script.py"],
  "signature": True  # use my account signature
}

fparams = []

# print(params)
df = pd.read_csv('gmail.csv')
# print(df)


names_array = df['name'].to_list()
emails_array = df['email'].to_list()
# print(names_array, emails_array)


# name = "piyush"
# html_template = f'<div><div class="adM"> </div><div> Hey {name}, </div><div> &nbsp; </div><div> I hope you\'re doing great! I’ve been following your insta page and I have to say, your content is absolutely lit! Your creativity really shines through, and it’s clear you put a ton of effort into it. </div><div> &nbsp; </div><div> That said, </div><div> I noticed there’s some room for enhancing the editing, </div><ul><li><strong>Edits are slow</strong></li><li><strong>Lacks good color grading</strong></li><li><strong>Your content is great but lacks retention</strong></li></ul><div> And that’s where I can help. I’m a video editor with experience working on hundreds of videos, and I’d love to assist you in making your videos even more engaging and polished. </div><div> &nbsp; </div><div> Here check <a href="https://myvideoeditingportfolio.my.canva.site/myportfolio" rel="noopener" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://myvideoeditingportfolio.my.canva.site/myportfolio&amp;source=gmail&amp;ust=1729443084781000&amp;usg=AOvVaw3fJVZmFSLT78F_TsS-l6AO">my portfolio</a> </div><div> &nbsp; </div><div> If you\'re open to it, I’d be happy to chat and see how we can collaborate </div><div> If you are interested ping me - <a href="http://t.me/Pranavj4712" rel="noopener" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://t.me/Pranavj4712&amp;source=gmail&amp;ust=1729443084781000&amp;usg=AOvVaw2omhqQqn7xqV2YA5EccnhM">Here</a> </div><div> &nbsp; </div><div> Looking forward to hearing from you. </div><div> &nbsp; </div><div> Best regards, </div><div> Pranav Jadhav </div><div class="yj6qo"></div><div class="adL"> </div><div class="adL"> &nbsp; </div><div class="adL"> </div></div>'

# print(html_template)





for i in range(len(emails_array)):
    fparams.append({
        "to" : emails_array[i],
        "sender" : "kinjawadekaradi112@gmail.com",
        "subject" : "Test mail",
        "msg_html": f'<div><div class="adM"> </div><div> Hey {names_array[i]}, </div><div> &nbsp; </div><div> I hope you\'re doing great! I’ve been following your insta page and I have to say, your content is absolutely lit! Your creativity really shines through, and it’s clear you put a ton of effort into it. </div><div> &nbsp; </div><div> That said, </div><div> I noticed there’s some room for enhancing the editing, </div><ul><li><strong>Edits are slow</strong></li><li><strong>Lacks good color grading</strong></li><li><strong>Your content is great but lacks retention</strong></li></ul><div> And that’s where I can help. I’m a video editor with experience working on hundreds of videos, and I’d love to assist you in making your videos even more engaging and polished. </div><div> &nbsp; </div><div> Here check <a href="https://myvideoeditingportfolio.my.canva.site/myportfolio" rel="noopener" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://myvideoeditingportfolio.my.canva.site/myportfolio&amp;source=gmail&amp;ust=1729443084781000&amp;usg=AOvVaw3fJVZmFSLT78F_TsS-l6AO">my portfolio</a> </div><div> &nbsp; </div><div> If you\'re open to it, I’d be happy to chat and see how we can collaborate </div><div> If you are interested ping me - <a href="http://t.me/Pranavj4712" rel="noopener" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://t.me/Pranavj4712&amp;source=gmail&amp;ust=1729443084781000&amp;usg=AOvVaw2omhqQqn7xqV2YA5EccnhM">Here</a> </div><div> &nbsp; </div><div> Looking forward to hearing from you. </div><div> &nbsp; </div><div> Best regards, </div><div> Pranav Jadhav </div><div class="yj6qo"></div><div class="adL"> </div><div class="adL"> &nbsp; </div><div class="adL"> </div></div>', 
        "msg_plain" : f"Hi {names_array[i]}, this is a test mail",
        "signature" : True
    })

# print(fparams)
for i in fparams:
    # print(i) 
    message = client.send_message(**i) 
