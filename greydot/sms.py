"""
Use the API to send an sms to a number. If you enable notify by email, you will receive an email every time the url is called with your APP Key.

URL :
https://greydotapi.me/?par1=[Number to SMS]&par2=[url encoded text message]&k=[APP Key]&do=[FID]

[Number to SMS]Number that will receive the sms message or list of numbers each separated by an e
[url encoded text message]Text to be sent to number in url encoded form
[APP Key] Your APP Key
[FID]The function ID for Send sms is 11

Bulk Example url :
https://greydotapi.me/?par1=0820000000e0820000001e0820000002&
par2=Test+sms%2C+Hallo+world.&k=abcdefghijklmnopqrst&do=11
Example url :
https://greydotapi.me/?par1=0820000000&
par2=Test+sms%2C+Hallo+world.&k=abcdefghijklmnopqrst&do=11

Example reply :
<?xml version="1.0" encoding="utf-8" ?>
<query>
    <query_result>
      <status>Success</status>
      <status>Send_SMS</status>
      <to>27110000000</to>
      <sms_id>000</sms_id>
    </query_result>
<query_status>DONE</query_status>
<query_code>D0011</query_code>
</query>
"""
