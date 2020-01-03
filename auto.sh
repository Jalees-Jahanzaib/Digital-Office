user="Jalees-Jahanzaib"
pswd="mmmajic@786"
git add .
git commit -m "$1"
git push 
expect "Username for 'https://www.github.com':"
{
send "$user\r"
}
expect "Password for 'https://$user@github.com':"
{
send "$pswd"
}