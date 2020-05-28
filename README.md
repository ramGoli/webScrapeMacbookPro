# webScrapeMacbookPro
checks apple refurbished website for 'macbook pro 16' and sends an email.

Need to configure with own AWS SES credentials for sending email. Can also use IAM Role with SES attached to EC2 if you can't use secret key and access id in script. 

I use it with lightsail vps which doesn't support attaching IAM role to it. 
