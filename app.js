var express = require('express');
var shellescape = require('shell-escape');
var config = require('config');
var exec = require('child_process').exec
var app = express();

app.get('/', function(req, res) {
  say('Hello my name is Mia!');
  res.send('Hello my name is Mia!');
});

var server = app.listen(3000, function() {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});

function say(phrase) {
  var args = config.get('Speak.cmd').split(' ').concat([' "' + phrase + '"']);
  console.log(args);
  exec(shellescape(args), log);
}
function log(error, stdout, stderr) { console.log(stdout);console.log(stderr) }
