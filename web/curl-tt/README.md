curl-tt - no response no matter what we do
==========================================
`curl-tt` requests given HTTP resource, prints response time in seconds, and
sleeps for some time before doing that all over again. Yuck.

Anyway.

```
$ curl-tt google.com
testing google.com, sleep 5s
0.041
0.040
^C
$ curl-tt example.com 0
testing example.com, sleep 0
0.270
0.271
0.278
0.276
0.278
^C
```
