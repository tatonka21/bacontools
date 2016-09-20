content-length - Uroboros that will cover the world
===================================================
`content-length` accepts one or several URLs and prints total size of their
content in bytes. It will default to reading `Content-Length` header, and, if
this header is not supplied by the server, it will download the file instead.

```
$ content-length https://i.imgur.com/OUXdexa.jpg https://i.imgur.com/UQOazoo.jpg https://i.imgur.com/FRHwPM4.jpg
10327788
$ curl -sI https://i.imgur.com/OUXdexa.jpg https://i.imgur.com/UQOazoo.jpg https://i.imgur.com/FRHwPM4.jpg | grep Content-Length
Content-Length: 4352398
Content-Length: 4227440
Content-Length: 1747950
```
