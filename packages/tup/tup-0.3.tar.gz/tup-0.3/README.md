# tup
Command line tool for uploading files to Telegram

## Usage
#### Logging in, and Uploading a file
Do `tup file` to upload a file to your saved messages.  if you aren't logged in, it will automatically login for you.


#### Other options
* `-r username` - which chat to send the file to (default: self)
* `-c caption` - the caption to send with the message
* `-s` - use a different session file
* `-d` - send the file as a document


#### Logging in with a different account
I'm sure many of you use multiple accounts, or alt accounts, so to use tup with different accounts,you can just use the `-s` flag to specify a different account.  It will be saved as another `.session` file.  
For example: `tup image.png -s personal_account`
