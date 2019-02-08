var express = require('express'); // Use Express in our app

var app = express(); // Create Express object

port = 3000; // Assign port to listen on

// Create app GET request on '/' route
// Request sends back 'Project Nani' to web browser
app.get('/', (req,res) => res.send('Project Nani'))

// App will listen for requests
app.listen(port, () => console.log(`Listening on port ${port}`))

