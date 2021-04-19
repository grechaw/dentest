<<<<<<< HEAD
<<<<<<< HEAD
# dentest
=======
=======
This is a service intended for serving up model inference that takes a long time, too long for a synchronous request.
>>>>>>> 5db0c75 (three modes)

So one URL fires off a "job"

It takes as parameter an array of S3 paths.
The serve endpoint
* returns with status of "starting check back here..."

* starts a session  --- how should one session authorize another one -- ENV variable with anyscale token is only way now.

* runs a prediction job
* stores results of prediction in new bucket location.
* changes status to done, with result location
* terminates the session
* removes it?



The second returns a job status, and if finished, the location? of returned data.

-----------------

OK first question in the prototype... the prd has one session running, say, the serve endpoints, and other ones getting created and run.  

My assumption is that this is a requirement because different ad-hoc jobs will have different compute requirements that should be exposed to the caller... however, this is an assumption.


<<<<<<< HEAD

>>>>>>> 3a16289 (initial commit)
=======
requests.post("http://localhost:8080/start", {})
>>>>>>> 5db0c75 (three modes)
